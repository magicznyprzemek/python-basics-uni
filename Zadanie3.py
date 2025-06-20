import cv2
import numpy as np

def main():
    obraz = cv2.imread('../Downloads/Python2-opencv_basic_masking/flowers.jpg')
    if obraz is None:
        print("Ups, nie mogę znaleźć obrazka!")
        return

    hsv = cv2.cvtColor(obraz, cv2.COLOR_BGR2HSV)
    dolny_zakres = np.array([35, 50, 50])
    gorny_zakres = np.array([85, 255, 255])

    maska = cv2.inRange(hsv, dolny_zakres, gorny_zakres)
    wynik = cv2.bitwise_and(obraz, obraz, mask=maska)

    cv2.imshow('Obrazek', obraz)
    cv2.imshow('Maska', maska)
    cv2.imshow('Wyciągnięty kolor', wynik)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
