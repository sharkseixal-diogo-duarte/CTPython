import numpy as np
import cv2

webcam = cv2.VideoCapture(0)

azul_claro = np.array([130,255 ,255])
azul_escuro = np.array([90,150 ,50])

while True:
    ret, frame = webcam.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, azul_escuro, azul_claro)

    result = cv2.bitwise_and(frame, frame, mask=mask)


    cv2.imshow("Azul Detectado", result)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
