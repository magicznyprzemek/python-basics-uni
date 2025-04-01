import cv2
import numpy as np

def task_9(image_path):
    image = cv2.imread(image_path)
    image[50:100, 50:100] = (255, 255, 255)
    cv2.imshow("Modified Area", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()