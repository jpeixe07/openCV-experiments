#Create a program that uses 2 trackbars to set the size of the image 
#and the other moves the window across the screen
import cv2
def callback1(val):
    global xPos
    xPos=val
def callback2(val):
    global yPos
    yPos=val
def callback3(val):
    global width
    width=val
    height=int(width*9/16)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #set the width we want
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
#FASTER LAUNCH OF THE WEBCAM AND SMOOTHER VIDEO IN openCV
width=640 #1920,1280,320
height=360 #1080,720,180
name='my Trackbars'
xPos=0
yPos=0
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #CAPTURING THE FRAME AND DOING A DIRECT SHOW
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #set the width we want
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #set the height we want
cam.set(cv2.CAP_PROP_FPS, 30) 
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) #moving jpg
cv2.namedWindow(name)
cv2.moveWindow(name,width,0)
cv2.resizeWindow(name,400,150)
cv2.createTrackbar('xPos',name,0,2000,callback1)
cv2.createTrackbar('yPos',name,0,1000,callback2)
cv2.createTrackbar('width',name, width,1920,callback3)

while True:
    ignore, frame=cam.read()
    
    cv2.imshow('My WEBCAM',frame)
    cv2.moveWindow('My WEBCAM',xPos,yPos)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()