import cv2
img=cv2.imread("C:/Users/BAPS/OneDrive/Desktop/PanTech/Lec-4/assignment_img.jpg")

grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
threshImg=cv2.threshold(grayImg,120,255,cv2.THRESH_BINARY)[1]
# thresold returns 2 values and our thresold image is at 2 and to get that image we use index 1
# _,threshImg=cv2.threshold(grayImg,120,255,cv2.THRESH_BINARY)
# other declaration
cv2.imwrite("C:/Users/BAPS/OneDrive/Desktop/PanTech/Lec-4/assignment_img_gray.jpg",grayImg)
cv2.imwrite("C:/Users/BAPS/OneDrive/Desktop/PanTech/Lec-4/assignment_img_thresh.jpg",threshImg)


# rect_img=cv2.imread("C:/Users/BAPS/OneDrive/Desktop/PanTech/Lec-4/image_gray.jpg")
# cv2.rectangle(rect_img,(0,0),(300,400),(0,255,0))
# cv2.imwrite("C:/Users/BAPS/OneDrive/Desktop/PanTech/Lec-4/image_rectangle.jpg",rect_img)

# For ractangle


