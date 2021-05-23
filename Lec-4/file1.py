import cv2
import imutils
img=cv2.imread("C:/Users/BAPS/OneDrive/Desktop/PanTech/Lec-4/assignment_img.jpg")
resizeImg=imutils.resize(img,width=200)
cv2.imwrite("C:/Users/BAPS/OneDrive/Desktop/PanTech/Lec-4/resize_img.jpg",resizeImg)