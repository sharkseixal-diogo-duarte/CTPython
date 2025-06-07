import cv2
import numpy as np
import pyautogui
import time
import keyboard

# Região do jogo (x, y, largura, altura)
test_area = (400, 200, 200, 150)

time.sleep(3)
pyautogui.press("space")  # Começa o jogo

try:
    while True:
        if keyboard.is_pressed('q'):
            break

        screenshot = pyautogui.screenshot(region=test_area)
        frame = np.array(screenshot)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

        # Região do obstáculo (ajuste conforme necessário)
        obstacle_area = thresh[60:100, 150:180]
        obstacle_pixels = cv2.countNonZero(obstacle_area)

        print("Pixels detectados:", obstacle_pixels)  # Debug

        if obstacle_pixels > 50:  # Experimente valores mais baixos
            pyautogui.press("space")  # ou "space"
            print("Pulo!")
            
        if obstacle_pixels > 50:  # Experimente valores mais baixos
            pyautogui.press("down")  # ou "space"
            print("Pulo!")
            
        cv2.imshow("Área de Detecção", obstacle_area)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Interrompido pelo usuário.")
finally:
    cv2.destroyAllWindows()
