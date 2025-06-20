import cv2
import imutils

img = cv2.imread('../Downloads/Python2-opencv_basic_rotation/image.jpg')

if img is None:
    print("nie wczytano obrazka")
else:
    rot = imutils.rotate(img, 180)

    cv2.imshow('obrot 180', rot)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
