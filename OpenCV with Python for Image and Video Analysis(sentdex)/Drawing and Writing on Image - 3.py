import cv2
import numpy as np

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0, 0), (140, 140), (255, 255, 255), 12)
cv2.rectangle(img, (100, 60), (200, 145), (0, 255, 0), 4)
cv2.circle(img, (100, 70), 53, (0, 0, 255), -1)

pts = np.array([[10, 5], [13, 6], [10, 20], [20, 22]])
cv2.polylines(img, [pts], True, (0, 255, 255), 4)

font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img, 'OpenCV Guys', (0, 120), font, 1, (170, 255, 255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()