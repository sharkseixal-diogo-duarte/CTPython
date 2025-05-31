import cv2
import numpy as np
import pyautogui
import time

# Região da tela onde está o jogo (ajuste conforme sua tela)
# Exemplo: (left, top, width, height)
game_area = (300, 400, 600, 150)

# Aguarda 3 segundos antes de iniciar
print("Iniciando em 3 segundos...")
time.sleep(3)
print("Bot rodando...")

while True:
    # Captura de tela da região do jogo
    screenshot = pyautogui.screenshot(region=game_area)
    frame = np.array(screenshot)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

    # Região onde o obstáculo costuma aparecer (área da frente do dinossauro)
    obstacle_area = thresh[60:120, 250:300]

    # Conta os pixels brancos (que representam os obstáculos)
    obstacle_pixels = cv2.countNonZero(obstacle_area)

    if obstacle_pixels > 100:
        pyautogui.press("space")  # Dino pula
        print("Pulo!")

    # Apenas para controle de visualização (remover se quiser rodar mais leve)
    # cv2.imshow("Obstacle Area", obstacle_area)
    # if cv2.waitKey(1) == ord('q'):
    #     break
