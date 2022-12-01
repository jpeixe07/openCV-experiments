#TRAIN THE FACES AND PICKLE THE DATA 
import cv2
import face_recognition as FR
import os
import pickle
names=[]
knownEncodings=[]
width=640 #1920,1280,320
height=360 #1080,720,180
font=cv2.FONT_HERSHEY_SIMPLEX

cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #CAPTURING THE FRAME AND DOING A DIRECT SHOW
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #set the width we want
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #set the height we want
cam.set(cv2.CAP_PROP_FPS, 30) 
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) #moving jpg


trainSetDir='C:\\Users\\jpedr\\Documents\\Python\\trainSet'
for root, dirs,files in os.walk(trainSetDir):
    #print('My Working Folder (root): ',root)
    #print('Dirs in root: ',dirs)
    #print('My files in root', files)
    for file in files:
        fullFilePath=os.path.join(trainSetDir,file)
        name=os.path.splitext(file)[0]
        names.append(name) #adiciona no fim da lista
        myPic=FR.load_image_file(fullFilePath)
        myPicLoc=FR.face_locations(myPic)[0] #first face so it doesnt return an array of arrays
        myPicEncode=FR.face_encodings(myPic)[0]
        knownEncodings.append(myPicEncode) #adding the encode to the list



#print(knownEncodings)
print(names)
with open('trainSet.pkl','wb') as f:
    pickle.dump(knownEncodings,f) #Ideally, you dont want to pickle data, since is low and not very Secure, according to whoever said that
    pickle.dump(names,f)
while True:
    ignore, frame=cam.read()
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    faceLocations=FR.face_locations(frameRGB)
    unknownEncodings=FR.face_encodings(frameRGB,faceLocations)
    for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
        
        top,right,bottom,left=faceLocation
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),3)
        name='Desconhecido'
        matches=FR.compare_faces(knownEncodings,unknownEncoding)
        print(matches)
        if True in matches:
            matchIndex=matches.index(True)
            print(names[matchIndex]) #por isso a ordem precisa ser a mesma
            name=names[matchIndex]
        cv2.putText(frame,name,(left,top),font,2,(255,0,0),3)
    
    cv2.imshow('My WEBCAM',frame)
    cv2.moveWindow('My WEBCAM',0,0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()