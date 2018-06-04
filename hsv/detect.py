import cv2
import numpy as np


cap = cv2.VideoCapture(0)

def nothing(x):
    pass
# Creating a window for later use
cv2.namedWindow('result')
cv2.namedWindow('rest')
#cv2.namedWindow('canny')
# Creating track bar
#cv2.createTrackbar('cnl','canny',0,200,nothing)
#cv2.createTrackbar('cnu','canny',0,200,nothing)

cv2.createTrackbar('hmin', 'result',0,180,nothing)
cv2.createTrackbar('hmax', 'result',0,180,nothing)
cv2.createTrackbar('smin', 'result',0,255,nothing)
cv2.createTrackbar('smax', 'result',0,255,nothing)
cv2.createTrackbar('vmin', 'result',0,255,nothing)
cv2.createTrackbar('vmax', 'result',0,255,nothing)

cv2.createTrackbar('h', 'rest',0,180,nothing)
cv2.createTrackbar('s', 'rest',0,255,nothing)
cv2.createTrackbar('v', 'rest',0,255,nothing)


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

    h = cv2.getTrackbarPos('h','rest')
    s = cv2.getTrackbarPos('s','rest')
    v = cv2.getTrackbarPos('v','rest')


    lower_blue = np.array([h,s,v])
    upper_blue = np.array([180,255,255])

    mask = cv2.inRange(hsv,lower_blue, upper_blue)

    result1 = cv2.bitwise_and(frame,frame,mask = mask)
    

    # Normal masking algorithm
    min = np.array([hlo,slo,vlo])
    max = np.array([hup,sup,vup])

    mask = cv2.inRange(hsv,min,max)

    result = cv2.bitwise_and(frame,frame,mask = mask)
    hello=cv2.medianBlur(result,15)
    blur = cv2.GaussianBlur(result,(15,15),0)
    kernel = np.ones((5,5),np.uint8)
    erosion = cv2.erode(mask,kernel,iterations = 1)
    dilation = cv2.dilate(mask,kernel,iterations = 1)
    edges = cv2.Canny(frame,100,200)
 
    # Display edges in a frame
    cv2.imshow('Edges',edges)
   
   # cv2.imshow('Gaussian Blurring',blur)
    cv2.imshow('frame',frame)
    cv2.imshow('result',result)
   #cv2.imshow('mask',mask)
   #cv2.imshow('hsv',hsv)
    #cv2.imshow('median',hello)
    #cv2.imshow('rest',result1)
    #cv2.imshow('erosion',erosion)
    #cv2.imshow('dilation',dilation)
    k = cv2.waitKey(1)
    if k == 27:
        break


cv2.destroyAllWindows()

