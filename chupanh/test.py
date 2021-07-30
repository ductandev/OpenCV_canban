import numpy as np
import cv2

cap = cv2.VideoCapture(0) # ham su dung camera tu laptop
#ret,frame = cap.read() # tra ve mot khung don trong bien fame

while(True):
    ret, frame =cap.read()
    cv2.imshow('anhchup',frame) # hien thi hinh anh da chup
    if cv2.waitKey(1) & 0xFF == ord('y'): #save anh thi nhan 'Y'
        cv2.imwrite('a.png',frame)
        break

cap.release()
cv2.destroyAllWindows()
