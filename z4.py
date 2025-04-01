import cv2
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")
cX, cY = canvas.shape[1] // 2, canvas.shape[0] // 2
cv2.rectangle(canvas, (cX-50, cY-50), (cX+50, cY+50), (255, 255, 255), 2)
cv2.circle(canvas, (cX, cY), 30, (255, 255, 255), 2)
cv2.imshow("Complex Shape", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()