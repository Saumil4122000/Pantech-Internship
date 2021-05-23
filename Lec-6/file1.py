import imutils
import cv2

redLower=(136,87,111)
#           H, S, V
redUpper=(180,255,255)
# For red color detection we have selected  color code

camera=cv2.VideoCapture(0)

while True:
    _,frame=camera.read()
    frame=imutils.resize(frame,width=600)
    blurred=cv2.GaussianBlur(frame,(11,11),0)
    hsv=cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)
    
    mask=cv2.inRange(hsv,redLower,redUpper)
    #It will mask the red color around the red object

    mask=cv2.erode(mask,None,iterations=2)
    # Removes holes from images

    mask=cv2.dilate(mask,None,iterations=2)

    cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    # Connect two neighbourhood dots and make border around it

    center=None
    if len(cnts)>0:
        c=max(cnts,key=cv2.contourArea)
        # Find the max contor area

        ((x,y),radius)=cv2.minEnclosingCircle(c)
        # Draw the circle which returns the center point and radius
        M=cv2.moments(c)
         # find the center of complete object

        center =(int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))

        if radius > 10:
            cv2.circle(frame,(int(x),int(y)),int(radius),(0,255,255),2)#thickness
            cv2.circle(frame,center,5,(0,0,255),-1)
            if radius>250:
                print("Stop")
            else:
                if(center[0]<150):
                    # x co-ordinates of center 
                    print("Left")
                elif(center[0]>450):
                    print("Right")
                elif(radius<250):
                    print("Front")
                else:
                    print("Stop")

        cv2.imshow("Frame",frame)
        key=cv2.waitKey(1)& 0xFF
        if key==ord("q"):
            break
camera.release()
cv2.destroyAllWindows()