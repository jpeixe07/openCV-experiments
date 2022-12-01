import cv2
print(cv2.__version__)
import numpy as np

boardSize=int(input("What Size is Your Board? "))
numSquares=int(input('How many squares? '))
squareSize=int(boardSize/numSquares)
darkColor=(255,255,255)
lightColor=(0,0,0)
nowColor=darkColor


while True:
    x=np.zeros([boardSize,boardSize,3], dtype=np.uint8)
    for row in range(0,numSquares):
        for column in range(0,numSquares):
            x[squareSize*row:squareSize*(row+1),squareSize*column:squareSize*(column+1)]=nowColor
            if nowColor==darkColor:
                nowColor=lightColor
            else:
                nowColor=darkColor
        if nowColor==darkColor:
            nowColor=lightColor
        else:
            nowColor=darkColor
    cv2.imshow('Checkerboard', x)    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
