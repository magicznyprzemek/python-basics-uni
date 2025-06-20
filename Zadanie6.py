import cv2

obraz = cv2.imread('../Downloads/Python2-opencv_basic_numpy_slicing/image.jpg')
obraz[250:350, 250:350] = obraz[50:150, 50:150]
cv2.imshow("Podmianka kawałka", obraz)
cv2.waitKey(0)
cv2.destroyAllWindows()
