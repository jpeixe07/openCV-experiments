import cv2
import mediapipe as mp

class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=.5,tol2=.5):
        self.hands=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
    def Marks(self,frame):
        myHands=[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands
class mpPose: 
    def __init__(self,imgType,UpperBody,Smo=True,tol1=.5,tol2=.5):
        self.myPose=mp.solutions.pose.Pose(imgType,UpperBody,Smo,tol1,tol2)
    def Marks(self,frame):
        landMarks=[]
        mpDraw=mp.solutions.drawing_utils
        #mpDraw.draw_landmarks(frame,results.pose_landmarks,mp.solutions.pose.POSE_CONNECTIONS)
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.myPose.process(frameRGB)
        if results.pose_landmarks != None:
            for lm in results.pose_landmarks.landmark:
                landMarks.append((int(lm.x*width),int(lm.y*height)))
        return landMarks

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
width=1280
height=720
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #set the width we want
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #set the height we want
cam.set(cv2.CAP_PROP_FPS, 30) 
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame=cam.read()
    jpPose=mpPose(False,False,True)
    poseLandmarks=jpPose.Marks(frame)
    if len(poseLandmarks)!=0:
        print(poseLandmarks)
    #cv2.circle(frame,poseLandmarks[0],10,(0,0,255),2)

    cv2.imshow('My Webcam',frame)
    cv2.moveWindow('My Webcam',0,0)
    if cv2.waitKey(1) & 0xff== ord('q'):
        break
cam.release()