import cv2
import numpy as np

def create_triangle(size):
    img = np.zeros((size, size), dtype="uint8")
    pts = np.array([[size//2, size//6], [size//6, 5*size//6], [5*size//6, 5*size//6]], np.int32).reshape((-1, 1, 2))
    cv2.fillPoly(img, [pts], 255)
    return img

def create_circle(size):
    img = np.zeros((size, size), dtype="uint8")
    cv2.circle(img, (size//2, size//2), size//3, 255, -1)
    return img

def main():
    size = 300
    triangle = create_triangle(size)
    circle = create_circle(size)

    bitwise_and = cv2.bitwise_and(triangle, circle)
    bitwise_or = cv2.bitwise_or(triangle, circle)
    bitwise_xor = cv2.bitwise_xor(triangle, circle)
    bitwise_not = cv2.bitwise_not(triangle)

    cv2.imshow("Trójkąt", triangle)
    cv2.imshow("Kółko", circle)
    cv2.imshow("I", bitwise_and)
    cv2.imshow("LUB", bitwise_or)
    cv2.imshow("XOR", bitwise_xor)
    cv2.imshow("NIE (Trójkąt)", bitwise_not)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
