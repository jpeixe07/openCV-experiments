import cv2
import numpy as np
#FASTER LAUNCH OF THE WEBCAM AND SMOOTHER VIDEO IN openCV
width=640 #1920,1280,320
height=360 #1080,720,180
#define the functions on the trackbar:
def onTrack1(val):
    global huelow
    huelow=val
    print('Hue Low',huelow)
def onTrack2(val):
    global huehigh
    huehigh=val
    print('Hue High',huehigh) #THE SECOND TRACKBAR
def onTrackHUE1(val):######
    global hue2low
    hue2low=val
    print('Hue 2 Low',hue2low) #THE SECOND TRACKBAR
def onTrackHUE2(val):###########
    global hue2high
    hue2high=val
    print('Hue 2 High',hue2high)
def onTrack3(val):
    global satlow
    satlow=val
    print('Sat Low',satlow)
def onTrack4(val):
    global sathigh
    sathigh=val
    print('Sat high',sathigh)
def onTrack5(val):
    global vallow
    vallow=val
    print('Val Low',vallow)
def onTrack6(val):
    global valhigh
    valhigh=val
    print('Val High',valhigh)



cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #CAPTURING THE FRAME AND DOING A DIRECT SHOW
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #set the width we want
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #set the height we want
cam.set(cv2.CAP_PROP_FPS, 30) 
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) #moving jpg


cv2.namedWindow('MyTracker')
cv2.resizeWindow('MyTracker',400,350)
cv2.moveWindow('MyTracker',width,0)
#Basically, color tracking is tracking the Hue (Goes from 0 to 179 and it is the color itself)
#And the Saturation value (defines how bright the color is)
#And the Val value, that defines how dark the Color is)
# #we need to set the initial values
huelow=10
hue2low=10
hue2high=20
huehigh=20
satlow=10
sathigh=250
vallow=10
valhigh=250
cv2.createTrackbar('Hue Low','MyTracker',10,179,onTrack1)
cv2.createTrackbar('Hue High','MyTracker',20,179,onTrack2)
cv2.createTrackbar('Hue 2 Low','MyTracker',10,179,onTrackHUE1)
cv2.createTrackbar('Hue 2 High','MyTracker',20,179,onTrackHUE2)
cv2.createTrackbar('Sat Low','MyTracker',10,255,onTrack3)
cv2.createTrackbar('Sat High','MyTracker',250,255,onTrack4)
cv2.createTrackbar('Val Low','MyTracker',10,255,onTrack5)
cv2.createTrackbar('Val High','MyTracker',250,255,onTrack6)
#######################
while True:
    ignore, frame=cam.read()
    
    
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lowerBound=np.array([huelow,satlow,vallow]) #set the minimum array value to compare
    upperBound=np.array([huehigh,sathigh,valhigh])#set the maximum array value to compare
    lowerBound2=np.array([hue2low,satlow,vallow]) #the second parameter for multi color tracking
    upperBound2=np.array([hue2high,sathigh,valhigh])#same here brah
    myMask=cv2.inRange(frameHSV,lowerBound,upperBound) #will show all the pixels that are in the range of lower and upperBound and it will turn white(in range) or black(not in range)
    myMask2=cv2.inRange(frameHSV,lowerBound2,upperBound2)
    myMaskUnion= myMask | myMask2
    #myMask=cv2.bitwise_not(myMask) the color that matches the HSV values is removed from the Object frame
    myObject=cv2.bitwise_and(frame,frame,mask=myMaskUnion)
 

    myObjectsmall=cv2.resize(myObject,(int(width/2),int(height/2)))    
    cv2.imshow('My Object',myObjectsmall)
    cv2.moveWindow('My Object',int(width/2),int(height))
    myMaskSmall=cv2.resize(myMask,(int(width/2),int(height/2)))
    myMask2Small=cv2.resize(myMask2,(int(width/2),int(height/2)))#only for display purposes
    cv2.imshow('My Mask', myMaskSmall)
    cv2.imshow('My Mask2', myMask2Small)
    cv2.moveWindow('My Mask',0,height)
    cv2.moveWindow('My Mask2',0,height+int(height/2)+30)
    
    
    ###################
    cv2.imshow('My WEBCAM',frame)
    cv2.moveWindow('My WEBCAM',0,0)
    
    ####################
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()