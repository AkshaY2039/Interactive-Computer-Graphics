# !/usr/bin/env python

#	Assignment 5.5 - Affine Transformation - Zooming
#		- Akshay Kumar (CED15I031)

import pygame # importing pygame module for graphics and sound libraries
import sys # importing sys module for system-specific functions

# defining some colors
backGroundColor = (0, 0, 0) # background color as black
white = (255, 255, 255) # white color
green = (0, 255, 0) # green color
purple = (255, 0, 255) # purple color

# select some properties for display
screenSize = scrWidth, scrHeight = 1024, 512
originX = int (scrWidth / 2)
originY = int (scrHeight / 2)

# draw polygon
def drawPolygon (vertexX, vertexY, numVertex, color) :
	for i in range (numVertex) :
		pygame.draw.line (display_box, color, [vertexX[i % numVertex], vertexY[i % numVertex]], [vertexX[(i + 1) % numVertex], vertexY[(i + 1) % numVertex]], 1)
	pygame.display.update ()

# zoomed
def zoomed (vertexX, vertexY, numVertex, color, zoomCenterX, zoomCenterY, zoomFactor) :
	for i in range (numVertex) :
		x1 = zoomCenterX + zoomFactor * (vertexX[i % numVertex] - zoomCenterX)
		y1 = zoomCenterY + zoomFactor * (zoomCenterY - vertexY[i % numVertex])
		x2 = zoomCenterX + zoomFactor * (vertexX[(i + 1) % numVertex] - zoomCenterX)
		y2 = zoomCenterY + zoomFactor * (zoomCenterY - vertexY[(i + 1) % numVertex])
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
			vertexX.append (temp % originX + originX)
			temp = int (input ('Y coordinate : ').strip ())
			vertexY.append (originY - temp % originY)
		zoomCenterX = int (input ('Enter the zoom center X coordinate : ').strip ())
		zoomCenterX = zoomCenterX % originX + originX
		zoomCenterY = int (input ('Enter the zoom center Y coordinate : ').strip ())
		zoomCenterY = originY - zoomCenterY % originY
		zoomFactor = int (input ('Enter the zoom Factor : ').strip ())

		# initialize the display box (window)
		display_box = pygame.display.set_mode (screenSize) # set size of screen
		display_box.fill (backGroundColor) # set background color of the screen
		pygame.display.update ()

		# draw axes
		pygame.draw.line (display_box, white, [originX, 0], [originX, scrHeight], 1)
		pygame.draw.line (display_box, white, [0, originY], [scrWidth, originY], 1)
		pygame.display.update ()

		# draw the polygon
		drawPolygon (vertexX, vertexY, numVertex, green)
		# draw the polygon zoomed
		zoomed (vertexX, vertexY, numVertex, purple, zoomCenterX, zoomCenterY, zoomFactor)

		# update display
		pygame.display.update ()

		# wait for user exit
		while 1 :
				for event in pygame.event.get () :
						if event.type == pygame.QUIT :
								sys.exit ()