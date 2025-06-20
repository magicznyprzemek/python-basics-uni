import cv2
import numpy as np

obraz = cv2.imread('../Downloads/Python2-opencv_basic_rotation/image.jpg')

if obraz is None:
    print("Nie udało się załadować obrazu!")
else:
    kąt = float(input("Podaj kąt obrotu: "))
    (wysokosc, szerokosc) = obraz.shape[:2]
    center = (szerokosc // 2, wysokosc // 2)
    M = cv2.getRotationMatrix2D(center, kąt, 1)
    obraz_obrocony = cv2.warpAffine(obraz, M, (szerokosc, wysokosc))

    cv2.imshow(f'Obraz po obrocie o {kąt} stopni', obraz_obrocony)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
