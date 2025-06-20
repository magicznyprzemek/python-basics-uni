import cv2
import numpy as np

img = cv2.imread('../Downloads/Python2-opencv_basic_rotation/image.jpg')

if img is None:
    print("nie wczytano obrazka")
else:
    h, w = img.shape[:2]
    m = cv2.getRotationMatrix2D((0, 0), 30, 1)
    rot = cv2.warpAffine(img, m, (w, h))

    cv2.imshow('obrot 30 od lewego gornego', rot)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
