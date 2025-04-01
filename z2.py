import cv2
import numpy as np

def task_2(image_path):
    image = cv2.imread(image_path)
    (h, w) = image.shape[:2]
    image[h-1, w-1] = (0, 0, 255)
    cv2.imshow("Modified Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()