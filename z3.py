import cv2
import numpy as np

def task_3(image_path):
    image = cv2.imread(image_path)
    (h, w) = image.shape[:2]
    (b, g, r) = image[h//2, w//2]
    print(f"Pixel at center ({w//2}, {h//2}) - Red: {r}, Green: {g}, Blue: {b}")
