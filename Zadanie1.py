import cv2
import numpy as np

def main():
    obraz = cv2.imread('../Downloads/Python2-opencv_basic_masking/face.jpg')
    if obraz is None:
        print("Ups, nie mogę znaleźć obrazka!")
        return

    maska = np.zeros(obraz.shape[:2], dtype="uint8")
    h, w = obraz.shape[:2]
    cv2.ellipse(maska, (w // 2, h // 2), (w // 4, h // 3), 0, 0, 360, 255, -1)

    wynik = cv2.bitwise_and(obraz, obraz, mask=maska)

    cv2.imshow('Obrazek', obraz)
    cv2.imshow('Maska', maska)
    cv2.imshow('Twarz po masce', wynik)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
