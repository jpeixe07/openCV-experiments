import cv2
import numpy as np
print(cv2.__version__)
width=640 ########
height=360 #############
snipW=120
snipH=60
boxCR=(height/2) #center row
boxCC=(width/2) #center column
deltaRow=10 #how many pixels each time through
deltaColumn=10 #same here
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

mycolor=(0,255,0)
mythick=2
while True:
    ignore, frame = cam.read()
    frameROI=frame[int(boxCR-snipH/2):int(boxCR+snipH/2),int(boxCC-snipW/2):int(boxCC+snipW/2)]
    #where the magic happens
    #cv2.rectangle(frame,upperLeft,lowerRight,mycolor,mythick)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame=cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    frame[int(boxCR-snipH/2):int(boxCR+snipH/2),int(boxCC-snipW/2):int(boxCC+snipW/2)]=frameROI

    if boxCR-snipH/2 <=0 or boxCR+snipH/2 >=height:
        deltaRow=deltaRow*(-1)
    if boxCC-snipW/2<=0 or boxCC+snipH/2>=width:
        deltaColumn=deltaColumn*(-1)
    
    boxCR=boxCR+deltaRow
    boxCC=boxCC+deltaColumn
    

    cv2.imshow('MYROI',frameROI)
    cv2.moveWindow('MYROI',width,0)
    cv2.imshow('MyWEBCAM', frame)
    cv2.moveWindow('MyWEBCAM',0,0)





    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
