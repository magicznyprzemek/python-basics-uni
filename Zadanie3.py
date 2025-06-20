import cv2
import numpy as np

def load_image(path):
    image = cv2.imread(path)
    if image is None:
        print("Nie udało się wczytać obrazka :(")
        exit()
    return image

def main():
    image = load_image("obrazek3.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh_with_blur = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3, 3), np.uint8)
    eroded_image = cv2.erode(thresh_with_blur, kernel, iterations=1)

    cv2.imshow("Przed erozją", thresh_with_blur)
    cv2.imshow("Po erozji", eroded_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
