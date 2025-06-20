import cv2

def load_and_resize(path, size=(300, 300)):
    img = cv2.imread(path)
    return cv2.resize(img, size)

def main():
    img1 = load_and_resize('../Downloads/Python2-opencv_basic_bitwise/image1.jpg')
    img2 = load_and_resize('../Downloads/Python2-opencv_basic-bitwise/image2.jpg')

    xor_diff = cv2.bitwise_xor(img1, img2)

    cv2.imshow("Obrazek 1", img1)
    cv2.imshow("Obrazek 2", img2)
    cv2.imshow("Różnica XOR", xor_diff)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
