import cv2
import imutils

obraz = cv2.imread('../Downloads/Python2-opencv_basic_resizing/image.jpg')

if obraz is None:
    print("nie udało się wczytać obrazka :(")
else:
    nowy = imutils.resize(obraz, width=800)
    cv2.imwrite('../Downloads/Python2-opencv_basic_resizing/resized_output.jpg', nowy)
    cv2.imshow('większy obrazek', nowy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
