# !/usr/bin/env python

#	Assignment 4.2 - Dancing Skeleton
#		- Akshay Kumar (CED15I031)

import pygame # importing pygame module for graphics and sound libraries
import sys # importing sys module for system-specific functions
import math # importing math module for sine and cosine functions

# defining delay in terms of milliseconds
delay = 20

# defining some colors
backGroundColor = (0, 0, 0) # background color as black
white = (255, 255, 255) # white color
red = (255, 0, 0) # red color
green = (0, 255, 0) # green color
blue = (0, 0, 255) # blue color
light_blue = (12, 50, 200) # light blue color

# select some properties for display
screenSize = scrWidth, scrHeight = 1024, 720
originX = int (scrWidth / 2)
originY = int (scrHeight / 2)

# class stick figure
class stickFigure :
	lineWeight = 5
	rHead = 40
	rPalm = int (rHead / 5)
	rFeet = int (rHead / 4)
	neckHeight = 10
	shoulderLength = int (rHead * 1.2)
	upperArmLength = rHead * 2
	foreArmLength = rHead * 2
	torsoHeight = rHead * 3
	thighLength = rHead * 2
	calfLength = rHead * 2
	angleShoulder = -30
	angleElbow = 30
	anglePelvic = 30
	angleKnee = -30
	legGap = rFeet * 2

	# constructor
	def __init__ (self, headX, headY, color) :
		self.headX = headX
		self.headY = headY
		self.penColor = color

	# updating of Position
	def updatePosition (self, headX, headY) :
		self.headX = headX
		self.headY = headY

	# updating of Angles
	def updateAngles (self, angleShoulder, angleElbow, anglePelvic, angleKnee) :
		self.angleShoulder = angleShoulder
		self.angleElbow = angleElbow
		self.anglePelvic = anglePelvic
		self.angleKnee = angleKnee

	# fincd various coordinates for drawing
	def findCoordinates (self) :
		# neck
		self.neckX = self.headX
		self.neckY = self.headY + self.rHead + self.neckHeight
		# shoulder
		self.shoulderLeftX = self.neckX - self.shoulderLength
		self.shoulderRightX = self.neckX + self.shoulderLength
		self.shoulderY = self.neckY
		# elbow
		self.elbowLeftX = self.shoulderLeftX - int (self.upperArmLength * (math.cos (math.radians (self.angleShoulder))))
		self.elbowLeftY = self.shoulderY + int (self.upperArmLength * (math.sin (math.radians (self.angleShoulder))))
		self.elbowRightX = self.shoulderRightX + int (self.upperArmLength * (math.cos (math.radians (self.angleShoulder))))
		self.elbowRightY = self.shoulderY + int (self.upperArmLength * (math.sin (math.radians (self.angleShoulder))))
		# palm
		self.palmLeftX = self.elbowLeftX - int (self.foreArmLength * (math.cos (math.radians (self.angleElbow))))
		self.palmLeftY = self.elbowLeftY - int (self.foreArmLength * (math.sin (math.radians (self.angleElbow))))
		self.palmRightX = self.elbowRightX + int (self.foreArmLength * (math.cos (math.radians (self.angleElbow))))
		self.palmRightY = self.elbowRightY - int (self.foreArmLength * (math.sin (math.radians (self.angleElbow))))
		# pelvic
		self.pelvicLeftX = self.shoulderLeftX
		self.pelvicRightX = self.shoulderRightX
		self.pelvicY = self.shoulderY + self.torsoHeight
		# pelvic joint
		self.pelvicJointLeftX = self.neckX - self.legGap
		self.pelvicJointRightX = self.neckX + self.legGap
		# knee
		self.kneeLeftX = self.pelvicJointLeftX - int (self.thighLength * (math.cos (math.radians (self.anglePelvic))))
		self.kneeLeftY = self.pelvicY + int (self.thighLength * (math.sin (math.radians (self.anglePelvic))))
		self.kneeRightX = self.pelvicJointRightX + int (self.thighLength * (math.cos (math.radians (self.anglePelvic))))
		self.kneeRightY = self.pelvicY + int (self.thighLength * (math.sin (math.radians (self.anglePelvic))))
		# feet
		self.feetLeftX = self.kneeLeftX + int (self.calfLength * (math.cos (math.radians (self.angleKnee))))
		self.feetLeftY = self.kneeLeftY + int (self.calfLength * (math.sin (math.radians (self.angleKnee))))
		self.feetRightX = self.kneeRightX - int (self.calfLength * (math.cos (math.radians (self.angleKnee))))
		self.feetRightY = self.kneeRightY + int (self.calfLength * (math.sin (math.radians (self.angleKnee))))

	# draw stick figure using coordinates
	def draw (self) :
		# findCoordinates new values
		self.findCoordinates ()
		# head
		pygame.draw.circle (display_box, self.penColor, (self.headX, self.headY), self.rHead)
		# neck
		pygame.draw.line (display_box, self.penColor, (self.headX, self.headY), 
														(self.neckX, self.neckY), self.lineWeight)
		# shoulder
		pygame.draw.line (display_box, self.penColor, (self.shoulderLeftX, self.shoulderY), 
														(self.shoulderRightX, self.shoulderY), self.lineWeight)
		# upperArms
		pygame.draw.line (display_box, self.penColor, (self.shoulderLeftX, self.shoulderY), 
														(self.elbowLeftX, self.elbowLeftY), self.lineWeight)
		pygame.draw.line (display_box, self.penColor, (self.shoulderRightX, self.shoulderY), 
														(self.elbowRightX, self.elbowRightY), self.lineWeight)
		# foreArms
		pygame.draw.line (display_box, self.penColor, (self.elbowLeftX, self.elbowLeftY), 
														(self.palmLeftX, self.palmLeftY), self.lineWeight)
		pygame.draw.line (display_box, self.penColor, (self.elbowRightX, self.elbowRightY), 
														(self.palmRightX, self.palmRightY), self.lineWeight)
		# palm
		pygame.draw.circle (display_box, self.penColor, (self.palmLeftX, self.palmLeftY), self.rPalm)
		pygame.draw.circle (display_box, self.penColor, (self.palmRightX, self.palmRightY), self.rPalm)
		# torso
		pygame.draw.line (display_box, self.penColor, (self.pelvicRightX, self.pelvicY), 
														(self.shoulderLeftX, self.shoulderY), self.lineWeight)
		pygame.draw.line (display_box, self.penColor, (self.pelvicLeftX, self.pelvicY), 
														(self.shoulderRightX, self.shoulderY), self.lineWeight)
		pygame.draw.line (display_box, self.penColor, (self.pelvicLeftX, self.pelvicY), 
														(self.pelvicRightX, self.pelvicY), self.lineWeight)
		# thighs
		pygame.draw.line (display_box, self.penColor, (self.pelvicJointLeftX, self.pelvicY), 
														(self.kneeLeftX, self.kneeLeftY), self.lineWeight)
		pygame.draw.line (display_box, self.penColor, (self.pelvicJointRightX, self.pelvicY), 
														(self.kneeRightX, self.kneeRightY), self.lineWeight)
		# calf
		pygame.draw.line (display_box, self.penColor, (self.kneeLeftX, self.kneeLeftY), 
														(self.feetLeftX, self.feetLeftY), self.lineWeight)
		pygame.draw.line (display_box, self.penColor, (self.kneeRightX, self.kneeRightY), 
														(self.feetRightX, self.feetRightY), self.lineWeight)
		# feet
		pygame.draw.circle (display_box, self.penColor, (self.feetLeftX, self.feetLeftY), self.rFeet)
		pygame.draw.circle (display_box, self.penColor, (self.feetRightX, self.feetRightY), self.rFeet)

