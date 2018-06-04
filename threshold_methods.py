# import the necessary packages
import argparse
import cv2
 
def nothing(x):
        pass

cv2.namedWindow('scale')
cv2.createTrackbar("track","scale",0,255,nothing)
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image to be thresholded")
ap.add_argument("-t", "--threshold", type = int, default = 128,
	help = "Threshold value")
args = vars(ap.parse_args())
 
# load the image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# initialize the list of threshold methods
methods = [
	("THRESH_BINARY", cv2.THRESH_BINARY),
	("THRESH_BINARY_INV", cv2.THRESH_BINARY_INV),
	("THRESH_TRUNC", cv2.THRESH_TRUNC),
	("THRESH_TOZERO", cv2.THRESH_TOZERO),
	("THRESH_TOZERO_INV", cv2.THRESH_TOZERO_INV)]
 
# loop over the threshold methods
#for (threshName, threshMethod) in methods:
	# threshold the image and show it
cap=cv2.VideoCapture(0)

while 1: 
	k=cv2.waitKey(1)
	y=cv2.getTrackbarPos("track","scale")
	ret,image=cap.read()
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	(T, thresh) = cv2.threshold(gray,y, 255,cv2.THRESH_BINARY)
	cv2.imshow("track", thresh)
	#cv2.waitKey(0)
