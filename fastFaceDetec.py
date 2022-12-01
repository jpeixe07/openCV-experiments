import cv2
import mediapipe as mp
#FASTER LAUNCH OF THE WEBCAM AND SMOOTHER VIDEO IN openCV
width=1280 #1920,1280,320
height=720 #1080,720,180
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #CAPTURING THE FRAME AND DOING A DIRECT SHOW
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #set the width we want
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #set the height we want
cam.set(cv2.CAP_PROP_FPS, 30) 
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) #moving jpg

findFace=mp.solutions.face_detection.FaceDetection()
drawFace=mp.solutions.drawing_utils
while True:
    ignore, frame=cam.read()
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=findFace.process(frameRGB)
    print(results.detections)
    
    #the output has many layers of data, so we need to specify exactly what
    #we want and where it is the data, in this case we want the relative_bounding box
    #and the ymin and xmin
    if results.detections != None:
        for face in results.detections:
           # drawFace.draw_detection(frame,face)
            #creating a shortcut for reference
            bBox=face.location_data.relative_bounding_box
            topLeft=(int(bBox.xmin*width),int(bBox.ymin*height))
            #escaling to pixels and definig the topleft to use on cv2
            bottomRight=(int((bBox.xmin+bBox.width)*width),int((bBox.ymin+bBox.height)*height))
            cv2.rectangle(frame,topLeft,bottomRight,(0,255,0),3)
    cv2.imshow('My WEBCAM',frame)
    cv2.moveWindow('My WEBCAM',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()