# !/usr/bin/env python

#	Lab Exam 15 Nov 2018
#	Program 1.	Using any language, draw 100 non intersecting disjoint circles.
#		- Akshay Kumar (CED15I031)

import pygame # importing pygame module for graphics and sound libraries
import sys # importing sys module for system-specific functions
import math # importing math module for sine and cosine functions
import random # importing random module to generate random numbers

# defining delay in terms of milliseconds
delay = 20

# defining some colors
backGroundColor = (255, 255, 255) # white color

# select some properties for display
screenSize = scrWidth, scrHeight = 700, 700
radius = int (math.sqrt (scrWidth * scrHeight / 400))

# screen update
def screenUpdate () :
	pygame.time.wait (delay)
	pygame.display.update ()

# draw 100 Circles function
def drawCircles () :
	for x in range (radius, scrWidth, 2*radius) :
		for y in range (radius, scrHeight, 2*radius) :
			pygame.draw.circle (display_box, ((x*x)%255, (y*y)%255, (x+y)%255), (x, y), radius-5, 2)
	screenUpdate ()
	
if __name__ == '__main__' :
	# initialize the display box (window)
	display_box = pygame.display.set_mode (screenSize) # set size of display_box
	display_box.fill (backGroundColor) # set background color of the display_box
	pygame.display.update ()

	# draw 100 circles
	drawCircles ()

while 1 :
	for event in pygame.event.get () :
		if event.type == pygame.QUIT :
			running = 0
			sys.exit ()
