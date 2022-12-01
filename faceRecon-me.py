import cv2
import face_recognition as FR
font=cv2.FONT_HERSHEY_SIMPLEX

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA): #resizing the picture
    dim = None
    (h, w) = image.shape[:2] #getting the height and width values from the tuple that returns
    #--- is (row, columns, channels) - but we dont want channels

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)
#adding joaopedro and saving his encoded face
joaoPic=FR.load_image_file('C:\\Users\\jpedr\\Documents\\Python\\trainSet\\joaoPedro.jpg')
jpLoc=FR.face_locations(joaoPic)[0]
jpFaceEncode=FR.face_encodings(joaoPic)[0]
#adding vitoria and saving his encoded face
vitoriaPic=FR.load_image_file('C:\\Users\\jpedr\\Documents\\Python\\trainSet\\vitoria.jpg')
vitoriaLoc=FR.face_locations(vitoriaPic)[0]
vitoriaFaceEncode=FR.face_encodings(vitoriaPic)[0]
#adding andre and saving his encoded face
andrePic=FR.load_image_file('C:\\Users\\jpedr\\Documents\\Python\\trainSet\\andre.jpg')
andreLoc=FR.face_locations(andrePic)[0]
andreFaceEncode=FR.face_encodings(andrePic)[0]
#adding tiago to and saving his encoded face
tiagoPic=FR.load_image_file('C:\\Users\\jpedr\\Documents\\Python\\trainSet\\tiago.jpg')
tiagoLoc=FR.face_locations(tiagoPic)[0]
tiagoFaceEncode=FR.face_encodings(tiagoPic)[0]
#adding lucas to and saving his encoded face
lucasPic=FR.load_image_file('C:\\Users\\jpedr\\Documents\\Python\\trainSet\\lucasNovo.jpg')
lucasLoc=FR.face_locations(lucasPic)[0]
lucasFaceEncode=FR.face_encodings(lucasPic)[0]

vovoPic=FR.load_image_file('C:\\Users\\jpedr\\Documents\\Python\\trainSet\\Vovo.jpg')
vovoLoc=FR.face_locations(vovoPic)[0]
vovoFaceEncode=FR.face_encodings(vovoPic)[0]

#ivaniraPic=FR.load_image_file('C:\\Users\\jpedr\\Documents\\Python\\trainSet\\ivanira.jpg')
#ivaniraLoc=FR.face_locations(ivaniraPic)[0]
#ivaniraFaceEncode=FR.face_encodings(ivaniraPic)[0]

#saving the encoded faces and adding a list of names based on the order of the encoded faces list
knownEncodings=[jpFaceEncode,vitoriaFaceEncode,andreFaceEncode,tiagoFaceEncode,lucasFaceEncode,vovoFaceEncode]
names=['Joao Pedro','Vitoria','Andre SEXO','BAT POETA','Rapidinha','Maria das Neves']

trainPic=FR.load_image_file('C:\\Users\\jpedr\\Documents\\Python\\testSet\\amigas.jpg')
trainPicBGR=cv2.cvtColor(trainPic,cv2.COLOR_RGB2BGR) #for display purposes
faceLocations=FR.face_locations(trainPic)
unknownEncodings=FR.face_encodings(trainPic,faceLocations)

for faceLocation,unknownEncoding in zip(faceLocations,unknownEncodings):
    top,right,bottom,left=faceLocation
    print(faceLocation)
    cv2.rectangle(trainPicBGR,(left,top),(right,bottom),(0,0,255),3)
    name='Desconhecido'
    matches=FR.compare_faces(knownEncodings,unknownEncoding)
    print(matches)
    if True in matches: #em cada vez que o loop acontecer, só vai acontecer uma match com o rosto, e essa condicional vai nos mostrar aonde foi
        matchIndex=matches.index(True)
        print(names[matchIndex]) #por isso a ordem precisa ser a mesma
        name=names[matchIndex]
    cv2.putText(trainPicBGR,name,(left,top),font,2,(255,0,0),3) #.5,.75

resize=ResizeWithAspectRatio(trainPicBGR, width=640)
cv2.imshow('My Faces',resize)

cv2.waitKey(15000)
