import cv2
import numpy as np

cam = cv2.VideoCapture(0)
img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("anhtest", frame)
    k = cv2.waitKey(1)

    if k%256 == 27: # nhan Esc de thoat chuong trinh
        print("Escape hit, closing...")
        break

    elif k%256 == 32: # nhan space de chup hinh
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()
cv2.destroyAllWindows()
