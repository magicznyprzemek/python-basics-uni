import cv2

obraz = cv2.imread('../Downloads/Python2-opencv_basic_numpy_slicing/image.jpg')
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(obraz, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

if len(faces) > 0:
    x, y, w, h = faces[0]
    twarz = obraz[y:y + h, x:x + w]
    cv2.imshow("Złapana twarz!", twarz)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No nie ma tu żadnej twarzy :(")
