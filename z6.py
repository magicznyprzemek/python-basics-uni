import cv2
import numpy as np

def task_6(image_path):
    image = cv2.imread(image_path)
    (h, w) = image.shape[:2]
    d_cX, d_cY = w // 2, h // 2
    image[d_cY-50:d_cY+50, d_cX-50:d_cX+50] = (0, 0, 255)
    cv2.imshow("Center Square", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()