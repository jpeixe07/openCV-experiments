import cv2
import numpy as np


#teste usando homografia e sift do pysource, copiei e colei pra testar a influencia da base de dados




width = 1920
height = 1080
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG')) #moving jpg

img = cv2.imread('C:/Users/jpedr/Documents/Python/ImageMatching_experiments/cereal.jpg', cv2.IMREAD_GRAYSCALE) 

# Features
sift = cv2.SIFT_create()
#sift = cv2.xfeatures2d.SIFT_create()
kp_image, desc_image = sift.detectAndCompute(img, None)

# Feature matching
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5) #Pesquisar a diferenca di algoritmo para 1
search_params = dict(checks = 50) ##antes tinha passado um dicionario vazio no lugar disso

flann = cv2.FlannBasedMatcher(index_params, search_params)

while True:
    _, frame = cap.read()
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # trainimage
    kp_grayframe, desc_grayframe = sift.detectAndCompute(grayframe, None)
    matches = flann.knnMatch(desc_image, desc_grayframe, k=2)
    
    good_points = []
    for i, pair in enumerate(matches): #solution when the tuple is empty
        try:
            m, n = pair
            if m.distance < 0.8*n.distance:
                good_points.append(m)
        except ValueError:
            pass
    
    # img3 = cv2.drawMatches(img, kp_image, grayframe, kp_grayframe, good_points, grayframe)
    # Homography
    if len(good_points) > 10:
        
        query_pts = np.float32([kp_image[m.queryIdx].pt for m in good_points]).reshape(-1, 1, 2)
        train_pts = np.float32([kp_grayframe[m.trainIdx].pt for m in good_points]).reshape(-1, 1, 2)
        
        matrix, mask = cv2.findHomography(query_pts, train_pts, cv2.RANSAC, 5.0)
        matches_mask = mask.ravel().tolist()
        
        # Perspective transform
        h, w = img.shape
        pts = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
        dst = cv2.perspectiveTransform(pts, matrix)
        upperLeft =  int(dst[0][0][0]), int(dst[0][0][1]) 
        lowerRight =  int(dst[2][0][0]), int(dst[2][0][1]) 
        
        print(upperLeft, lowerRight)
        homography = cv2.polylines(frame, [np.int32(dst)], True, (255, 0, 0), 3)
        cv2.imshow("Homography", homography)
    else:
        cv2.imshow("Homography", grayframe)
    # cv2.imshow("Image", img)
    # cv2.imshow("grayFrame", grayframe)
    # cv2.imshow("img3", img3)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()