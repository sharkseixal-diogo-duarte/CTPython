import cv2
import numpy as np
import pyautogui
import time
import keyboard
test_area = (400, 150, 220, 150)
pyautogui.press("win")
time.sleep(0.7)
pyautogui.write("chrome")
time.sleep(0.7)
pyautogui.press("enter")
time.sleep(0.7)
pyautogui.write("https://chrome-dino-game.github.io/")
time.sleep(0.7)
pyautogui.press("enter")
time.sleep(0.7)
pyautogui.press("space")
time.sleep(0.3)
pyautogui.click(1225,60)
try:
    while True:
        if keyboard.is_pressed('q'):
            break

        screenshot = pyautogui.screenshot(region=test_area)
        frame = np.array(screenshot)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

        obstacle_area = thresh[60:100, 150:180]
        obstacle_pixels = cv2.countNonZero(obstacle_area)

        print("Pixels detectados:", obstacle_pixels)

        if obstacle_pixels > 50 and obstacle_pixels < 999:
            pyautogui.press("space")

        if obstacle_pixels > 1000 and obstacle_pixels < 1190:
            _, thresh_white = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)
            obstacle_area_white = thresh[60:100, 150:180]
            obstacle_pixels_white = cv2.countNonZero(obstacle_area)
            pyautogui.press("space")
        cv2.imshow("Área de Detecção", thresh)
        print("Pixels detectados:", obstacle_pixels_white)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Interrompido pelo usuário.")
finally:
    cv2.destroyAllWindows()
