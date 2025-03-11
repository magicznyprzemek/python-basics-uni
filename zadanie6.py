import cv2

path = "test.jpg"
color = cv2.imread(path)
cv2.namedWindow("scalling", cv2.WINDOW_NORMAL)
cv2.imshow("scalling", color)
cv2.waitKey(0)
cv2.destroyAllWindows()