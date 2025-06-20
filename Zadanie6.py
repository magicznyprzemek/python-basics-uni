import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_image(path):
    image = cv2.imread(path)
    if image is None:
        print("Nie udało się wczytać obrazka :(")
        exit()
    return image

def main():
    image = load_image("obrazek6.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    otsu_threshold, otsu_thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    plt.figure(figsize=(10, 5))
    plt.plot(hist)
    plt.title('Histogram szarości')
    plt.xlabel('Jasność')
    plt.ylabel('Ile tego jest')
    plt.axvline(x=otsu_threshold, color='r', linestyle='--', label=f'Otsu próg = {otsu_threshold}')
    plt.legend(loc='upper right')
    plt.show()

    cv2.imshow("Po progowaniu Otsu", otsu_thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
