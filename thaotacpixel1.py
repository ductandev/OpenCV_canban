import cv2
import numpy as np

img = cv2.imread('abc.jpg', 1)
px = img[0][0];
print (px)

for i in range(200):
	for j in range(200):
		if (img[i,j,0]> 30):
		 	img[i,j] = 1;
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.imwrite('dave2.jpg', img);

