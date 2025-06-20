import cv2

obraz = cv2.imread('../Downloads/Python2-opencv_basic_numpy_slicing/image.jpg')

if obraz is None:
    print("Ej, nie znalazłem obrazka!")
    exit()

startX = int(input("Podaj X skąd tniesz: "))
endX = int(input("Podaj X dokąd tniesz: "))
startY = int(input("Podaj Y skąd tniesz: "))
endY = int(input("Podaj Y dokąd tniesz: "))

roi = obraz[startY:endY, startX:endX]
cv2.imshow("Wycięty kawałek fotki", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
