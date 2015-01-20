import numpy as np
import cv2
import subprocess
import random
import math
from decimal import *


class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def substractAbs(Point1,Point2):
	    x_new = abs(int(Point2.x) - int(Point1.x))
	    y_new = abs(int(Point2.y) - int(Point1.y))
	    return Point(x_new,y_new)

	def distanceBetweenPoints(Point1,Point2):
		return float(math.sqrt(math.pow(Point1.getX() - Point2.getX(),2) + math.pow(Point1.getY() - Point2.getY(),2)))
	
	def printPoint(self):
		print "(" + str(self.x)  + "," + str(self.y) + ")"

	def movePoint(self,moveX,moveY):
		self.x= int(self.x) + int(moveX)
		self.y =int(self.y) + int(moveY)

	def getX(self):
		return float(self.x)

	def getY(self):
		return float(self.y) 

	def setX(self,x):
		self.x = x

	def setY(self,y):
		self.y = y 

class FacialFeatures:
	def __init__(self,listOfFeatures,filename):
		self.listOfFeatures = listOfFeatures
		self.filename = filename

	def printFeatures(self):
		for point in self.listOfFeatures:
			point.printPoint()

	def getFeatures(self):
		return self.listOfFeatures

	def getFilename(self):
		return self.filename

	def getWidthLeftRightTemple(self):
		return Point.distanceBetweenPoints(self.getLeftTempleLocation(),self.getRightTempleLocation())

	def getOuterEyeWidth(self):
		return Point.distanceBetweenPoints(self.getOuterCornerOfRightEyeLocation(),self.getOuterCornerOfLeftEyeLocation())

	def getInnerEyeWidth(self):
		return Point.distanceBetweenPoints(self.getInnerCornerOfLeftEyeLocation(),self.getInnerCornerOfRightEyeLocation())

	def getLeftEyeWidth(self):
		return Point.distanceBetweenPoints(self.getInnerCornerOfLeftEyeLocation(),self.getOuterCornerOfLeftEyeLocation())
	
	def getRightEyeWidth(self):
		return Point.distanceBetweenPoints(self.getInnerCornerOfRightEyeLocation(),self.self.getOuterCornerOfRightEyeLocation())
	
	def getWidthBetweenPupils(self):
		return Point.distanceBetweenPoints(self.getLeftEyePupilLocation(),self.self.getRightEyePupilLocation())

	def getRightEyePupilLocation(self):
		return self.listOfFeatures[0]
	
	def getLeftEyePupilLocation(self):
		return self.listOfFeatures[1]

	def getRightMouthCornerLocation(self):
		return self.listOfFeatures[2]

	def getLeftMouthCornerLocation(self):
		return self.listOfFeatures[3]

	def getOuterEndOfRightEyeBrowLocation(self):
		return self.listOfFeatures[4]

	def getInnerEndOfRightEyeBrowLocation(self):
		return self.listOfFeatures[5]

	def getInnerEndOfLeftEyeBrowLocation(self):
		return self.listOfFeatures[6]

	def getOuterEndOfLeftEyeBrowLocation(self):
		return self.listOfFeatures[7]

	def getRightTempleLocation(self):
		return self.listOfFeatures[8]

	def getOuterCornerOfRightEyeLocation(self):
		return self.listOfFeatures[9]

	def getInnerCornerOfRightEyeLocation(self):
		return self.listOfFeatures[10]

	def getInnerCornerOfLeftEyeLocation(self):
		return self.listOfFeatures[11]

	def getOuterCornerOfLeftEyeLocation(self):
		return self.listOfFeatures[12]
	
	def getLeftTempleLocation(self):
		return self.listOfFeatures[13]

	def getTipOfNoseLocation(self):
		return self.listOfFeatures[14]

	def getRightNostrilLocation(self):
		return self.listOfFeatures[15]

	def getLeftNostrilLocation(self):
		return self.listOfFeatures[16]

	def getCentrePointOnOuterEdgeOfUpperLipLocation(self):
		return self.listOfFeatures[17]


	def getCentrePointOnOuterEdgeOfLowerLipLocation(self):
		return self.listOfFeatures[18]

	def getTipOfChinLocation(self):
		return self.listOfFeatures[19]

	def getCenterBetweenEyesLocation(self):
		return Point( (self.getLeftEyePupilLocation().getX() + self.getRightEyePupilLocation().getX()) / 2 , (self.getLeftEyePupilLocation().getY() + self.getRightEyePupilLocation().getY()) / 2 )  


	
	def moveFeatures(self,moveX,moveY):
		for point in self.listOfFeatures:
			point.movePoint(moveX,moveY)

	def rotateFeatures(self,angle):
		for point in self.listOfFeatures:
			point.setX(point.getX()*math.cos(angle) - (point.getY()*math.sin(angle)))
			point.setY(point.getX()*math.sin(angle) + (point.getY()*math.cos(angle)))

	def getFaceRotation(self):
		rotation_vector = np.array([self.getRightEyePupilLocation().getX() - self.getLeftEyePupilLocation().getX(),self.getRightEyePupilLocation().getY() - self.getLeftEyePupilLocation().getY()])
		rotation_vector = rotation_vector /  np.linalg.norm(rotation_vector)
		#print "rot vektor: " + str(rotation_vector)	
		sign = 1
		if (rotation_vector[1] < 0):
			sign = -1 
		return sign*math.acos(np.dot(rotation_vector,np.array([-1,0])))


	def getCenterBetweenEyes(self):
		rotation_vector = np.array([self.getRightEyePupilLocation().getX() - self.getLeftEyePupilLocation().getX(),self.getRightEyePupilLocation().getY() - self.getLeftEyePupilLocation().getY()])
		return rotation_vector/2

	def proportion_width_between_pupils_vs_temples_width(self):
		return Point.distanceBetweenPoints(self.getRightEyePupilLocation(),self.getLeftEyePupilLocation()) / Point.distanceBetweenPoints(self.getRightTempleLocation(),self.getLeftTempleLocation())

	def proportion_width_between_temples_vs_centerBetweenEyes_to_chin(self):
		return Point.distanceBetweenPoints(self.getLeftTempleLocation(),self.getRightTempleLocation()) / Point.distanceBetweenPoints(self.getCenterBetweenEyesLocation(),self.getTipOfChinLocation())

	def proportion_width_between_pupils_vs_lips_width(self):
		return Point.distanceBetweenPoints(self.getLeftEyePupilLocation(),self.getRightEyePupilLocation()) / Point.distanceBetweenPoints(self.getLeftMouthCornerLocation(),self.getRightMouthCornerLocation())

	def proportion_width_between_outerEyesCorners_vs_lips_width(self):
		return Point.distanceBetweenPoints(self.getOuterCornerOfLeftEyeLocation(),self.getOuterCornerOfRightEyeLocation()) / Point.distanceBetweenPoints(self.getLeftMouthCornerLocation(),self.getRightMouthCornerLocation())

	def proportion_width_between_outerEyebrows_vs_temples(self):
		return Point.distanceBetweenPoints(self.getOuterEndOfLeftEyeBrowLocation(),self.getOuterEndOfRightEyeBrowLocation()) / Point.distanceBetweenPoints(self.getLeftTempleLocation(),self.getRightTempleLocation())

	def proportion_width_between_innerEyebrows_vs_temples(self):
		return Point.distanceBetweenPoints(self.getInnerEndOfLeftEyeBrowLocation(),self.getInnerEndOfRightEyeBrowLocation()) / Point.distanceBetweenPoints(self.getLeftTempleLocation(),self.getRightTempleLocation())

	def proportion_width_betweenPupils_vs_distance_tipOfNose_to_chin(self):
		return Point.distanceBetweenPoints(self.getLeftEyePupilLocation(),self.getRightEyePupilLocation()) / Point.distanceBetweenPoints(self.getTipOfNoseLocation(),self.getTipOfChinLocation())

	def proportion_width_centerEyesToChin_vs_noseToChin(self):
		return Point.distanceBetweenPoints(self.getCenterBetweenEyesLocation(),self.getTipOfChinLocation()) / Point.distanceBetweenPoints(self.getTipOfNoseLocation(),self.getTipOfChinLocation())





