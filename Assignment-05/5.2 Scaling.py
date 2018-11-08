# !/usr/bin/env python

#	Assignment 5.2 - Affine Transformation - Scaling
#		- Akshay Kumar (CED15I031)

import pygame # importing pygame module for graphics and sound libraries
import sys # importing sys module for system-specific functions

# defining some colors
backGroundColor = (0, 0, 0) # background color as black
white = (255, 255, 255) # white color
red = (255, 0, 0) # red color
green = (0, 255, 0) # green color
blue = (0, 0, 255) # blue color
purple = (255, 0, 255) # purple color

# select some properties for display
screenSize = scrWidth, scrHeight = 1024, 512

# draw polygon
def drawPolygon (vertexX, vertexY, numVertex, color) :
	for i in range (numVertex) :
		pygame.draw.line (display_box, color, [vertexX[i % numVertex], vertexY[i % numVertex]], [vertexX[(i + 1) % numVertex], vertexY[(i + 1) % numVertex]], 1)
	pygame.display.update ()

# scaled
def scaled (vertexX, vertexY, numVertex, color, scaleX, scaleY) :
	for i in range (numVertex) :
		pygame.draw.line (display_box, color, [vertexX[i % numVertex] * scaleX, vertexY[i % numVertex] * scaleY], [vertexX[(i + 1) % numVertex] * scaleX, vertexY[(i + 1) % numVertex] * scaleY], 1)
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
			vertexX.append (temp)
			temp = int (input ('Y coordinate : ').strip ())
			vertexY.append (temp)
		scaleX = int (input ('Enter the translation along X : ').strip ())
		scaleY = int (input ('Enter the translation along Y : ').strip ())

		# initialize the display box (window)
		display_box = pygame.display.set_mode (screenSize) # set size of screen
		display_box.fill (backGroundColor) # set background color of the screen
		pygame.display.update ()

		# draw the polygon
		drawPolygon (vertexX, vertexY, numVertex, green)
		# draw the polygon scaled X
		scaled (vertexX, vertexY, numVertex, red, scaleX, 1)
		# draw the polygon scaled Y
		scaled (vertexX, vertexY, numVertex, blue, 1, scaleY)
		# draw the polygon scaled XY
		scaled (vertexX, vertexY, numVertex, purple, scaleX, scaleY)

		# update display
		pygame.display.update ()

		# wait for user exit
		while 1 :
				for event in pygame.event.get () :
						if event.type == pygame.QUIT :
								sys.exit ()