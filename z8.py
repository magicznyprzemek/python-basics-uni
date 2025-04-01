import cv2
import numpy as np

def task_8(image_path):
    image = cv2.imread(image_path)
    image[100, :] = (0, 255, 0)
    cv2.imshow("Modified Row", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()