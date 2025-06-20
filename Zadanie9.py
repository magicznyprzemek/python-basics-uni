import cv2

obraz = cv2.imread('../Downloads/Python2-opencv_basic_numpy_slicing/image.jpg')
kawa = obraz[0:300, 0:300]
cv2.imwrite('../Downloads/Python2-opencv_basic_numpy_slicing/cropped_image.jpg', kawa)
cv2.imshow('Przycięty kawałek fotki', kawa)
cv2.waitKey(0)
cv2.destroyAllWindows()
