import cv2
import numpy as np
img = np.uint8([[[232,162,0]]])

hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print (hsv_img)
img2=cv2.imread('aaa.png',1)
hsv_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

min_mau = np.array([97,255,232])
max_mau = np.array([100,255,232])
mask  = cv2.inRange(hsv_img2,min_mau,max_mau)
final = cv2.bitwise_and(img2,img2,mask=mask)

cv2.imshow("tach doi tuong mau", final)
cv2.waitKey(0)


