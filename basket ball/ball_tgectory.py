import cv2
from cvzone.ColorModule import ColorFinder
import numpy as np
cap=cv2.VideoCapture('v1.mp4')
myColorFinder=ColorFinder(True)
#algo=cv2.bgsegm.createBackgroundSubtractorMOG()
#detect=[]
#counter=0
import cvzone
def rescale(frame,scale=0.5):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimension=(width,height)
    return cv2.resize(frame,dimension,interpolation=cv2.INTER_AREA)
poslist=[]

hsvVals='red'
while True:
    #ret,frame_resize=cap.read()
    #img= rescale(frame_resize)
    img= cv2.imread("img1.jpeg")
    #img= rescale(img)
    img=img[0:900,:]
    imgColor,mask=myColorFinder.update(img,hsvVals)
    #location
   # imgCountours,countours= cvzone.findContours(img,mask,minArea=150)
    #dooted points
    """if countours:
        poslist.append(countours[0]['center'])

    for pos in poslist:    
        cv2.circle(imgCountours,pos,4,(0,255,0),cv2.FILLED)"""


    #blur=cv2.GaussianBlur(grey,(3,3),5)
    img=cv2.resize(img,(0,0),None,1,1)
    cv2.imshow("Output",img)
    cv2.imshow("Image colour",imgColor)
    cv2.waitKey(50)

