import cv2

path = "test.jpg"
color = cv2.imread(path)
if color is not None:
    print(f'kanaly: {color.shape[2]}')