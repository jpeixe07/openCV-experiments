import cv2
print(cv2.__version__)
width=640
height=360
evt=0

def mouseClick(event,xPos,yPos,flags,params):
    global evt
    global pnt1
    global pnt2
    
    if event==cv2.EVENT_LBUTTONDOWN:
        print('Left Button Down')
        evt=event #1
        pnt1=(xPos,yPos)
    if event==cv2.EVENT_LBUTTONUP:
        print('Left Button Up')
        evt=event #4
        pnt2=(xPos,yPos)
        print(pnt2)
    if event ==cv2.EVENT_RBUTTONUP:
        evt=event
        print('R button Up')


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
    
    if evt==4:
        cv2.rectangle(frame,pnt1,pnt2,(255,255,0),3)
        ROI=frame[pnt1[1]:pnt2[1],pnt1[0]:pnt2[0]] # rows primeiro e depois columns
        cv2.imshow('ROI', ROI)
        cv2.moveWindow('ROI', int(width*1.1),0)
    if evt==5:
        cv2.destroyWindow('ROI')
        evt=0
    cv2.imshow(name, frame)
    cv2.moveWindow(name, 0,0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()