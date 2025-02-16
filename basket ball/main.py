import cv2
from cvzone.ColorModule import ColorFinder
import numpy as np
cap=cv2.VideoCapture('video.mp4')
myColorFinder=ColorFinder(False)
import cvzone
def rescale(frame,scale=1):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimension=(width,height)
    return cv2.resize(frame,dimension,interpolation=cv2.INTER_AREA)
poslist=[]

hsvVals={'hmin': 0, 'smin': 144, 'vmin': 115, 'hmax': 6, 'smax': 255, 'vmax': 172}
while True:
    ret,frame_resize=cap.read()
    img= rescale(frame_resize)
    
    img=img[0:900,:]
    imgColor,mask=myColorFinder.update(img,hsvVals)
   
    imgCountours,countours= cvzone.findContours(img,mask,minArea=150)

    if countours:
        poslist.append(countours[0]['center'])

    for pos in poslist:
        cv2.circle(imgCountours,pos,5,(0,0,255),cv2.FILLED)
        print(pos)
        #After touching the Ring
        if pos>=[1100,650]:
            poslist=[]
            continue

    imgColor=cv2.resize(imgColor,(0,0),None,1,1)
    cv2.imshow("Image colour",imgCountours)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

