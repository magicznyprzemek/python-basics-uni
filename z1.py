import cv2
import numpy as np

def task_1(image_path):
    image = cv2.imread(image_path)
    (b, g, r) = image[0, 0]
    print(f"Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}")