import cv2
import numpy as np
import pyautogui
import keyboard
test_area = (400, 200, 220, 150)

try:
    while True:
        if keyboard.is_pressed('q'):
            break

        screenshot = pyautogui.screenshot(region=test_area)
        gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

        obstacle_area = thresh[60:100, 150:180]
        obstacle_pixels = cv2.countNonZero(obstacle_area)

        print("Pixels detectados:", obstacle_pixels)

        if (50 < obstacle_pixels < 999) or (1000 < obstacle_pixels < 1190):
            pyautogui.press("space")

        cv2.imshow("Área de Detecção", thresh)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Interrompido pelo usuário.")
finally:
    cv2.destroyAllWindows()
