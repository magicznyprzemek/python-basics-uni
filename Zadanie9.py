import cv2
import numpy as np

obraz = cv2.imread('../Downloads/Python2-opencv_basic_resizing/image.jpg')

if obraz is None:
    print("nie udało się wczytać obrazka :(")
else:
    for skala in np.arange(1.0, 3.2, 0.2):
        szer = int(obraz.shape[1] * skala)
        wys = int(obraz.shape[0] * skala)
        zmieniony = cv2.resize(obraz, (szer, wys), interpolation=cv2.INTER_LINEAR)
        cv2.imshow('zmiana rozmiaru', zmieniony)
        cv2.waitKey(500)
    cv2.destroyAllWindows()
