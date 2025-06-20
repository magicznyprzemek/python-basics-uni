import cv2
import numpy as np

def main():
    obraz = cv2.imread('../Downloads/Python2-opencv_basic_masking/face.jpg')
    if obraz is None:
        print("Ups, nie mogę znaleźć obrazka!")
        return

    maska = np.ones(obraz.shape[:2], dtype="uint8") * 255
    cv2.rectangle(maska, (100, 50), (300, 150), 0, -1)

    wynik = cv2.bitwise_and(obraz, obraz, mask=maska)

    cv2.imshow('Obrazek', obraz)
    cv2.imshow('Maska', maska)
    cv2.imshow('Zamaskowane oczy', wynik)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
