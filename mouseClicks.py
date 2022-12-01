import cv2
print(cv2.__version__)
width=1280
height=720
evt=0
def mouseClick(event,xPos,yPos,flags,params):
    global evt
    global pnt
    if event==cv2.EVENT_LBUTTONDOWN: #Botao esquerdo mouse apertado
        print('Mouse Event was: ', event)
        print('At position: ', xPos,yPos)
        print(flags)
        print(params)
        evt=event
        pnt=(xPos,yPos)

    if event==cv2.EVENT_LBUTTONUP: #Botao esquerdo mouse "soltado"
        print('Mouse event was: ', event)
        print('At position: ', xPos,yPos)
        print(flags)
        print(params)
        evt=event
    if event==cv2.EVENT_RBUTTONUP: #botao direito do mouse "soltado"
        pnt=(xPos,yPos)
        evt=event
    if event==cv2.EVENT_RBUTTONDOWN: #botao direito mouse apertado
        print('R Button DOWN: ', event)
        evt=event
        pnt=(xPos,yPos)
        
name='My WEBCAM'
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MPJG'))
cv2.namedWindow(name)

cv2.setMouseCallback(name,mouseClick,) #retorna o valor do mouse e ativa a função que deve ser definida anteriormente

while True:
    ignore, frame=cam.read()
    if evt==1 or evt==4:
        cv2.circle(frame,pnt,25,(255,0,0),2)  

    cv2.imshow(name, frame)
    cv2.moveWindow(name, 0,0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
