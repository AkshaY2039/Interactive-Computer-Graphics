# !/usr/bin/env python

#	Assignment 5.3 - Affine Transformation - Rotation
#		- Akshay Kumar (CED15I031)

import pygame # importing pygame module for graphics and sound libraries
import sys # importing sys module for system-specific functions
import math # importing math module for mathematical functions

# defining some colors
backGroundColor = (0, 0, 0) # background color as black
green = (0, 255, 0) # green color
purple = (255, 0, 255) # purple color

# select some properties for display
screenSize = scrWidth, scrHeight = 1024, 600

# draw polygon
def drawPolygon (vertexX, vertexY, numVertex, color) :
	for i in range (numVertex) :
		pygame.draw.line (display_box, color,
								 [vertexX[i % numVertex],
								 vertexY[i % numVertex]],
								 [vertexX[(i + 1) % numVertex],
								 vertexY[(i + 1) % numVertex]], 1)
	pygame.display.update ()

# rotated
def rotated (vertexX, vertexY, numVertex, color, angle) :
	for i in range (numVertex) :
		x1 = abs (int (float (vertexX[i % numVertex]) * math.cos (angle) - float (vertexY[i % numVertex]) * math.sin (angle)))
		y1 = abs (int (float (vertexX[i % numVertex]) * math.sin (angle) + float (vertexY[i % numVertex]) * math.cos (angle)))
		x2 = abs (int (float (vertexX[(i + 1) % numVertex]) * math.cos (angle) - float (vertexY[(i + 1) % numVertex]) * math.sin (angle)))
		y2 = abs (int (float (vertexX[(i + 1) % numVertex]) * math.sin (angle) + float (vertexY[(i + 1) % numVertex]) * math.cos (angle)))
		pygame.draw.line (display_box, color, [x1, y1], [x2, y2], 1)
	pygame.display.update ()

# start here
if __name__ == '__main__' :
		# get input from command line
		numVertex = int (input ('Enter the number of vertices for your polygon : ').strip ())
		print ('The vertices will be modified into', scrWidth, 'x', scrHeight, 'quadrant')
		vertexX = list ()
		vertexY = list ()
		for i in range (numVertex) :
			print ("Vertex", i)
			temp = int (input ('X coordinate : ').strip ())
			vertexX.append (temp % scrWidth)
			temp = int (input ('Y coordinate : ').strip ())
			vertexY.append (temp & scrHeight)
		alpha = float (input ("Enter the angle of rotation : ").strip ())
		angle = math.radians (alpha % 360)

		# initialize the display box (window)
		display_box = pygame.display.set_mode (screenSize) # set size of screen
		display_box.fill (backGroundColor) # set background color of the screen
		pygame.display.update ()

		# draw the polygon
		drawPolygon (vertexX, vertexY, numVertex, green)
		# draw the polygon rotated alpa
		rotated (vertexX, vertexY, numVertex, purple, angle)

		# update display
		pygame.display.update ()

		# wait for user exit
		while 1 :
				for event in pygame.event.get () :
						if event.type == pygame.QUIT :
								sys.exit ()