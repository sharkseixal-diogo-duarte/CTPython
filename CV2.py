import cv2

img = cv2.imread("assets/imagem1.jpg")
img_resized = cv2.resize(img, (400,400))
img_rotate = cv2.rotate(img_resized, cv2.ROTATE_90_CLOCKWISE)
img_grayscale = img = cv2.imread("assets/imagem1.jpg", 0)
# salvar a imagem
cv2.imwrite("assets/image_grayscale.jpg", img_grayscale)
# criar a janela
cv2.imshow("aula1 -Read, Resize and Rotate Image", img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()