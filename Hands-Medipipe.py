import cv2
import mediapipe as mp

#FASTER LAUNCH OF THE WEBCAM AND SMOOTHER VIDEO IN openCV
width=640 #1920,1280,320
height=360 #1080,720,180
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #CAPTURING THE FRAME AND DOING A DIRECT SHOW
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #set the width we want
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #set the height we want
cam.set(cv2.CAP_PROP_FPS, 30) 
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) #moving jpg

hands=mp.solutions.hands.Hands(False,2,.5,.5)
mpDraw=mp.solutions.drawing_utils

while True:
    myHands=[]
    ignore, frame=cam.read()
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=hands.process(frameRGB)
    
    if results.multi_hand_landmarks !=None: #each hand has 21 landmarks
        for handLandMarks in results.multi_hand_landmarks: #step trought each landmarks of a hand
            myHand=[]
            #mpDraw.draw_landmarks(frame,handLandMarks,mp.solutions.hands.HAND_CONNECTIONS)
            for Landmark in handLandMarks.landmark: 
                #I want the x and y value of each landmark of one hand
                myHand.append((int(Landmark.x*width),int(Landmark.y*height)))
                #denormalize the x and y values (before they were 0.something)
            cv2.circle(frame,myHand[20],15,(255,0,255),-1)
            cv2.circle(frame,myHand[19],15,(255,0,255),-1)
            cv2.circle(frame,myHand[18],15,(255,0,255),-1)
            cv2.circle(frame,myHand[17],15,(255,0,255),-1)
            myHands.append(myHand)
            
            
            print(myHand)
            print('')
            print(myHands)
            print('')
    
    
    cv2.imshow('My WEBCAM',frame)
    cv2.moveWindow('My WEBCAM',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
