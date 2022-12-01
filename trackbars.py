import cv2
width=1280 #1920,1280,320
height=720 #1080,720,180
def myCallBack1(val):
    global xPos
    print('xPos: ',val)
    xPos=val
def myCallBack2(val):
    global yPos
    print('yPos: ',val)
    yPos=val
def myCallBack3(val):
    global myRad
    print('radius: ',val)
    myRad=val
def myCallBack4(val):
    global myThick
    print('myThick: ',val)
    myThick=val
xPos=int(width/2)
yPos=int(height/2)
myRad=25
myThick=1
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #CAPTURING THE FRAME AND DOING A DIRECT SHOW
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #set the width we want
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #set the height we want
cam.set(cv2.CAP_PROP_FPS, 30) 
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) #moving jpg
cv2.namedWindow('myTrackbars')
cv2.resizeWindow('myTrackbars',400,150)
cv2.moveWindow('myTrackbars',width,0)
cv2.createTrackbar('xPos','myTrackbars',xPos,1920,myCallBack1) #precisa criar uma janela anteriormente
cv2.createTrackbar('yPos','myTrackbars',yPos,1080,myCallBack2)
cv2.createTrackbar('radius','myTrackbars',myRad,int(height/2),myCallBack3)
cv2.createTrackbar('thick','myTrackbars',myThick,7,myCallBack4)
#o primeiro valor é onde a trackbar começa, e não o valor mínimo que ela pode assumir
while True:
    ignore, frame=cam.read()
    if myThick==0:
        myThick=(-1)

    cv2.circle(frame,(xPos,yPos),myRad,(255,0,255),myThick)
    cv2.imshow('My WEBCAM',frame)
    cv2.moveWindow('My WEBCAM',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()