if __name__ == '__main__' :
	numIter = int (input ('Enter the number of times animation to repeat : ').strip ())

	# initialize the display box (window)
	display_box = pygame.display.set_mode (screenSize) # set size of screen
	display_box.fill (backGroundColor) # set background color of the screen
	pygame.display.update ()

	skeleton1 = stickFigure (int (originX / 2), int (originY / 1.5), red)
	skeleton2 = stickFigure (int (originX / 2) + originX, int (originY / 1.5), blue)

	# animation loop
	for i in range (0, numIter) :
		# animation sub loop1
		for angle11, angle12, angle21, angle22 in zip (range (80, 60, -1), range (30, 60), range (10, 60), range (110, 60, -1)) :
			# clear screen
			pygame.time.wait (delay)
			display_box.fill (backGroundColor)
			pygame.display.update ()
			skeleton1.updateAngles (angle11, angle12, angle11, angle12)
			skeleton2.updateAngles (angle21, angle22, angle21, angle22)
			skeleton1.draw ()
			skeleton2.draw ()
			# update display
			pygame.display.update ()

		# animation sub loop2
		for angle11, angle12, angle21, angle22 in zip (range (60, 10, -1), range (60, 110), range (60, 80), range (60, 30, -1)) :
			# clear screen
			pygame.time.wait (delay)
			display_box.fill (backGroundColor)
			pygame.display.update ()
			skeleton1.updateAngles (angle11, angle12, angle11, angle12)
			skeleton2.updateAngles (angle21, angle22, angle21, angle22)
			skeleton1.draw ()
			skeleton2.draw ()
			# update display
			pygame.display.update ()

		# animation reverse sub loop2
		for angle11, angle12, angle21, angle22 in zip (range (10, 60), range (100, 60, -1), range (80, 60, -1), range (30, 60)) :
			# clear screen
			pygame.time.wait (delay)
			display_box.fill (backGroundColor)
			pygame.display.update ()
			skeleton1.updateAngles (angle11, angle12, angle11, angle12)
			skeleton2.updateAngles (angle21, angle22, angle21, angle22)
			skeleton1.draw ()
			skeleton2.draw ()
			# update display
			pygame.display.update ()

		# animation reverse sub loop1
		for angle11, angle12, angle21, angle22 in zip (range (60, 80), range (60, 30, -1), range (60, 10, -1), range (60, 110)) :
			# clear screen
			pygame.time.wait (delay)
			display_box.fill (backGroundColor)
			pygame.display.update ()
			skeleton1.updateAngles (angle11, angle12, angle11, angle12)
			skeleton2.updateAngles (angle21, angle22, angle21, angle22)
			skeleton1.draw ()
			skeleton2.draw ()
			# update display
			pygame.display.update ()

	while 1 :
		for event in pygame.event.get() :
			if event.type == pygame.QUIT :
				sys.exit()
