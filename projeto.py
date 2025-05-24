import os
import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time
# Configurations
screen_width, screen_height = pyautogui.size()
pyautogui.FAILSAFE = False

# Face mesh points for blink detection (eyes)
UPPER_LID = [159, 386]  # upper eyelid points
LOWER_LID = [145, 374]  # lower eyelid points

# Iris center landmarks (MediaPipe face mesh with refine_landmarks=True)
LEFT_IRIS_CENTER = 468
RIGHT_IRIS_CENTER = 473

# Thresholds and cooldown
BLINK_THRESHOLD = 3.5      # EAR threshold for blink detection
CLICK_COOLDOWN = 0.5       # seconds between clicks

def eye_aspect_ratio(upper, lower):
    """Calculate vertical distance between upper and lower eyelid points."""
    return np.linalg.norm(upper - lower)

def main():
    cap = cv2.VideoCapture(0)
    last_click_time = 0

    mp_face_mesh = mp.solutions.face_mesh

    # Enable refine_landmarks=True to include iris landmarks
    with mp_face_mesh.FaceMesh(
        static_image_mode=False,
        max_num_faces=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
        refine_landmarks=True
    ) as face_mesh:

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img_h, img_w, _ = frame.shape

            results = face_mesh.process(rgb_frame)

            if results and results.multi_face_landmarks:
                mesh_points = results.multi_face_landmarks[0].landmark

                # Get iris center coordinates for left and right eyes
                left_iris = mesh_points[LEFT_IRIS_CENTER]
                right_iris = mesh_points[RIGHT_IRIS_CENTER]

                # Calculate average iris position (x, y) scaled to image size
                iris_x = (left_iris.x + right_iris.x) / 2 * img_w
                iris_y = (left_iris.y + right_iris.y) / 2 * img_h

                # Map iris position to screen coordinates
                screen_x = int((iris_x / img_w) * screen_width)
                screen_y = int((iris_y / img_h) * screen_height)

                # Move the cursor to the iris position
                pyautogui.moveTo(screen_x, screen_y, duration=0.1)

                # Blink detection using upper and lower eyelid points
                upper = np.array([
                    [mesh_points[UPPER_LID[0]].x * img_w, mesh_points[UPPER_LID[0]].y * img_h],
                    [mesh_points[UPPER_LID[1]].x * img_w, mesh_points[UPPER_LID[1]].y * img_h]
                ])
                lower = np.array([
                    [mesh_points[LOWER_LID[0]].x * img_w, mesh_points[LOWER_LID[0]].y * img_h],
                    [mesh_points[LOWER_LID[1]].x * img_w, mesh_points[LOWER_LID[1]].y * img_h]
                ])

                ear = (eye_aspect_ratio(upper[0], lower[0]) + eye_aspect_ratio(upper[1], lower[1])) / 2

                current_time = time.time()
                if ear < BLINK_THRESHOLD and (current_time - last_click_time) > CLICK_COOLDOWN:
                    pyautogui.click()
                    last_click_time = current_time

            # Show the camera feed window
            cv2.imshow('Eye Tracker - Iris Cursor & Blink Click', frame)

            if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
#.\.venv\Scripts\activate      
