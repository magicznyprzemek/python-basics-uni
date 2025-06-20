import cv2

obraz = cv2.imread('../Downloads/Python2-opencv_basic_resizing/image.jpg')

if obraz is None:
    print("nie udało się wczytać obrazka :(")
else:
    zmniejszony = cv2.resize(obraz, (obraz.shape[1] // 2, obraz.shape[0] // 2))
    cv2.imshow('mniejszy obrazek', zmniejszony)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
