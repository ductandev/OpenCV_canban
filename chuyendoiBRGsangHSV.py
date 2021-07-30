import cv2
import numpy as np
img = np.uint8([[[232,162,0]]])	# tao bo loc de loc anh (B, R G)

#hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#print (hsv_img)

img2=cv2.imread('aaa.png',1)
hsv_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
hsv_img2 = cv2.resize(hsv_img2,(600,450))
ball=img2[280:340,330:390]
cv2.imshow('nhandangmautheokhonggianHSV',ball)
cv2.waitKey(0)
