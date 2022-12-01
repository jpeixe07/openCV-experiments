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
myRadius=30
myColor=(255,255,255)
myThick=3
myText='Hello World'
upperleft=(250,140)
theColor=(0,255,0)
lowerRight=(390,220)
font=cv2.FONT_HERSHEY_COMPLEX
fontSize=1
bllue=(255,0,0)
fontThickness=2
tlast=time.time()
time.sleep(.1)
while True:
    dT=time.time()-tlast
    #print(dT)
    fps=1/dT  #if dt is 0,5 sec, then fps=2
    print(fps)
    tlast=time.time()
    ignore, frame=cam.read()
    frame[140:220,250:390]=(255,0,0) #black box
    cv2.rectangle(frame,upperleft,lowerRight,(0,255,0),4) #-1 deixa o quadrado preenchidoqqqq
    
    cv2.circle(frame,(int(width/2),int(height/2)),myRadius,myColor,myThick)
    
    cv2.putText(frame,myText,(120,100),font,fontSize,bllue,fontThickness) 
    cv2.putText(frame,str(int(fps))+' FPS',(5,30),font,1,(0,255,255),2)
    
    cv2.imshow('My WEBCAM',frame)
    cv2.moveWindow('My WEBCAM',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()