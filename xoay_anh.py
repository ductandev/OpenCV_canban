import cv2
import numpy as np

img = cv2.imread('thuysinh.jpg',1)
height, width = img.shape[:2]
rotation_maxtrix = cv2.getRotationMatrix2D((width/2,height/2), 90, .5)
rotated_image = cv2.warpAffine(img, rotation_maxtrix, (width,height))

frame=cv2.resize(rotated_image,(300,250))

cv2.imshow('1 image', rotated_image)
cv2.imshow('2 image', rotation_maxtrix)
cv2.imshow('3 image', frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
