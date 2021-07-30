import cv2

img = cv2.imread('./chupanh/anh_0.png',0)		#chọn đường dẫn ảnh để đọc
img2 = cv2.Canny(img,50,200)		#hàm đọc biên ảnh (đường dẫn ảnh, độ sáng ngưỡng ảnh muốn đọc trong khoản từ nhỏ nhất là  50 đến lớn nhất là 200)
cv2.imshow('bienanh',img2)		# hiển thị ảnh
cv2.waitKey(0)				# tạm dừng cho đến khi tắt 
cv2.destroyAllWindows()			# giải phóng bộ nhớ

