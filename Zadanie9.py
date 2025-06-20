import cv2
import numpy as np

img = cv2.imread('../Downloads/Python2-opencv_basic_rotation/image.jpg')

if img is None:
    print("nie wczytano obrazka")
else:
    h, w = img.shape[:2]
    c = (w // 2, h // 2)

    m = cv2.getRotationMatrix2D(c, 75, 1)
    rot = cv2.warpAffine(img, m, (w, h))

    cv2.imwrite('../Downloads/Python2-opencv_basic_rotation/rotated_output.jpg', rot)
    print("zapisano jako rotated_output.jpg")

    cv2.imshow('obrot 75', rot)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
