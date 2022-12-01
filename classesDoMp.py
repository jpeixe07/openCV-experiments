import cv2
#print(cv2.__version__)
import mediapipe as mp

class mpHands:
    import mediapipe as mp
    def __init__(self,maxHands=2,tol1=.5,tol2=.5):
        self.hands=self.mp.solutions.hands.Hands(False,maxHands,tol1,tol2)
    def Marks(self,frame):
        myHands=[]
        handsType=[]
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for hand in results.multi_handedness:
                handType=hand.classification[0].label
                handsType.append(handType)
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landMark in handLandMarks.landmark:
                    myHand.append((int(landMark.x*width),int(landMark.y*height)))
                myHands.append(myHand)
        return myHands,handsType

class mpPose:
    #having trouble in importing mediapipe in the class
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

class mpFace:
    #having trouble in importing mediapipe in the class
    def __init__(self):
        self.myface=mp.solutions.face_detection.FaceDetection()
    def Marks(self,frame,):
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.myface.process(frameRGB)
        faceBoundBoxs=[]
        listaCentro=[]
        if results.detections != None:
            for face in results.detections:
                #creating a shortcut
                bBox=face.location_data.relative_bounding_box
                topLeft=(int(bBox.xmin*width),int(bBox.ymin*height))
                bottomRight=(int((bBox.xmin+bBox.width)*width),int((bBox.ymin+bBox.height)*height))
                faceBoundBoxs.append((topLeft,bottomRight)) #2 tuples in a list for each face    
        return faceBoundBoxs

class mpMesh:
    import mediapipe as mp 
    def __init__(self,imgType=False,numP=3,tol1=.5,tol2=.5,drawMesh=True):
        mpDraw=mp.solutions.drawing_utils
        self.myDraw=self.mp.solutions.drawing_utils
        self.draw=drawMesh
        self.faceMesh=mp.solutions.face_mesh.FaceMesh(imgType,numP,tol1,tol2)
    def Marks(self,frame):
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=self.faceMesh.process(frameRGB)
        facesMeshLandmarks=[]
        if results.multi_face_landmarks != None:
            for faceMesh in results.multi_face_landmarks:
                faceMeshLandmarks=[]
                for lm in faceMesh.landmark:
                    loc=(int(lm.x*width),int(lm.y*height))
                    faceMeshLandmarks.append(loc)
                facesMeshLandmarks.append(faceMeshLandmarks)
            if self.draw==True:
                self.myDraw.draw_landmarks(frame,faceMesh)
        return facesMeshLandmarks


def setLower(value):
    global lowerlimit
    lowerlimit=value
def setUpper(value):
    global upperLimit
    upperLimit=value


width=1280
height=720
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

#Creating those objects 
findHands=mpHands(2)
findFace=mpFace()
findPose=mpPose(False,False,True)
findMesh=mpMesh(drawMesh=True)
    
fontColor=(0,0,255)
fontThick=3
fontThick1=1
fontSize=.4
font=cv2.FONT_HERSHEY_SIMPLEX
circleRadius=20

lowerlimit=0
upperLimit=468

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',width+50,0)
cv2.resizeWindow('Trackbars',400,150)
cv2.createTrackbar('lower limit','Trackbars',0,468,setLower)
cv2.createTrackbar('upperLimit','Trackbars',468,468,setUpper)

while True:
    ignore,  frame = cam.read()
    #the landmarks and the hand type

    handsLM,handsType=findHands.Marks(frame)
    faceLoc =findFace.Marks(frame)
    poseLM=findPose.Marks(frame)
    meshLM=findMesh.Marks(frame)
    for faceMeshLM in meshLM:
        #each face singular in the array of arrays
        cnt=0
        for lm in faceMeshLM:
            if cnt>=lowerlimit and cnt<=upperLimit:

                cv2.putText(frame,str(cnt),lm,font,fontSize,fontColor,fontThick1)
            cnt=cnt+1

    if poseLM != []:
        for ind in [13,14,15,16]:
            cv2.circle(frame,poseLM[ind],circleRadius,(0,255,0),-1)
    for face in faceLoc:
        #each face has a list of the topleft and top bottom coordinates
        cv2.rectangle(frame,face[0],face[1],(0,255,255),3)
    for hand,handType in zip(handsLM,handsType):
        if handType=='Right':
            lbl='Left'
        if handType=='Left':
            lbl='Right'
        cv2.putText(frame,lbl,hand[8],cv2.FONT_HERSHEY_SIMPLEX,3,fontColor,fontThick,2)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()