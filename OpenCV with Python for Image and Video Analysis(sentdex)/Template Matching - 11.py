import cv2
import numpy as np

img_bgr = cv2.imread('opencv-template-matching-python-tutorial.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread('opencv-template-for-matching.jpg', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(template, )