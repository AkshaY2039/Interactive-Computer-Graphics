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
originX = scrWidth / 2
originY = scrHeight / 2

# initialize the display box (window)
display_box = pygame.display.set_mode (screenSize) # set size of screen
display_box.fill (backGroundColor) # set background color of the screen
pygame.display.update ()

# class stick figure
class stickFigure :
	penColor = light_blue
	lineWeight = 2
	rHead = 20
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

	def __init__ (self, headX, headY) :
		self.headX = headX
		self.headY = headY

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
		self.elbowLeftX = self.shoulderLeftX + int (self.upperArmLength * (math.cos (math.radians (180 - self.angleShoulder))))
		self.elbowLeftY = self.shoulderY + int (self.upperArmLength * (math.sin (math.radians (180 - self.angleShoulder))))
		self.elbowRightX = self.shoulderRightX + int (self.upperArmLength * (math.cos (math.radians (self.angleShoulder))))
		self.elbowRightY = self.shoulderY + int (self.upperArmLength * (math.sin (math.radians (self.angleShoulder))))
		# palm
		self.palmLeftX = self.elbowLeftX + int (self.foreArmLength * (math.cos (math.radians (90 - self.angleElbow))))
		self.palmLeftY = self.elbowLeftY + int (self.foreArmLength * (math.sin (math.radians (90 - self.angleElbow))))
		self.palmRightX = self.elbowRightX + int (self.foreArmLength * (math.cos (math.radians (270 - self.angleElbow))))
		self.palmRightY = self.elbowRightY + int (self.foreArmLength * (math.sin (math.radians (270 - self.angleElbow))))
		# pelvic
		self.pelvicLeftX = self.shoulderLeftX
		self.pelvicRightX = self.shoulderRightX
		self.pelvicY = self.shoulderY + self.torsoHeight
		# pelvic joint
		self.pelvicJointLeftX = self.neckX - self.legGap
		self.pelvicJointRightX = self.neckX + self.legGap
		# knee
		self.kneeLeftX = self.pelvicJointLeftX + int (self.thighLength * (math.cos (math.radians (self.anglePelvic))))
		self.kneeLeftY = self.pelvicY + int (self.thighLength * (math.sin (math.radians (self.anglePelvic))))
		self.kneeRightX = self.pelvicJointRightX + int (self.thighLength * (math.cos (math.radians (180 + self.anglePelvic))))
		self.kneeRightY = self.pelvicY + int (self.thighLength * (math.sin (math.radians (180 + self.anglePelvic))))
		# feet
		self.feetLeftX = self.kneeLeftX + int (self.calfLength * (math.cos (math.radians (90 + self.angleKnee))))
		self.feetLeftY = self.kneeLeftY + int (self.calfLength * (math.sin (math.radians (90 + self.angleKnee))))
		self.feetRightX = self.kneeRightX + int (self.calfLength * (math.cos (math.radians (270 + self.angleKnee))))
		self.feetRightY = self.kneeRightY + int (self.calfLength * (math.sin (math.radians (270 + self.angleKnee))))

	# draw stick figure using coordinates
	def draw (self) :
		# clear screen
		display_box.fill (backGroundColor)
		pygame.display.update ()
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
		# update display
		pygame.display.update ()

if __name__ == '__main__' :
	skeleton = stickFigure (int (originX / 2), int (originY / 2))

	# do the hands
	for i in range (30, 60) :
		pygame.time.wait (delay)
		skeleton.updateAngles (-i, i, i, -i)
		skeleton.draw ()
	for i in range (60, 30, -1) :
		pygame.time.wait (delay)
		skeleton.updateAngles (-i, i, i, -i)
		skeleton.draw ()
	for i, j in zip (range (30, 0, -1), range (30, 60)) :
		pygame.time.wait (delay)
		skeleton.updateAngles (-i, j, i, -j)
		skeleton.draw ()
		
	# 300, 70
	for j in range (1) :
		for i in range (300, 250, -1) :
			pygame.time.wait (delay)
			skeleton.updatePosition (i, 100)
			skeleton.draw ()
		for i in range (250, 350) :
			pygame.time.wait (delay)
			skeleton.updatePosition (i, 100)
			skeleton.draw ()
		for i in range (350, 250, -1) :
			pygame.time.wait (delay)
			skeleton.updatePosition (i, 100)
			skeleton.draw ()

	# jump
	for j in range (1) :
		for i in range (100, 70, -1) :
			pygame.time.wait (delay)
			skeleton.updatePosition (250, i)
			skeleton.draw ()
		for i in range (70, 100) :
			pygame.time.wait (delay)
			skeleton.updatePosition (250, i)
			skeleton.draw ()

	# do the hands again
	for i in range (30, 60) :
		pygame.time.wait (delay)
		skeleton.updateAngles (-i, i, i, -i)
		skeleton.draw ()
	for i in range (60, 30, -1) :
		pygame.time.wait (delay)
		skeleton.updateAngles (-i, i, i, -i)
		skeleton.draw ()
	for i, j in zip (range (30, 0, -1), range (30, 60)) :
		pygame.time.wait (delay)
		skeleton.updateAngles (-i, j, i, -j,)
		skeleton.draw ()


	while 1 :
		for event in pygame.event.get() :
			if event.type == pygame.QUIT :
				sys.exit()
