import cv2
                              
(width,height)=(130,100)
alg="C:/Users/BAPS/OneDrive/Desktop/PanTech/Lec-5/haarcascade_frontalface_default.xml"
haar_cascade=cv2.CascadeClassifier(alg)
cam=cv2.VideoCapture(0)
while True:
    _,img=cam.read()
    text="No person Detected"
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=haar_cascade.detectMultiScale(grayImg,1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        text="Person Detected"
    print(text)
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),5)
    cv2.imshow("Person Detected",img)
    key=cv2.waitKey(10)
     
    if key==27:
        break
cam.release()
cv2.destroyAllWindows()