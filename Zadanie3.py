import cv2

obraz = cv2.imread('../Downloads/Python2-opencv_basic_resizing/image.jpg')

if obraz is None:
    print("nie udało się wczytać obrazka :(")
else:
    nowy_rozmiar = (200, 300)
    zmieniony = cv2.resize(obraz, nowy_rozmiar)
    cv2.imshow('obrazek 200x300', zmieniony)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
