import cv2
import numpy as np

def wczytaj_obraz(sciezka):
    obraz = cv2.imread(sciezka)
    if obraz is None:
        print("wip: nie udało się załadować obrazka :(")
    return obraz

def przesun_obraz(obraz, tx, ty):
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    return cv2.warpAffine(obraz, M, (obraz.shape[1], obraz.shape[0]))

def wyswietl_obraz(obraz):
    cv2.imshow('przesunięty obrazek (work in progress)', obraz)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    obraz = wczytaj_obraz('../Downloads/Python2-opencv_basic_transforming/image.jpg')
    if obraz is not None:
        try:
            tx = int(input("podaj przesunięcie w poziomie (tx): "))
            ty = int(input("podaj przesunięcie w pionie (ty): "))
        except ValueError:
            print("wip: coś poszło nie tak z przesunięciem :(")
        else:
            obraz_przesuniety = przesun_obraz(obraz, tx, ty)
            wyswietl_obraz(obraz_przesuniety)
