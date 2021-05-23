
import cv2
img=cv2.imread("C:/Users/BAPS/OneDrive/Desktop/PanTech/Lec-3(Open Vision)/python_img.jpg")
cv2.imshow("Python Logo",img)
cv2.imwrite("C:/Users/BAPS/OneDrive/Desktop/PanTech/Lec-3(Open Vision)/python_img_logo.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
