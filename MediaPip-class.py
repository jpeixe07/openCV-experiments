import cv2 
width=640 #1920,1280,320
height=360 #1080,720,180

class HandP:
    import mediapipe as mp
    
    def __init__(self,nameP,Frame,iType,Q):
        self.HandOwner=nameP #nome de quem a mão (ou mãos) pertence
        self.Frame=cv2.cvtColor(Frame,cv2.COLOR_BGR2RGB) #já convertendo para RGB o frame escolhido para processamento
        self.imgType=iType #o tipo, True para estático, False para não estático
        self.numHands=Q #Quantas mãos esse indivíduo possuí e quantas delas vão ser levadas em conta
        
    def mpHand(self):
        import mediapipe as mp
        self.mp=mp.solutions.hands.Hands(self.imgType,self.numHands,.5,.5)
        return self.mp

    def process_and_append(self): #Você precisa assinalar o retorno da função a uma variável e 
        import mediapipe as mp
        mpDraw=mp.solutions.drawing_utils 
        #declarar ela novamente quando for chamar essa função
        results=self.mp.process(self.Frame)
        myHands=[]
        
        if results.multi_hand_landmarks !=None:
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                #mpDraw.draw_landmarks(frame,handLandMarks,mp.solutions.hands.HAND_CONNECTIONS) #step trought each landmarks of a hand
                for Landmark in handLandMarks.landmark: 
                    #I want the x and y value of each landmark of one hand
                    myHand.append((int(Landmark.x*width),int(Landmark.y*height)))
                myHands.append(myHand)
            self.myHands=myHands
            self.myHand=myHand
        else:
            self.myHands=0
            self.myHand=0
        return self.myHands,self.myHand #the method returns one array of arrays with the 21 landmarks of both hands
                                #and another returns one array with 21 landmarks of the last hand recognized
       
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #CAPTURING THE FRAME AND DOING A DIRECT SHOW
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #set the width we want
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #set the height we want
cam.set(cv2.CAP_PROP_FPS, 30) 
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) #moving jpg

while True:
    ignore, frame=cam.read()
    handJp=HandP('JoaoPedro',frame,False,2)
    mp_joao=handJp.mpHand()
    handsJp,handJp=handJp.process_and_append()
    if handJp != 0:
        for hand in handsJp:
            for ind in [0,5,6,7,8]:
                cv2.circle(frame,hand[ind],25,(0,255,255),3)
        

    cv2.imshow('My WEBCAM',frame)
    cv2.moveWindow('My WEBCAM',0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()

