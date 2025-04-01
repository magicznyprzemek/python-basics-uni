import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")
blue = (255, 0, 0)
cX, cY = canvas.shape[1] // 2, canvas.shape[0] // 2
cv2.line(canvas, (cX, cY), (canvas.shape[1]-1, canvas.shape[0]-1), blue, 2)
cv2.imshow("Line", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()