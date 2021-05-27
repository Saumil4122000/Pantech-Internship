# It only detect the movement in north direction
import cv2
import imutils
cascade_src='Lec-18\cars.xml'
car_cascade=cv2.CascadeClassifier(cascade_src)
# Load classifier
cam=cv2.VideoCapture(0)

while True:
    detected=0
    _,img=cam.read()
    # Read from camera
    img=imutils.resize(img,width=300)
    # Resize the frame
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Color image to grayImage
    cars=car_cascade.detectMultiScale(gray,1.1,1)
    # Coordinates of vegicle in frame
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("Frame",img)
    b=str(len(cars))
    # detect number of cars
    a=int(b)
    detected=a
    n=detected
    print("----------------------------------------------------------------")
    print("North: %d"%(n))
    if(n >=2):
        # If more then 2 cars detected then show the traffic
        print("North more traffic")
    else:
        print("No traffic")
    if cv2.waitKey(33)==27:
        break
cam.release()
cv2.destroyAllWindows()


