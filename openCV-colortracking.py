import numpy as np
import cv2
evt=0
yVal=0
xVal=0

def mouseclick(event, xPos, yPos, flags,params):
    global evt
    global xVal
    global yVal
    if event==cv2.EVENT_LBUTTONDOWN:
        print(event)
        evt=event
        xVal=xPos
        yVal=yPos
    if event == cv2.EVENT_RBUTTONUP:
        evt=event
        print(event)



#FASTER LAUNCH OF THE WEBCAM AND SMOOTHER VIDEO IN openCV
width=640 #1920,1280,320
height=360 #1080,720,180
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #CAPTURING THE FRAME AND DOING A DIRECT SHOW
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #set the width we want
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #set the height we want
cam.set(cv2.CAP_PROP_FPS, 30) 
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) #moving jpg
cv2.namedWindow('My WEBCAM')

cv2.setMouseCallback('My WEBCAM',mouseclick)
while True:
    ignore, frame=cam.read()
    if evt==1:
        x=np.zeros([250,250,3],dtype=np.uint8)
        y=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        clr=y[yVal][xVal]
        print(clr) #codigo ta dando problema e não ta marcando as cores direito
        x[:,:]=clr
        x=cv2.cvtColor(x,cv2.COLOR_HSV2BGR)
        cv2.putText(x,str(clr),(0,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),1) 
        cv2.imshow('Color Picker', x)
        cv2.moveWindow('Color Picker', width,0)
        evt=0
    cv2.imshow('My WEBCAM',frame)
    cv2.moveWindow('My WEBCAM',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()