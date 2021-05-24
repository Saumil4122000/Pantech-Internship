import cv2,numpy,os
# i have used numpy for computation of matrix from one point of our face
haar_file='Lec-7\haarcascade_frontalface_default.xml'
face_cascade=cv2.CascadeClassifier(haar_file)
datasets='Lec-7\dataset'
id=0
(images,labels,names)=([],[],{})

for(subdirs,dirs,files) in os.walk(datasets):
    # Iterate through dataset folder
    # move through different subdirectory
    for subdirs in dirs:
      
        names[id]=subdirs
        # assign name to directory according id
        subjectpath=os.path.join(datasets,subdirs)
        for filename in os.listdir(subjectpath):
            path=subjectpath+'/'+filename
            label=id
            # Loads the images into the images array
            images.append(cv2.imread(path,0))
            # Loads the labels into the label arrray
            labels.append(int(label))
            # print(labels)
        id+=1
(images,labels)=[numpy.array(lis) for lis in [images,labels]]
# print(images,labels)
# take images and label after place it into numpy array
(width,height)=(130,100)

model=cv2.face.LBPHFaceRecognizer_create()
# Face classifier
# model=cv2.face.FisherFaceRecognizer_create()
# 2nd classifier

model.train(images,labels)
# It will do training and processing of images and labels


webCam=cv2.VideoCapture(0)
cnt=0

#Face Detection Part
while True:
    _,img=webCam.read()
    # Converting Image to GrayImage
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(grayImg,1.3,4)
    for (x,y,w,h) in faces:
        # Create Rectangle
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

        face=grayImg[y:y+h,x:x+w]
        # Make rectangle around face
        face_resize=cv2.resize(face,(width,height))

       
    ## Recognizer Part

        prediction=model.predict(face_resize)
        # Predict face

        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0))

        #
        if prediction[1]<800:
        #passing the id=prediction[0] to array of name then it shows name
            cv2.putText(img,'%s - %.0f' % (names[prediction[0]],prediction[1]),(x-10,y-10),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255))
            print(names[prediction[0]])
            cnt=0
        else:
            # Checking for 100 times if person is identified or not if not then it will go into cnt>100 condition and print unknown person
            cnt+=1
            cv2.putText(img,'Unknown',(x-10,y-10),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255))
            if(cnt>100):
                print("Unknown Person")
                cv2.imwrite('input.jpg',img)
                # save unknown person image
                cnt=0
    cv2.imshow('OpenCV',img)
    key=cv2.waitKey(10)
    if key==27:
        break
webCam.release()