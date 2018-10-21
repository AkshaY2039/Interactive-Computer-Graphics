# !/usr/bin/env python

#	Assignment 3.2 - Koch Curve - SnowFlake
#			Parameters for Koch Curve : 
#				1.	start point  (startX, startY)
#				2.	end point  (endX, endY)
#				3.	number of iterations  (numIter)
#		- Akshay Kumar  (CED15I031)

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
originX = scrWidth / 2
originY = scrHeight / 2
length = 150

# Koch Snoflake Curve Fucntion
#				a						b						c
#   |----------------------|----------------------|----------------------|
#  (startX,startY)	    (x1, y1)		    	(x2, y2)		  (endX, endY)
def kochSnowFlakeCurve (startX, startY, length, alpha, numIter) :
	# calculate endX, endY from length and angle
	endX = startX + length * math.cos (math.radians (alpha))
	endY = startY + length * math.sin (math.radians (alpha))

	if numIter > 0 :
		# point x1, y1 to fix
		x1 = startX +  (length/3) * math.cos (math.radians (alpha))
		y1 = startY +  (length/3) * math.sin (math.radians (alpha))
		# point x2, y2 to fix
		x2 = startX + 2 *  (length/3) * math.cos (math.radians (alpha))
		y2 = startY + 2 *  (length/3) * math.sin (math.radians (alpha))
		# tip of equilateral triangle out of section C
		triTipX = x1 +  (length/3)* (math.cos (math.radians (alpha + 60)))
		triTipY = y1 +  (length/3)* (math.sin (math.radians (alpha + 60)))
		# draw section a
		kochSnowFlakeCurve (startX, startY, length/3, alpha, numIter - 1)
		# draw section c
		kochSnowFlakeCurve (x2, y2, length / 3, alpha, numIter - 1)
		# draw triangle out of section b
		kochSnowFlakeCurve (x1, y1, length / 3, alpha + 60, numIter - 1)
		kochSnowFlakeCurve (triTipX, triTipY, length / 3, alpha - 60, numIter - 1)
	else :
		pygame.draw.line (display_box, blue, [startX, startY], [endX, endY], 1)
		pygame.display.update ()

def kochSnowFlake (numIter) :
	# define local origin
	orX = originX - int (length * math.cos (math.radians (60)))
	orY = originY - int ((length / 3) * math.sin (math.radians (60)))
	# draw first edge from origin 
	kochSnowFlakeCurve (orX, orY, length, 60, numIter)
	# update strting point for second edge
	orX += length * math.cos (math.radians (60))
	orY += length * math.sin (math.radians (60))
	kochSnowFlakeCurve (orX, orY, length, -60, numIter)
	# update starting point for third edge
	orX += length * math.cos (math.radians (-60))
	orY += length * math.sin (math.radians (-60))
	kochSnowFlakeCurve (orX, orY, length, 180, numIter)

# start here
if __name__ == '__main__' :
	# get input from command line
	numIter = int (input ('Enter the number of iterations to undergo: ').strip ())

	# initialize the display box (window)
	display_box = pygame.display.set_mode (screenSize) # set size of screen
	display_box.fill (backGroundColor) # set background color of the screen
	pygame.display.update ()

	# draw origin
	pygame.draw.line (display_box, green, [originX, originY], [originX, originY], 1)
	pygame.display.update ()
	pygame.time.delay (delay)

	# draw koch curve
	kochSnowFlake (numIter)

	# update display
	pygame.display.update ()

	# wait for user exit
	while 1 :
		for event in pygame.event.get () :
			if event.type == pygame.QUIT :
				sys.exit ()

