import cv2

obraz = cv2.imread('../Downloads/Python2-opencv_basic_numpy_slicing/image.jpg')
wys, szer, _ = obraz.shape
wys_cz = wys // 3
szer_cz = szer // 3

for i in range(3):
    for j in range(3):
        cz = obraz[i*wys_cz:(i+1)*wys_cz, j*szer_cz:(j+1)*szer_cz]
        cv2.imshow(f"Kawałek nr {i*3+j+1}", cz)

cv2.waitKey(0)
cv2.destroyAllWindows()
