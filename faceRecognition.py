import cv2
import face_recognition as FR
font=cv2.FONT_HERSHEY_SIMPLEX
donFace=FR.load_image_file('C:\\Users\jpedr\\Documents\\Python\\demoImages\\known\\Donald Trump.jpg')
faceLoc=FR.face_locations(donFace)[0]#o primeiro rosto que achar no donFace
donFaceEncode=FR.face_encodings(donFace)[0] #procedure for array of encodings'
#print(faceLoc) #return arrays of arrays even if it is just one face detected
#top,right,bottom,left=faceLoc
#cv2.rectangle(donFace,(left,top),(right,bottom),(255,0,0),3)
#donFaceBGR=cv2.cvtColor(donFace,cv2.COLOR_RGB2BGR) #we need to convert to BGR to show
nancyFace=FR.load_image_file('C:\\Users\\jpedr\\Documents\\Python\\demoImages\\known\\Nancy Pelosi.jpg')
faceLoc=FR.face_locations(nancyFace)[0]
nancyFaceEncode=FR.face_encodings(nancyFace)[0]

penceFace=FR.load_image_file('C:\\Users\\jpedr\\Documents\\Python\\demoImages\\known\\Mike Pence.jpg')
faceLoc=FR.face_locations(penceFace)[0]
penceFaceEncode=FR.face_encodings(penceFace)[0]

knownEncodings=[donFaceEncode,nancyFaceEncode,penceFaceEncode]
names=['Donald Trump','Nancy Pelosi','Mike Pence'] #must be in the same order

unknownFace=FR.load_image_file('C:\\Users\\jpedr\\Documents\\Python\\demoImages\\unknown\\u1.jpg')
unknownFaceBGR=cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR) #Converting to BGR for display purposes
faceLocations=FR.face_locations(unknownFace)#achar algum rosto na foto(unknownFace)
unknownEncodings=FR.face_encodings(unknownFace,faceLocations) #encodes the images based on the location

for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings): #The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
    #If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.
    
    #para cada localização do rosto e encode da foto com desconhecidos na lista de lista face locations e encode:
    
    top,right,bottom,left=faceLocation #face location é uma tupla com 4 numeros descrevendo a localização do rosto encontrado
    print(faceLocation)
    cv2.rectangle(unknownFaceBGR,(left,top),(right,bottom),(255,0,0),3)
    name='Unknown Person'
    matches=FR.compare_faces(knownEncodings,unknownEncoding)
    print(matches)
    if True in matches:  #em cada vez que o loop acontecer, só vai acontecer uma match com o rosto, e essa condicional vai nos mostrar aonde foi
        matchIndex=matches.index(True)
        print(matchIndex) #mostra a localização da lista onde foi True o reconhecimento
        print(names[matchIndex])
        name=names[matchIndex]
    cv2.putText(unknownFaceBGR,name,(left,top),font,.75,(0,0,255),2)

cv2.imshow('My Faces', unknownFaceBGR)
cv2.waitKey(5000)
