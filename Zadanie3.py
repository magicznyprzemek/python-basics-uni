import cv2

obraz = cv2.imread('../Downloads/Python2-opencv_basic_numpy_slicing/image.jpg')

if obraz is None:
    print("Ej, nie znalazłem obrazka!")
    exit()

szer = obraz.shape[1]
prawa = obraz[:, szer//2:]
cv2.imshow('Prawa część', prawa)
cv2.waitKey(0)
cv2.destroyAllWindows()
