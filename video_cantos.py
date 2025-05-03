import numpy as np
import cv2

webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    frame = cv2.resize(frame,(600,500))
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cantos = cv2.goodFeaturesToTrack(gray, 100, 0.5, 10)
    cantos = np.intp(cantos)
    for canto in cantos:
        x, y = canto.ravel()
        cv2.circle(frame,(x,y),3,(0, 0, 255),-1)

    cv2.imshow("cantos", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()


