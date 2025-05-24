import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# Configurações iniciais
screen_width, screen_height = pyautogui.size()
pyautogui.FAILSAFE = False

# Inicializa MediaPipe
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5)

# Índices dos pontos dos olhos
LEFT_EYE = [33, 133]  # canto interno e externo do olho esquerdo
RIGHT_EYE = [362, 263]  # canto interno e externo do olho direito
UPPER_LID = [159, 386]  # parte de cima dos olhos (para detecção de piscada)
LOWER_LID = [145, 374]  # parte de baixo dos olhos

# Função para detectar piscada
def eye_aspect_ratio(upper, lower):
    return np.linalg.norm(upper - lower)

cap = cv2.VideoCapture(0)

blink_threshold = 3.5  # limiar para detectar piscada (ajuste se necessário)
click_cooldown = 1  # segundos entre cliques
last_click_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img_h, img_w, _ = frame.shape

    results = face_mesh.process(rgb_frame)

    if results.multi_face_landmarks:
        mesh_points = results.multi_face_landmarks[0].landmark

        # Coordenadas dos olhos
        left_eye = np.array([
            [mesh_points[LEFT_EYE[0]].x * img_w, mesh_points[LEFT_EYE[0]].y * img_h],
            [mesh_points[LEFT_EYE[1]].x * img_w, mesh_points[LEFT_EYE[1]].y * img_h]
        ])
        right_eye = np.array([
            [mesh_points[RIGHT_EYE[0]].x * img_w, mesh_points[RIGHT_EYE[0]].y * img_h],
            [mesh_points[RIGHT_EYE[1]].x * img_w, mesh_points[RIGHT_EYE[1]].y * img_h]
        ])

        # Centro dos olhos para controle de cursor
        eye_center = np.mean(np.concatenate((left_eye, right_eye)), axis=0)

        # Mapeia para tela
        screen_x = int((eye_center[0] / img_w) * screen_width)
        screen_y = int((eye_center[1] / img_h) * screen_height)
        pyautogui.moveTo(screen_x, screen_y, duration=0.1)

        # Detecta piscada
        upper = np.array([
            [mesh_points[UPPER_LID[0]].x * img_w, mesh_points[UPPER_LID[0]].y * img_h],
            [mesh_points[UPPER_LID[1]].x * img_w, mesh_points[UPPER_LID[1]].y * img_h]
        ])
        lower = np.array([
            [mesh_points[LOWER_LID[0]].x * img_w, mesh_points[LOWER_LID[0]].y * img_h],
            [mesh_points[LOWER_LID[1]].x * img_w, mesh_points[LOWER_LID[1]].y * img_h]
        ])

        ear = eye_aspect_ratio(upper[0], lower[0]) + eye_aspect_ratio(upper[1], lower[1])

        if ear < blink_threshold and (time.time() - last_click_time) > click_cooldown:
            pyautogui.click()
            last_click_time = time.time()

    cv2.imshow('Eye Tracker', frame)

    if cv2.waitKey(1) == 27:  # ESC para sair
        break

cap.release()
cv2.destroyAllWindows()
# .\.venv\Scripts\activate