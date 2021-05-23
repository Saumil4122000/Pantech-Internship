# Reading frame from camera 
# Video Capture
import cv2
import time
vs=cv2.VideoCapture(0)
time.sleep(1)
# 0 for primary camera
while True:
    _,img=vs.read()
    cv2.imshow("Video Stream",img)
    key=cv2.waitKey(1) & 0xFF
    if key==ord("q"):
        break
vs.release()
cv2.destroyAllWindows()

# _,img=vs.read()
# cv2.imwrite("C:/Users/BAPS/OneDrive/Desktop/PanTech/Lec-4/click_image.jpg",img)
# vs.release()                                                                 