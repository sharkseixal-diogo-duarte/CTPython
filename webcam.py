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
    image[:height // 2, :width // 2] = small_frame # small frame "normal"
    stretched_frame = cv2.resize(small_frame, (240, 320))
    image[height // 2:, :width // 2] = cv2.rotate(stretched_frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    image[:height // 2, width // 2:] = cv2.rotate(stretched_frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    image[height // 2:, width // 2:] = cv2.rotate(small_frame, cv2.ROTATE_180)
    cv2.imshow('4 webcam', image)

    if cv2.waitKey(1) == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()
