import cv2
import numpy as np

def load_image(path):
    image = cv2.imread(path)
    if image is None:
        print("Nie udało się wczytać obrazka :(")
        exit()
    return image

def main():
    image = load_image("obrazek5.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    brightened_image = cv2.add(gray, 50)
    _, otsu_thresh = cv2.threshold(brightened_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    cv2.imshow("Rozjaśniony + Otsu", otsu_thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
