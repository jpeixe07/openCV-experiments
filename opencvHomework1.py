import cv2
#THE PROGRAM DISPLAY 4 WEBCAM IMAGES, 2 BLACK N WHITE & 2 W/COLOR
camera=cv2.VideoCapture(0)
while True:
    ignore, frame_raw = camera.read()
    grayFrame=cv2.cvtColor(frame_raw,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('webcamTopRight',frame_raw)
    cv2.imshow('webcamBottomRight',grayFrame)
    cv2.imshow('webcamBottomLeft',frame_raw)
    cv2.imshow('webcamTopLeft',grayFrame)
    
    cv2.moveWindow('webcamTopRight',900,0)
    cv2.moveWindow('webcamTopLeft',0,0) #640 480
    cv2.moveWindow('webcamBottomRight',900,400)
    cv2.moveWindow('webcamBottomLeft',0,400)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
    #because of the numLock the key may return 2 differnte values
    #that's why the 0xff is needed, to take only the last byte of the returned value
camera.release()