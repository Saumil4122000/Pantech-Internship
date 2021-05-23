import cv2
img=cv2.imread("C:/Users/BAPS/OneDrive/Desktop/PanTech/Lec-3(Open Vision)/img_assignment.jpg")
cv2.imshow("Original Image",img)


print(img.size)
print(img.shape)
print(img.dtype)

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imwrite("C:/Users/BAPS/OneDrive/Desktop/PanTech/Lec-3(Open Vision)/img_assignment.jpg/gray_img.jpg",img)


cv2.imshow("Gray Image",img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()