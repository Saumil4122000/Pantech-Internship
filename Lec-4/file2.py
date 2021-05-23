import cv2
import imutils
img=cv2.imread("C:/Users/BAPS/OneDrive/Desktop/PanTech/Lec-4/assignment_img.jpg")
gaussianBlurImg=cv2.GaussianBlur(img,(21,21),0)
cv2.imwrite("C:/Users/BAPS/OneDrive/Desktop/PanTech/Lec-4/gaussian_blur_img.jpg",gaussianBlurImg)

