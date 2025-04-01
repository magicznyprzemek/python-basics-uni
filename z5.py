import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")
cX, cY = canvas.shape[1] // 2, canvas.shape[0] // 2
for size in range(20, 150, 20):
    cv2.rectangle(canvas, (cX-size, cY-size), (cX+size, cY+size), (255, 255, 255), 1)
cv2.imshow("Squares", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()