def normalizeFloatArray(array):
	sum = 0
	for el in array:
		sum += el
	length = math.sqrt(sum)
	
	array[:] = [round(x / length,3) for x in array]

	return array	




CENTERX = 1000
CENTERY = 600

subprocess.call("./listFiles.sh", shell=True)
files = [line.strip() for line in open("files.list")]
faces = []
for file in files:
	filename = file[:-4]
	print filename
	img = cv2.imread(filename + ".jpg")
	lines = [line.strip() for line in open(filename + ".log")]
	facialFeatures = []
	for i in range(7,27):
		x = lines[i].split()[0]

		y = lines[i].split()[1]
		facialFeatures.append(Point(x,y))
		cv2.circle(img,(int(x),int(y)), 2, (0,0,255), -1)	


	ff = FacialFeatures(facialFeatures,filename)
	faces.append(ff)
	#cv2.imshow('image',img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()

pictureProportionsArray = []
for face in faces:
	face.moveFeatures(CENTERX-int(face.getLeftEyePupilLocation().getX()),CENTERY-int(face.getLeftEyePupilLocation().getY()))


for znacilnice in faces:
	proportionVector = []
	#print float(math.degrees(znacilnice.getFaceRotation()))	
	znacilnice.rotateFeatures(znacilnice.getFaceRotation())
	znacilnice.moveFeatures(CENTERX-int(znacilnice.getLeftEyePupilLocation().getX()),CENTERY-int(znacilnice.getLeftEyePupilLocation().getY()))
	proportionVector.append(znacilnice.getFilename())
	proportionVector.append(znacilnice.proportion_width_between_pupils_vs_temples_width())
	proportionVector.append(znacilnice.proportion_width_between_innerEyebrows_vs_temples())
	proportionVector.append(znacilnice.proportion_width_between_outerEyebrows_vs_temples())
	proportionVector.append(znacilnice.proportion_width_between_pupils_vs_lips_width())
	proportionVector.append(znacilnice.proportion_width_between_outerEyesCorners_vs_lips_width())
	#proportionVector.append(znacilnice.proportion_width_centerEyesToChin_vs_noseToChin())
	proportionVector.append(znacilnice.proportion_width_between_temples_vs_centerBetweenEyes_to_chin())
	proportionVector.append(znacilnice.proportion_width_betweenPupils_vs_distance_tipOfNose_to_chin())
	#proportionVector = normalizeFloatArray(proportionVector)
	pictureProportionsArray.append(proportionVector)
	znacilnica = znacilnice.getFeatures()
	slika = np.zeros((2000,2000,3), np.uint8)
	random_r = random.randint(0,255)
	random_g = random.randint(0,255)
	random_b = random.randint(0,255)
	for point in znacilnica:
		cv2.circle(slika,(int(point.getX()),int(point.getY())),2,(random_r,random_g,random_b),-1)
	

	#cv2.imshow('slika',slika)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()




f = open('znacilnice.txt', 'w')
for znacilniceSlike in pictureProportionsArray:
	s = str(znacilniceSlike) + "\n"
	f.write(s)
f.close()


