import cv2 
import numpy as np
#Display a checkerboard red and black
while True:
    frame=np.zeros([799,799,3], dtype=np.uint8)
    for w in range(100,701,200):
        for i in range(100,701,200):
            frame[(w-100):w,(i-100):i]=(255,255,255) #primeira linha W, linha impar, colunas impares I  =red ou white
            frame[(w-100):w,i:(i+100)]=(0,0,0) #primeira linha, linha impar, colunas pares I  =blue OU BLACK
        for i in range(100,701,200):
            frame[w:(w+100),(i-100):i]=(0,0,0) #segunda linha W, linha par, colunas impares I =blue OU BLACK
            frame[w:(w+100),i:(i+100)]=(255,255,255) #segunda linha W, linha par, colunas pares I  =red ou white        
    cv2.imshow('Checkerboard', frame)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
