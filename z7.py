import cv2
import numpy as np

def task_7(image_path):
    image = cv2.imread(image_path)
    (h, w) = image.shape[:2]
    part = image[h//3:h//3*2, w//3:w//3*2]
    cv2.imshow("Cropped Center", part)
    cv2.waitKey(0)
    cv2.destroyAllWindows()