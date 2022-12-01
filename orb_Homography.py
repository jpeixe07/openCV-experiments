import cv2
import numpy as np
import time
from matplotlib import pyplot as plt

#Vou estar tentando fazer o image matching de um objeto e testando a sua acuracia
#Bem como a sua viabilidade para sistemas embarcados 

width=1920 #1920,1280,320, 640
height=1080 #1080,720,180, 340
cam=cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width) 
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height) 
cam.set(cv2.CAP_PROP_FPS, 30) 
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) #moving jpg

#Loading the image
trainImage = cv2.imread('C:/Users/jpedr/Documents/Python/ImageMatching_experiments/cereal.jpg', cv2.IMREAD_GRAYSCALE) 

#Iniciating ORB Detector
orb = cv2.ORB_create(nfeatures=1000) #default is 500, i was using 1500

#finding the kp and descs of the trainImage
kp1, desc1 = orb.detectAndCompute(trainImage, None)

# using the orb detector, we pass the flann parameters as following:
FLANN_INDEX_LSH = 6
index_params= dict(algorithm = FLANN_INDEX_LSH,
                   table_number = 6, # 12
                   key_size = 12,     # 20
                   multi_probe_level = 1) #2

search_params = dict(checks=50)   # or pass empty dictionary
#Second dictionary is the SearchParams. It specifies the number of times the trees in the index should be recursively traversed. Higher values gives better precision, but also takes more time. 
# If you want to change the value, pass search_params = dict(checks=100).

flann = cv2.FlannBasedMatcher(index_params, search_params)

while True:
    ignore, frame=cam.read()

    #timer = cv2.getTickCount()

    #we are going to pass the frame in gray scale
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kp_grayframe, desc_grayframe = orb.detectAndCompute(grayframe, None)
    
    matches = flann.knnMatch(desc1, desc_grayframe, k=2) #ainda nao sei o parametro k=2

    good_points = []
    
    for i, pair in enumerate(matches): #solution when the tuple is empty
        try:
            m, n = pair
            if m.distance < 0.7*n.distance:
                good_points.append(m)
        except ValueError:
            pass

    #img3 = cv2.drawMatches(trainImage, kp1, grayframe, kp_grayframe, good_points, grayframe)

    #Homography

    if len(good_points) > 10: #10 = min_value_count

        ##these steps are required for the algorithm of homography
        query_pts = np.float32([ kp1[m.queryIdx].pt for m  in good_points]).reshape(-1,1,2)
        train_pts = np.float32([kp_grayframe[m.trainIdx].pt for m in good_points]).reshape(-1,1,2)
        
        matrix,  mask = cv2.findHomography(query_pts, train_pts, cv2.RANSAC, 5.0)
        matches_mask = mask.ravel().tolist()

        #Perspective Transform
        h, w = trainImage.shape
        pts = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts, matrix)
        
        homography = cv2.polylines(frame, [np.int32(dst)], True, (0, 0, 255), 3)
        cv2.imshow("Homography", homography)
    else:
        cv2.imshow("Homography", grayframe) #caso nao tenha match suficiente para fazer a homografia

    #cv2.putText(img3, f"{fps:.2f} FPS", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    #fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    #print(fps)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()

#OBSERVAÇÕES:
#Nao sei se o tamanho da imagem a ser treinada infere na distancia minima de detecção na mesma na webcam, se tornando inutil para o nosso uso
#Testar com o draw_utils de acordo com a documentação do openCV