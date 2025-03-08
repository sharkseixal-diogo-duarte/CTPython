import cv2
import random

img = cv2.imread("assets/imagem1.jpg")
img = cv2.resize(img, (400,400))

bocadinho = img[60:90, 245:275]
img[360:390, 360:390] = bocadinho

for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255),
                     random.randint(0, 255),
                     random.randint(0, 255)]
cv2.imshow("assets/imagem1.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
