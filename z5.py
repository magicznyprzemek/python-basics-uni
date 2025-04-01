import cv2
import numpy as np

def task_5(image_path):
    image = cv2.imread(image_path)
    (h, w) = image.shape[:2]
    image[:h//2, :w//2] = (255, 0, 0)
    cv2.imshow("Colored Quarter", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()