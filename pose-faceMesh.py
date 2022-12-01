import cv2
#print(cv2.__version__)
import mediapipe as mp
#FASTER LAUNCH OF THE WEBCAM AND SMOOTHER VIDEO IN openCV
width=1280 #1920,1280,320
height=720 #1080,720,180
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #CAPTURING THE FRAME AND DOING A DIRECT SHOW
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #set the width we want
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #set the height we want
cam.set(cv2.CAP_PROP_FPS, 30) 
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) #moving jpg
faceMesh=mp.solutions.face_mesh.FaceMesh(False)#)
#img type, num of faces
mpDraw=mp.solutions.drawing_utils
drawSpecCircle=mpDraw.DrawingSpec(thickness=1,circle_radius=2,color=(255,0,0))
drawSpecLine=mpDraw.DrawingSpec(thickness=3,circle_radius=2,color=(0,0,255))
#settings some parameters to have control of the mp.draw solution


font=cv2.FONT_HERSHEY_SIMPLEX
fontSize=.3
fontColor=(0,255,255)
fontThick=1


while True:
    ignore, frame=cam.read()
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=faceMesh.process(frameRGB)
    #print(results.multi_face_landmarks)
    #the way we crack into is:
    if results.multi_face_landmarks != None:
        for faceLandmarks in results.multi_face_landmarks:
            #468 data points formando o facemesh
            mpDraw.draw_landmarks(frame,faceLandmarks,mp.solutions.face_mesh.FACE_CONNECTIONS,drawSpecCircle,drawSpecLine)
            #it is looking for the circle spec first, then the line spec
            indx=0
            for lm in faceLandmarks.landmark:
                cv2.putText(frame,str(indx),(int(lm.x*width),int(lm.y*height)),font,fontSize,fontColor,fontThick)
                indx=indx+1
    cv2.imshow('My WEBCAM',frame)
    cv2.moveWindow('My WEBCAM',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()