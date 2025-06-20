import cv2

obraz = cv2.imread('../Downloads/Python2-opencv_basic_numpy_slicing/image.jpg')

if obraz is None:
    print("Ej, nie znalazłem obrazka!")
    exit()

wysokosc = obraz.shape[0]
dol = obraz[wysokosc//2:, :]
cv2.imshow('Dół fotki', dol)
cv2.waitKey(0)
cv2.destroyAllWindows()
