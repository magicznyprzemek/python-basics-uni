import cv2

path = "test.jpg"
gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
if gray is not None:
    print(f'kanaly: {len(gray.shape)}')