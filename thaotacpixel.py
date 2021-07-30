import cv2
import numpy as np

img = cv2.imread('abc.jpg', 1)
px = img[0][0];
print (px)

for i in range(100):
	img[i][i] = [1,1,1]
	img[i+2][i+2] = [1,1,1]

cv2.imshow('img', img)
cv2.waitKey(0)














#cv2.imwrite('dave1.jpg', img)
