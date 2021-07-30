import cv2
import numpy as np

cam = cv2.VideoCapture(0)
img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("anhtest", frame)
    k = cv2.waitKey(1)

    if k%256 == 27: # nhan Esc de thoat chuong trinh
        print("closing...")
        break

    elif k%256 == 32: # nhan space de chup hinh
        cv2.imwrite("anh_%d.png"%img_counter,frame)
        print ("da chup %d anh"%img_counter)
        img_counter += 1

cam.release()
cv2.destroyAllWindows()


