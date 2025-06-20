import cv2
import numpy as np

obraz = cv2.imread('../Downloads/Python2-opencv_basic_resizing/image.jpg')

if obraz is None:
    print("nie udało się wczytać obrazka :(")
else:
    skala = 3
    metody = {
        'nearest': cv2.INTER_NEAREST,
        'linear': cv2.INTER_LINEAR,
        'cubic': cv2.INTER_CUBIC,
        'lanczos4': cv2.INTER_LANCZOS4
    }

    for nazwa, metoda in metody.items():
        wiekszy = cv2.resize(obraz, None, fx=skala, fy=skala, interpolation=metoda)
        cv2.imshow(nazwa, wiekszy)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
