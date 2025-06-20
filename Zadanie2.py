import cv2

def load_image(path):
    image = cv2.imread(path)
    if image is None:
        print("Nie udało się wczytać obrazka :(")
        exit()
    return image

def main():
    image = load_image("obrazek2.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh_no_blur = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    _, thresh_with_blur = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)

    cv2.imshow("Szary obrazek", gray)
    cv2.imshow("Obrazek po rozmyciu", blurred)
    cv2.imshow("Progowanie bez rozmycia", thresh_no_blur)
    cv2.imshow("Progowanie po rozmyciu", thresh_with_blur)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
