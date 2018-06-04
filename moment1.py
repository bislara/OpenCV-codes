import cv2
import numpy as np


cap = cv2.VideoCapture(0)
kernel=np.ones((5,5),np.uint8)
def nothing(x):
    pass
cv2.namedWindow('result')
cv2.createTrackbar('hmin', 'result',0,180,nothing)
cv2.createTrackbar('hmax', 'result',0,180,nothing)
cv2.createTrackbar('smin', 'result',0,255,nothing)
cv2.createTrackbar('smax', 'result',0,255,nothing)
cv2.createTrackbar('vmin', 'result',0,255,nothing)
cv2.createTrackbar('vmax', 'result',0,255,nothing)

while(1):
	k = cv2.waitKey(1)
        if k == 27:
                break

	ret,frame=cap.read()	
	#blur = cv2.GaussianBlur(frame,(15,15),0)		
	blur=cv2.GaussianBlur(frame,(15,15),0)
	hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)
	hlo = cv2.getTrackbarPos('hmin','result')
        hup = cv2.getTrackbarPos('hmax','result')
        slo = cv2.getTrackbarPos('smin','result')
        sup = cv2.getTrackbarPos('smax','result')
        vlo = cv2.getTrackbarPos('vmin','result')
        vup = cv2.getTrackbarPos('vmax','result')
        min = np.array([hlo,slo,vlo])
        max = np.array([hup,sup,vup])

        mask = cv2.inRange(hsv,min,max)

        #result = cv2.bitwise_and(frame,frame,mask = mask)
        #hello=cv2.medianBlur(frame,15)
        results=cv2.medianBlur(mask,15)
	closing=cv2.morphologyEx(results,cv2.MORPH_CLOSE,kernel)
	erode=cv2.erode(closing,kernel,iterations=1)
	erode1=cv2.medianBlur(erode,15)
	_,contours,_=cv2.findContours(erode1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	cnt=0
	for contour in contours:
		area=cv2.contourArea(contour)
		if area>2000:
			
			cnt=contour
	if len(contours)==0:
		continue
	cv2.drawContours(frame,[cnt],-1,(0,255,0),6)

	M=cv2.moments(cnt)
	if int(M['m00'])==0:
		continue
	cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
	#cv2.drawContours(frame,contours , -1, (0, 0, 255), 6)

	cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
	cv2.putText(frame, "center", (cx - 20, cy - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
	#edges = cv2.Canny(frame,100,200)
	#cv2.imshow('Edges',edges)
	#cv2.imshow("Image", hello)
	
	cv2.imshow("Results",results)
	cv2.imshow("frame",frame)
        


cv2.destroyAllWindows()

