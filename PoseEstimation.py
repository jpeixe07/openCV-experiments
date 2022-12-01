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

pose=mp.solutions.pose.Pose(False,False,True,.5,.5)
#working with static image, working with upper only, and smoothing the points
mpDraw=mp.solutions.drawing_utils


circleRadius=(10)
circleColor=(0,0,255)
circleThickness=4
eyeRadius=10
eyeColor=(255,0,0)
eyeThickness=-1
while True:
    ignore, frame=cam.read()
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=pose.process(frameRGB)
    landMarks=[]
    if results.pose_landmarks!=None:
        #mpDraw.draw_landmarks(frame,results.pose_landmarks,mp.solutions.pose.POSE_CONNECTIONS)
        #print(results.pose_landmarks)
        for lm in results.pose_landmarks.landmark:
            landMarks.append((int(lm.x*width),int(lm.y*height)))
    cv2.circle(frame,landMarks[0],circleRadius,circleColor,circleThickness)
    cv2.circle(frame,landMarks[2],eyeRadius,eyeColor,eyeThickness)
    cv2.circle(frame,landMarks[5],eyeRadius,eyeColor,eyeThickness)
    cv2.imshow('My WEBCAM',frame)
    cv2.moveWindow('My WEBCAM',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()