import cv2

cap = cv2.VideoCapture(0)

def nothing(x):
    pass
#cv2.namedWindow('b')
#cv2.namedWindow('g')
#cv2.namedWindow('r')

while(1):

	ret,frame= cap.read()

	b = frame.copy()
# set green and red channels to 0
	b[:, :, 1] = 0
	b[:, :, 2] = 0


	g = frame.copy()
# set blue and red channels to 0
	g[:, :, 0] = 0
	g[:, :, 2] = 0

	r = frame.copy()
# set blue and green channels to 0
	r[:, :, 0] = 0
	r[:, :, 1] = 0


# RGB - Blue
	cv2.imshow('Blue color', b)

# RGB - Green
	cv2.imshow('Green color', g)

# RGB - Red
	cv2.imshow('Red color', r)

	k = cv2.waitKey(1)
    	if k == 27:
        	 break


cv2.destroyAllWindows()

