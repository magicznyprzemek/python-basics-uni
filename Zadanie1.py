import cv2

def load_image(path):
    image = cv2.imread(path)
    if image is None:
        print("Nie udało się wczytać obrazka :(")
        exit()
    return image

def show_thresholds(gray):
    thresholds = [30, 100, 200]
    for t in thresholds:
        _, thresh = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)
        cv2.imshow(f"Obrazek po progowaniu T={t}", thresh)

def main():
    image = load_image("obrazek1.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Szary obrazek", gray)
    show_thresholds(gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
