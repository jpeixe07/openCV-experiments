import cv2
import time
#FASTER LAUNCH OF THE WEBCAM AND SMOOTHER VIDEO IN openCV
width=640 #1920,1280,320
height=360 #1080,720,180
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #CAPTURING THE FRAME AND DOING A DIRECT SHOW
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #set the width we want
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #set the height we want
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) #moving jpg
font=cv2.FONT_HERSHEY_COMPLEX
fontSize=1
Color=(0,0,255)
Thick=2
#faceCascade=cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml') # if the haar paste is already on our working folder
faceCascade=cv2.CascadeClassifier('C:\\Users\jpedr\Documents\Python\haar\haarcascade_frontalface_default.xml')
eyeCascade=cv2.CascadeClassifier('C:\\Users\jpedr\Documents\Python\haar\haarcascade_eye.xml') #make sure to add the \ after C:\
#prebuilt model
tlast=time.time()
time.sleep(1)
while True:
    dt=time.time()-tlast
    fps=1/dt
    tlast=time.time()
    ignore, frame=cam.read()
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


    cv2.putText(frame,str(int(fps))+' FPS',(35,30),font,fontSize,Color,Thick)
    cv2.imshow('My WEBCAM',frame)
    cv2.moveWindow('My WEBCAM',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()