from tkinter import image_names
import cv2
print(cv2.__version__)

cam=cv2.VideoCapture(0)
while True:
    ignore, frame = cam.read()
    grayFrame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #transformando de blue green red para grey
    #THIS IS WHERE THE MAGIC HAPPENS 
    #Artificial intelligence
    
    
    cv2.imshow('my WEBCAM',grayFrame)
    cv2.moveWindow('my WEBCAM',0,0)
    #gracefully exit the program so it releases the camera
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
