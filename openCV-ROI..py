import cv2


#decidindo arbitrariamente onde será a região de interesse

width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame = cam.read()
    frameROI=frame[150:210,250:390] #assinalando a sua região de interesse da imagem declarando a slice de rows e columns desejada
    frameROIGRAY=cv2.cvtColor(frameROI,cv2.COLOR_BGR2GRAY) #convertendo a imagem para preto e branco
    frameROIBGR=cv2.cvtColor(frameROIGRAY,cv2.COLOR_GRAY2BGR) #convertendo a imagem em preto e branco para uma matriz com 3 pontos (0,0,0)
    frame[150:210,250:390]=frameROIBGR #quando você assinalar a MY ROY vai se tornar cinza tb
    cv2.imshow('MY BGR ROI',frameROIBGR) #caso você tentasse mostrar a imagem sem converter de volta para BGR ia dar erro
    cv2.moveWindow('MY BGR ROI',650,180)
    
    cv2.imshow('MY GRAY ROI', frameROIGRAY)
    cv2.moveWindow('MY GRAY ROI', 650,90)

    cv2.imshow('MY ROI', frameROI)
    cv2.moveWindow('MY ROI',650,0)
    
    cv2.imshow('MY WEBCAM', frame)
    cv2.moveWindow('MY WEBCAM', 0,0)
    
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cam.release()
