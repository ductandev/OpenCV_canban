import cv2 

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('aa.mp4', fourcc, 20.0, (640,480))
print(cap.isOpened()) #in ra do phan giai (dai x rong)

while (cap.isOpened()):
	ret, frame = cap.read()
	if ret == True:
		print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # do dai khung hinh
		print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # do rong khung hinh

		out.write(frame)

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('frame',gray)

		if cv2.waitKey(1) & 0xFF == ord('q'):
		   break
	else:
	   break
cap.release()
out.release()
cv2.destroyAllWindows()
