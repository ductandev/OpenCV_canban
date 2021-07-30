import cv2
import numpy as np

img1 = cv2.imread('digits.png', 1)
img2 = cv2.imread('anh1.jpg', 1)

img1 = img1[300:500, 400:800]
img2 = img2[300:500, 400:800]

img3 = cv2.add(img1,img2)
cv2.imwrite('anhghep.jpg', img3)
cv2.imshow('anhghep.jpg', img3)
cv2.waitKey(0)
