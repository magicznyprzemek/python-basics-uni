import cv2
import imutils

img = cv2.imread('../Downloads/Python2-opencv_basic_rotation/image.jpg')

if img is None:
    print("nie wczytano obrazka")
else:
    rot = imutils.rotate_bound(img, -33)

    cv2.imshow('obrot -33 bez ciecia', rot)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
