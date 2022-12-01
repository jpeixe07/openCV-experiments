import cv2
print(cv2.__version__)
import numpy as np
while True:
    frame=np.zeros([1080,1920,3],dtype=np.uint8) #cada interseção com 3 numeros
    # para o padrão BGR BLUE/GREEN/RED
    # Se fosse apenas preto e branco não precisaria
    frame[:,:]=[0,0,255]

    frame[:,0:125]=(0,255,0) #pode ser []
    cv2.imshow('My Window',frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break


