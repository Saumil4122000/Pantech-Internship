import cv2
img=cv2.imread("C:/Users/BAPS/OneDrive/Desktop/PanTech/Lec-3(Open Vision)/python_img.jpg")
grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("C:/Users/BAPS/OneDrive/Desktop/PanTech/Lec-3(Open Vision)/python_img_gray.jpg",grayImg)
cv2.imshow("Original Image",img)
cv2.imshow("Gray Scale Image",grayImg)
cv2.waitKey(0)
cv2.destroyAllWindows()