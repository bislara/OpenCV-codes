import cv2
import numpy as np


cap = cv2.VideoCapture(0)

def nothing(x):
    pass
# Creating a window for later use
cv2.namedWindow('result')

# Creating track bar
cv2.createTrackbar('hmin', 'result',0,180,nothing)
cv2.createTrackbar('hmax', 'result',0,180,nothing)
cv2.createTrackbar('smin', 'result',0,255,nothing)
cv2.createTrackbar('smax', 'result',0,255,nothing)
cv2.createTrackbar('vmin', 'result',0,255,nothing)
cv2.createTrackbar('vmax', 'result',0,255,nothing)


while(1):

    ret, frame = cap.read()
 #converting to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # get info from track bar and appy to result
    hlo = cv2.getTrackbarPos('hmin','result')
    hup = cv2.getTrackbarPos('hmax','result')
    slo = cv2.getTrackbarPos('smin','result')
    sup = cv2.getTrackbarPos('smax','result')
    vlo = cv2.getTrackbarPos('vmin','result')
    vup = cv2.getTrackbarPos('vmax','result')


    # Normal masking algorithm
    min = np.array([hlo,slo,vlo])
    max = np.array([hup,sup,vup])

    mask = cv2.inRange(hsv,min,max)

    result = cv2.bitwise_and(frame,frame,mask = mask)
    cv2.imshow('frame',frame)
    cv2.imshow('result',result)
    cv2.imshow('mask',mask)
    cv2.imshow('hsv',hsv)
    k = cv2.waitKey(1)
    if k == 27:
	 break


cv2.destroyAllWindows()

