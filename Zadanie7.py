import cv2
import numpy as np

def load_image(path):
    image = cv2.imread(path)
    if image is None:
        print("Nie udało się wczytać obrazka :(")
        exit()
    return image

def main():
    image = load_image("obrazek7.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, otsu_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    masked_image = cv2.bitwise_and(image, image, mask=otsu_thresh)

    cv2.imshow("Oryginał", image)
    cv2.imshow("Maska Otsu", otsu_thresh)
    cv2.imshow("Wycięty obiekt", masked_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
