import cv2
import numpy as np

canvas = np.zeros((400, 400, 3), dtype="uint8")
green = (0, 255, 0)
red = (0, 0, 255)
cv2.rectangle(canvas, (0, 0), (100, 50), green, -1)
cv2.rectangle(canvas, (300, 350), (399, 399), red, 3)
cv2.imshow("Rectangles", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()