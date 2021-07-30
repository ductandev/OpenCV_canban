import numpy as np
import cv2

cap = cv2.VideoCapture(0)		#('video.mp4')

while(True):
    ret, frame = cap.read()
   # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #video mau xam
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break

#cv2.imwrite('cameralaptop.mp4', frame)
cap.release()
#cv2.waitKey(0)
cv2.destroyAllWindows()
