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

    # Preencher a image com a frame redimensionada
    image[:height // 2, :width // 2] = small_frame
    image[height // 2:, :width // 2] = small_frame
    image[:height // 2, width // 2:] = small_frame
    image[height // 2:, width // 2:] = small_frame

    # Preencher a image com a frame redimensionada c/ rotações das small_frame's
    #image[:height // 2, :width // 2] = small_frame # small frame "normal"
    #stretched_frame = cv2.resize(small_frame, (240, 320))
    #image[height // 2:, :width // 2] = cv2.rotate(stretched_frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    #image[:height // 2, width // 2:] = cv2.rotate(stretched_frame, cv2.ROTATE_90_CLOCKWISE)
    #image[height // 2:, width // 2:] = cv2.rotate(small_frame, cv2.ROTATE_180)

    #img = cv2.line(frame, (0,0), (width, height), (255,0,0), 10)
    #img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)
    #img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)
    #img = cv2.circle(img,(320, 240), 60, (0, 0, 255), -1)

    image[:height // 2, :width // 2] = cv2.rectangle(small_frame, (0, 0), (320, 240), (0, 0, 255), 5)
    image[height // 2:, :width // 2] = small_frame
    image[:height // 2, width // 2:] = cv2.circle(small_frame,(160, 120), 60, (255, 0, 0), -1)
    image[height // 2:, width // 2:] = small_frame


    cv2.imshow('desenho na webcam', image)

    if cv2.waitKey(1) == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
