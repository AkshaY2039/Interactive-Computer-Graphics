# !/usr/bin/env python

#	Assignment 4.1 - Image using inbuilt command (IIITDM Gate)
#		- Akshay Kumar (CED15I031)

import pygame # importing pygame module for graphics and sound libraries
import sys # importing sys module for system-specific functions
import math # importing math module for sine and cosine functions

# defining delay in terms of milliseconds
delay = 20

# defining some colors
black = (0, 0, 0) # black color
white = (255, 255, 255) # white color
red = (255, 0, 0) # red color
green = (0, 255, 0) # green color
blue = (0, 0, 255) # blue color
light_blue = (12, 50, 200) # light blue color
sky = (217, 235, 237) # sky color
cream = (250, 210, 188) # cream color

# select some properties for display
screenSize = scrWidth, scrHeight = 1024, 512

# draw gate function
def drawGate () :
	# roof

	# box for institute name
	pygame.draw.polygon (display_box, white, [(58, 105), (1020, 105), (1021, 125), (57, 125)])
	# Institute Name
	pygame.font.init ()
	myfont = pygame.font.SysFont ('monospace', 16, 1)
	textsurface = myfont.render ('INDIAN INSTITUTE OF INFORMATION TECHNOLOGY DESIGN AND MANUFACTURING, KANCHEEPURAM', False, (0, 0, 0))
	display_box.blit (textsurface, (138, 107))
	# update display
	pygame.display.update ()

if __name__ == '__main__' :
	print ("IIITDM Gate Drawing")

	# initialize the display box (window)
	display_box = pygame.display.set_mode (screenSize) # set size of display_box
	display_box.fill (sky) # set background color of the display_box
	surf = pygame.display.get_surface ()
	pygame.display.update ()

	# draw IIITDM Gate
	drawGate ()

while 1 :
	for event in pygame.event.get () :
		if event.type == pygame.QUIT :
			running = 0
			sys.exit ()
