import cv2
import numpy as np

def task_4(image_path, x, y):
    image = cv2.imread(image_path)
    (h, w) = image.shape[:2]
    if 0 <= x < w and 0 <= y < h:
        image[y, x] = (0, 0, 0)
        cv2.imshow("Modified Pixel", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()