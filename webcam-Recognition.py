import cv2
import numpy as np
import face_recognition as FR
import time

width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) #moving jpg
fontFPS=cv2.FONT_HERSHEY_COMPLEX
font=cv2.FONT_HERSHEY_SIMPLEX
#Defining the known encodings:
joaoPic=FR.load_image_file('C:\\Users\\jpedr\\Documents\\Python\\trainSet\\joaoPedro.jpg')
faceLoc=FR.face_locations(joaoPic)[0]
joaoFaceEncodings=FR.face_encodings(joaoPic)[0]

knownEncodings=[joaoFaceEncodings]
names=['JOAO PEDRO']


tlast=time.time()
time.sleep(1)
while True:
    dT=time.time()-tlast
    fps=1/dT
    tlast=time.time()
    ignore, frame=cam.read()
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
    faceLocations=FR.face_locations(frameRGB)
    unknownEncodings=FR.face_encodings(frameRGB,faceLocations)

    for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
        top,right,bottom,left=faceLocation
        print(faceLocation)
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),3)
        name='Desconhecido'
        matches=FR.compare_faces(knownEncodings,unknownEncoding)
        print(matches)
        if True in matches:
            matchIndex=matches.index(True)
            print(names[matchIndex])
            name=names[matchIndex]
        cv2.putText(frame,name,(left,top),font,1,(255,0,0),3)
    cv2.putText(frame,str(int(fps)),(25,25),fontFPS,1,(0,255,255),2)
    cv2.imshow('MYWEB',frame)
    cv2.moveWindow('MYWEB',0,0)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()
