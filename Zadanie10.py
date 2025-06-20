import cv2
import numpy as np

img = cv2.imread('../Downloads/Python2-opencv_basic_rotation/image.jpg')

if img is None:
    print("nie wczytano obrazka")
else:
    h, w = img.shape[:2]
    c = (w // 2, h // 2)

    for kat in range(0, 360, 15):
        m = cv2.getRotationMatrix2D(c, kat, 1)
        rot = cv2.warpAffine(img, m, (w, h))

        cv2.imshow(f'obrot {kat}', rot)
        cv2.waitKey(500)

    cv2.destroyAllWindows()
