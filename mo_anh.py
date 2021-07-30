import numpy as np
import cv2
#mo file anh
img = cv2.imread('thuysinh.jpg',1)
#ke line anh
img = cv2.line(img, (0,0), (400,300), (0,0,255), 5)
#hien thi hinh anh
cv2.imshow('image', img)
#luu anh
cv2.imwrite('abc',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
