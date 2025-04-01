import cv2
import numpy as np

def task_10(image_path):
    image = cv2.imread(image_path)
    (b1, g1, r1) = image[50, 50]
    (b2, g2, r2) = image[200, 200]
    print(f"Difference in RGB: R:{abs(r1-r2)}, G:{abs(g1-g2)}, B:{abs(b1-b2)}")
