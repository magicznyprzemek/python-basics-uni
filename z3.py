import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")
cv2.circle(canvas, (40, 40), 40, (255, 0, 0), -1)
cv2.circle(canvas, (canvas.shape[1]//2, canvas.shape[0]//2), 60, (0, 0, 255), -1)
cv2.imshow("Circles", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()