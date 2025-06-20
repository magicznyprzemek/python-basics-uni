import cv2

obraz = cv2.imread('../Downloads/Python2-opencv_basic_numpy_slicing/image.jpg')
wys, szer, _ = obraz.shape
startX, endX, startY, endY = 0, 100, 0, 100
przes = 10

while True:
    roi = obraz[startY:endY, startX:endX]
    cv2.imshow('Kawałek do przesuwania', roi)
    key = cv2.waitKey(0) & 0xFF
    if key == ord('d'):
        startX += przes
        endX += przes
    elif key == ord('a'):
        startX -= przes
        endX -= przes
    elif key == ord('q'):
        break

cv2.destroyAllWindows()
