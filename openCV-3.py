import cv2
#FASTER LAUNCH OF THE WEBCAM AND SMOOTHER VIDEO IN openCV
width=640 #1920,1280,320
height=360 #1080,720,180
cam=cv2.VideoCapture(1) #CAPTURING THE FRAME AND DOING A DIRECT SHOW
#cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #set the width we want
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #set the height we want
#cam.set(cv2.CAP_PROP_FPS, 30) 
#cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) #moving jpg

while True:
    ignore, frame=cam.read()
    
    cv2.imshow('My WEBCAM',frame)
    cv2.moveWindow('My WEBCAM',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()