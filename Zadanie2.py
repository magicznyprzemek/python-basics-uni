import cv2

obraz = cv2.imread('../Downloads/Python2-opencv_basic_resizing/image.jpg')

if obraz is None:
    print("nie udało się wczytać obrazka :(")
else:
    wiekszy = cv2.resize(obraz, (obraz.shape[1] * 2, obraz.shape[0] * 2), interpolation=cv2.INTER_LINEAR)
    cv2.imshow('większy obrazek', wiekszy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
