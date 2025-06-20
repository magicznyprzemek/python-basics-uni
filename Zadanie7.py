import cv2

obraz = cv2.imread('../Downloads/Python2-opencv_basic_resizing/image.jpg')

if obraz is None:
    print("nie udało się wczytać obrazka :(")
else:
    mniejszy = cv2.resize(obraz, (obraz.shape[1] // 5, obraz.shape[0] // 5), interpolation=cv2.INTER_AREA)
    cv2.imshow('mniejszy obrazek (area)', mniejszy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
