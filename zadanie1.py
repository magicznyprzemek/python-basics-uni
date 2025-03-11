import cv2

path = "test.jpg"
image = cv2.imread(path)
if image is None:
    print("brak")
else:
    cv2.imshow("ok", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()