import cv2

obraz = cv2.imread('../Downloads/Python2-opencv_basic_numpy_slicing/image.jpg')

if obraz is None:
    print("Ej, nie znalazłem obrazka!")
    exit()

roi = obraz[0:100, 0:100]
cv2.imshow('Patrz na to!', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
