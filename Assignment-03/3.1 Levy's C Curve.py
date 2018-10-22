# !/usr/bin/env python

#	Assignment 3.1 - Levy's C Curve
#			Parameters for Levy's C Curve : 
#				1.	starting point (startX, startY)
#				2.	length of line (length)
#				3.	number of iterations (numIter)
#				4.	angle with x axis (alpha)
#		- Akshay Kumar (CED15I031)

import pygame # importing pygame module for graphics and sound libraries
import sys # importing sys module for system-specific functions
import math # importing math module for sine and cosine functions

# defining delay in terms of milliseconds
delay = 10

# defining some colors
backGroundColor = (0, 0, 0) # background color as black
white = (255, 255, 255) # white color
red = (255, 0, 0) # red color
green = (0, 255, 0) # green color
blue = (0, 0, 255) # blue color

# select some properties for display
screenSize = scrWidth, scrHeight = 1024, 720
originX = int (scrWidth / 2)
originY = int (scrHeight / 2)

# Levy's C Curve function
def levy_C_Curve (startX, startY, length, alpha, numIter) :
	if numIter > 0 :
		length = float (length / math.sqrt (2))
		levy_C_Curve (startX, startY, length, alpha + 45, numIter - 1)
		levy_C_Curve ((startX + length * math.cos (math.radians (45 + alpha))),
						 (startY + length * math.sin (math.radians (45 + alpha))),
						 length, alpha - 45, numIter - 1)
	else :
		endX = int (startX + (length * math.cos (math.radians (alpha))))
		endY = int (startY + (length * math.sin (math.radians (alpha))))
		pygame.draw.line (display_box, red, [startX, startY], [endX, endY], 1)
		pygame.display.update ()

# start here
if __name__ == '__main__' :
	# taking inputs from command line
	startX = int (input ('Enter the start point of curve (x) : ').strip ())
	startY = int (input ('Enter the start point of curve (y) : ').strip ())
	length = int (input ('Enter the length of the line : ').strip ())
	alpha = int (input ('Enter the angle with the x axis (in degrees) : ').strip ())
	numIter = int (input ('Enter the number of iterations to undergo : ').strip ())

	# initialize the display box (window)
	display_box = pygame.display.set_mode (screenSize) # set size of screen
	display_box.fill (backGroundColor) # set background color of the screen
	pygame.display.update ()

	# draw origin
	pygame.draw.line (display_box, green, [originX, originY], [originX, originY], 1)
	pygame.display.update ()
	pygame.time.delay (delay)

	# normalize startX and startY
	startX += originX
	startY += originY

	# draw the c curve
	levy_C_Curve (startX, startY, length, alpha, numIter)

	# update display
	pygame.display.update ()

	# wait for user exit
	while 1 :
		for event in pygame.event.get () :
			if event.type == pygame.QUIT :
				sys.exit ()
