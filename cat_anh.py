import cv2
import numpy as np

img = cv2.imread('thuysinh.jpg', 1)
img = img[300:500, 500:700]
cv2.imwrite('catanh.jpg', img)
cv2.imshow('image', img)
cv2.waitKey(0)
