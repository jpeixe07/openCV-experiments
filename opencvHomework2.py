import cv2
#FASTER LAUNCH OF THE WEBCAM AND SMOOTHER VIDEO IN openCV

rows=int(input('How Many Rows? '))
columns=int(input('How Many Columns? '))

width=1280 #1920,1280,320
height=720 #1080,720,180
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW) #CAPTURING THE FRAME AND DOING A DIRECT SHOW
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) #set the width we want
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height) #set the height we want
cam.set(cv2.CAP_PROP_FPS, 30) 
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) #moving jpg

while True:
    ignore, frame=cam.read()
    frame=cv2.resize(frame,(int(width/columns),int(height/columns)))
    for i in range(0,rows):
        for j in range(0,columns):
            windName='Window'+str(i)+' x '+str(j)
            cv2.imshow(windName,frame)
            cv2.moveWindow(windName,int(width/columns)*j,int(height/columns+30)*i)

    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()