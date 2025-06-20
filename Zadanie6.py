import cv2
import imutils

obraz = cv2.imread('../Downloads/Python2-opencv_basic_resizing/image.jpg')

if obraz is None:
    print("nie udało się wczytać obrazka :(")
else:
    wysokosc = 400
    przeskalowany = imutils.resize(obraz, height=wysokosc)
    cv2.imshow('przeskalowany obrazek', przeskalowany)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
