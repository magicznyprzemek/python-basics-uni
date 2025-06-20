import cv2
import numpy as np

def load_image(path):
    image = cv2.imread(path)
    if image is None:
        print("Nie udało się wczytać obrazka :(")
        exit()
    return image

def main():
    image = load_image("obrazek4.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    brightened_image = cv2.add(gray, 50)
    _, thresh_original = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    _, thresh_brightened = cv2.threshold(brightened_image, 100, 255, cv2.THRESH_BINARY)

    cv2.imshow("Oryginał po progowaniu", thresh_original)
    cv2.imshow("Rozjaśniony po progowaniu", thresh_brightened)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
