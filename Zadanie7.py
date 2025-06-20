import cv2
import imutils
import numpy as np

img = cv2.imread('../Downloads/Python2-opencv_basic_rotation/image.jpg')

if img is None:
    print("nie wczytano obrazka")
else:
    h, w = img.shape[:2]
    c = (w // 2, h // 2)
    m = cv2.getRotationMatrix2D(c, 60, 1)
    rot1 = cv2.warpAffine(img, m, (w, h))
    rot2 = imutils.rotate(img, 60)

    cv2.imshow('obrot 60 warp', rot1)
    cv2.imshow('obrot 60 imutils', rot2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
