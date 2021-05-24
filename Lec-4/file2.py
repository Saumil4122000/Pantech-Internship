import cv2
img=cv2.imread("Lec-4\assignment_img.jpg")
gaussianBlurImg=cv2.GaussianBlur(img,(21,21),0)
cv2.imwrite("Lec-4\gaussian_blur_img.jpg",gaussianBlurImg)