import cv2

path = "test.jpg"
color = cv2.imread(path)
gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
cv2.imshow("kolor", color)
cv2.imshow("szary", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()