from os import listdir
from os.path import isfile, join
from PIL import Image
import numpy as np
import cv2

RADIUS = 3
picDir = "slike/"
greyscaleDir = "slike/greyscale/"

def min(a,b):
	if a <= b:
		return a
	else:
		return b

def setResizeStep(radius,maxHeight,maxWidth):
	if maxHeight <= maxWidth:
		return float(((2*float(RADIUS))/3)/float(maxHeight))
	else:
		return float(((2*float(RADIUS))/3)/float(maxWidth))


def listFiles(mypath):
	onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
	return onlyfiles

def getMaxDimensions(picDir,files):
	maxH = 0;
	maxW = 0;
	for picture in files:
		img = cv2.imread(picDir + picture,0)
		height, width = img.shape
		if (height > maxH) :
			maxH = height 
		if (width > maxW) : 
			maxW = width


	return maxH, maxW

def neighbours(img,i,j):
	return np.delete(img[i-1:i+2,j-1:j+2].flatten(),4)

def isPeak(hood,px):
	maxEl = np.amax(hood) 
	minEl = np.amin(hood)

	if (px > maxEl):
		return True
	elif (px < minEl):
		return True
	else:
		return False

 
fajli = listFiles(picDir)
resizeStep = 0.01
print resizeStep


#for slika in fajli:
#	img = cv2.imread(picDir + slika,0)
#	height, width = img.shape
#	mean = np.average(img)
#	newimage = np.zeros((maxHeight,maxWidth))
#	newimage[0:height,0:width] = img
#	newimage[height:maxHeight,::] = mean
#	newimage[::,width:maxWidth] = mean
#	cv2.imwrite(greyscaleDir + slika ,newimage)

peaksResolutions = []

preparedPics = listFiles(greyscaleDir)
maxHeight, maxWidth = getMaxDimensions(greyscaleDir,preparedPics)
print preparedPics
for slika in preparedPics:
	f = open('peaks' + slika.rstrip('.jpg') + '.txt', 'w')
	img = cv2.imread(greyscaleDir + slika,0)
	v = float(1)
	while (min(maxWidth,maxHeight)*v > 3*RADIUS):
		peakCounter = 0
		resizedimg = cv2.resize(img,None, fx=v, fy=v)
		#resizedimg = cv2.resize(resizedimg,None, fx=(1/v), fy=(1/v))
		imgHeight, imgWidth = resizedimg.shape
		for i in range(1,imgHeight-1):
			for j in range(1,imgWidth-1):
				px = resizedimg[i,j]
				hood  = neighbours(resizedimg,i,j) 
				if isPeak(hood,px):
					peakCounter+=1
		
		peaksResolutions.append([v, peakCounter])			
		s = str(slika) + ";" + str(v) + ";" + str(peakCounter) + "\n"
		f.write(s)
		cv2.imwrite("slike/resolutions/" + str(v) +  slika ,resizedimg)
		v = v-resizeStep

f.close()


resolucije = open("peaks.txt",'r')
for line in resolucije:
    print line,

