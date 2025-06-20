import cv2
import numpy as np

img = cv2.imread('../Downloads/Python2-opencv_basic_rotation/image.jpg')

if img is None:
    print("nie wczytano obrazka")
else:
    h, w = img.shape[:2]
    c = (w // 2, h // 2)

    m1 = cv2.getRotationMatrix2D(c, 30, 1)
    rot30 = cv2.warpAffine(img, m1, (w, h))

    m2 = cv2.getRotationMatrix2D(c, 30, 1)
    rot60 = cv2.warpAffine(rot30, m2, (w, h))

    m3 = cv2.getRotationMatrix2D(c, 30, 1)
    rot90 = cv2.warpAffine(rot60, m3, (w, h))

    m4 = cv2.getRotationMatrix2D(c, 90, 1)
    rot90once = cv2.warpAffine(img, m4, (w, h))

    cv2.imshow('3x30', rot90)
    cv2.imshow('raz90', rot90once)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
