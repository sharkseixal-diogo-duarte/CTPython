import cv2
import pyautogui
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

webcam = cv2.VideoCapture(0)

while True:

    ret, frame = webcam.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eyes = eye_cascade.detectMultiScale(gray, 1.3 ,5)
    UPPER_LID = [159, 386]  # upper eyelid points
    LOWER_LID = [145, 374]  # lower eyelid points

    # Iris center landmarks (MediaPipe face mesh with refine_landmarks=True)
    LEFT_IRIS_CENTER = 468
    RIGHT_IRIS_CENTER = 473

    # Thresholds and cooldown
    BLINK_THRESHOLD = 3.5  # EAR threshold for blink detection
    CLICK_COOLDOWN = 0.5  # seconds between clicks

    for(x,y,w,h) in eyes:

        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

    pyautogui.moveTo(UPPER_LID, LOWER_LID, duration=0.1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imshow("face and eyes detector",frame)