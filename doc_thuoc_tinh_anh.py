import cv2
import numpy as np
img=cv2.imread("anh1.jpg",1)
print (img.shape) #(in ra gia tri buc anh tuong ung voi [cao,rong,kenhmau])
print (img.size)  # kich thuoc cua 1 buc anh
print (img.dtype) # biet duoc buc anh bao nhieu byte

