import numpy as np
import cv2

webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read()
    width = int(webcam.get(3))
    height = int(webcam.get(4))

    # Criar uma imagem do tamanho da frame da webcam e por todos os pixeis a "zero"
    image = np.zeros(frame.shape, np.uint8)

    # Resize the frame a metade no eixo de x e y
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    image[:height // 2, :width // 2] = small_frame # small frame "normal"
    stretched_frame = cv2.resize(small_frame, (240, 320))
    image[height // 2:, :width // 2] = cv2.rotate(stretched_frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    image[:height // 2, width // 2:] = cv2.rotate(stretched_frame, cv2.ROTATE_90_CLOCKWISE)
    image[height // 2:, width // 2:] = cv2.rotate(small_frame, cv2.ROTATE_180)

    image_2 = cv2.rectangle(image,(0, 0),(320, 240),(0, 0, 255),5)
    image_2 = cv2.line(image_2, (640, 0),(0,480) , (0, 255, 0), 5)
    image_2 = cv2.line(image_2, (320,0), (640,240), (0, 255, 0), 5)
    image_2 = cv2.circle(image_2,(160, 360),45,(255, 0, 0),-1)
    image_2 = cv2.rectangle(image_2, (450, 330), (510, 390), (0, 0, 255), -1)
    image_2 = cv2.putText(image_2, "sharkcoders", (50,50), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0), 1, cv2.LINE_4)

    cv2.imshow('desenho na webcam', image_2)

    if cv2.waitKey(1) == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
