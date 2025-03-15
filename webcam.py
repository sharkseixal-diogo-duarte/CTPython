import cv2
import numpy
import numpy as np

capt = cv2.VideoCapture(0)


while True:
    ret, frame = capt.read()
    width = int(capt.get(3))
    height = int(capt.get(4))
    image = np.zeros(frame.shapes, np.uint8)
    small_frame = cv2.resize(frame / 0.5)
    rotate = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow('webcam', small_frame)
    if cv2.waitKey(1) == ord('q'):
        break


capt.release()
cv2.destroyAllWindows()
