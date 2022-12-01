import cv2
#import numpy as np
print(cv2.__version__)

tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
tracker_type = tracker_types[2]

if tracker_type == 'BOOSTING':
    tracker = cv2.TrackerBoosting_create()
if tracker_type == 'MIL':
    tracker = cv2.TrackerMIL_create() 
if tracker_type == 'KCF':
    tracker = cv2.TrackerKCF_create() 
if tracker_type == 'TLD':
    tracker = cv2.TrackerTLD_create() 
if tracker_type == 'MEDIANFLOW':
    tracker = cv2.TrackerMedianFlow_create() 
if tracker_type == 'GOTURN':
    tracker = cv2.TrackerGOTURN_create()
if tracker_type == 'MOSSE':
    tracker = cv2.TrackerMOSSE_create()
if tracker_type == "CSRT":
    tracker = cv2.TrackerCSRT_create()

cam = cv2.VideoCapture(1)
width = 1280
height = 720

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)

firstFrame = True


while True:
    _, frame = cam.read()
    if firstFrame == True:
        bbox = cv2.selectROI("Tracking", frame)
        ret = tracker.init(frame, bbox)
        firstFrame = False

    timer = cv2.getTickCount()
    ret, bbox = tracker.update(frame)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    if ret:
        upperLeft = (int(bbox[0]), int(bbox[1]))
        lowerRight = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, upperLeft, lowerRight, (0,255,255), 2)
    else:
        cv2.putText(frame, "Tracking failure!!", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,0,0), 2)
    
    print(upperLeft)
    print(lowerRight)
    cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2)
    cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2)
    cv2.imshow("Tracking", frame)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release(0)
cv2.destroyAllWindows()


    
