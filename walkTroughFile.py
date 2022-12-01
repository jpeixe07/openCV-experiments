import os
import cv2
import face_recognition as FR
print(cv2.__version__)

imageDir='C:\\Users\\jpedr\\Documents\\Python\\demoImages\\known'
for root,dirs,files in os.walk(imageDir):
    print('My Working Folder (root): ',root)
    print('Dirs in root: ',dirs)
    print('My files in root', files)
    for file in files:
        print('Your guy is ',file)
        fullFilePath=os.path.join(root,file)
        print(fullFilePath)
        name=os.path.splitext(file)[0]
        print(name)
        myPicture=FR.load_image_file(fullFilePath)
        myPicture=cv2.cvtColor(myPicture,cv2.COLOR_RGB2BGR)
        cv2.imshow(name,myPicture)
        cv2.moveWindow(name,0,0)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()

    