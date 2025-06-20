import cv2
import numpy as np

obraz = cv2.imread('../Downloads/Python2-opencv_basic_resizing/image.jpg')

if obraz is None:
    print("nie udało się wczytać obrazka :(")
else:
    wiekszy_cubic = cv2.resize(obraz, (obraz.shape[1] * 4, obraz.shape[0] * 4), interpolation=cv2.INTER_CUBIC)
    wiekszy_lanczos = cv2.resize(obraz, (obraz.shape[1] * 4, obraz.shape[0] * 4), interpolation=cv2.INTER_LANCZOS4)
    cv2.imshow('większy (cubic)', wiekszy_cubic)
    cv2.imshow('większy (lanczos4)', wiekszy_lanczos)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
