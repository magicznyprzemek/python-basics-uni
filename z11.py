import cv2
import numpy as np

def task_11(image_path):
    image = cv2.imread(image_path)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
    print(f"Brightest pixel at {maxLoc} with intensity {maxVal}")
