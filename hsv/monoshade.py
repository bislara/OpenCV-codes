import cv2
import numpy as np
def nothing(x):
    pass

cap = cv2.VideoCapture(0)

while(1):
	ret,im_gray = cap.read()
	im_gray1=cv2.cvtColor(im_gray,cv2.COLOR_BGR2RGB)
	im_color = cv2.applyColorMap(im_gray, cv2.COLORMAP_JET)
	im_color1 = cv2.applyColorMap(im_gray1, cv2.COLORMAP_SUMMER)
	im_color2 = cv2.applyColorMap(im_gray, cv2.COLORMAP_PINK)
	im_color3 = cv2.applyColorMap(im_gray, cv2.COLORMAP_SUMMER)
	im_color2 = cv2.applyColorMap(im_gray, cv2.COLORMAP_PINK)
#        im_color3=cv2.medianBlur(im_color3,15)
 	blur = cv2.GaussianBlur(im_color3,(15,15),0)
        kernel = np.ones((5,5),np.uint8)
        erosion = cv2.erode(blur,kernel,iterations = 1)
        im_color3 = cv2.dilate(blur,kernel,iterations = 1)


	cv2.imshow('Red color', im_color3)
	cv2.imshow('autumn',im_color1)
#	cv2.imshow('pink',im_color2)
	k = cv2.waitKey(1)
	if k == 27:
		break

cv2.destroyAllWindows()
