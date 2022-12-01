import cv2
import time
#FASTER LAUNCH OF THE WEBCAM AND SMOOTHER VIDEO IN openCV
width=640 #1920,1280,320
height=360 #1080,720,180
font=cv2.FONT_HERSHEY_COMPLEX
fontSize=1
Color=(0,0,255)
Thick=2
frame=cv2.imread('C:\\Users\\jpedr\\Documents\\Python\\testSet\\piscina.jpg')
#faceCascade=cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml') # if the haar paste is already on our working folder
faceCascade=cv2.CascadeClassifier('C:\\Users\jpedr\Documents\Python\haar\haarcascade_frontalface_default.xml')
eyeCascade=cv2.CascadeClassifier('C:\\Users\jpedr\Documents\Python\haar\haarcascade_eye.xml') #make sure to add the \ after C:\
#prebuilt model

while True:

    frameGray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #black and white images require less computation resources
    faces=faceCascade.detectMultiScale(frameGray,1.3,5)
    for face in faces:
        x,y,w,h=face
        #print('x=',x,'y=',y,'width=',w,'height=',h)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3) #same principle of color tracking rectangle
    eyes=eyeCascade.detectMultiScale(frameGray,1.3,5)
    for eye in eyes:
        xE,yE,wE,hE=eye
        cv2.rectangle(frame,(xE,yE),(xE+wE,yE+hE),(0,0,255),2) #putting the rectangles on your eyes



    cv2.imshow('My WEBCAM',frame)
    cv2.moveWindow('My WEBCAM',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break