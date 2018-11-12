# !/usr/bin/env python

#	Assignment 4.1 - Image using inbuilt command (IIITDM Gate)
#		- Akshay Kumar (CED15I031)

import pygame # importing pygame module for graphics and sound libraries
import sys # importing sys module for system-specific functions
import math # importing math module for sine and cosine functions
import random # importing random module to generate random numbers

# defining delay in terms of milliseconds
delay = 500

# defining some colors
black = (0, 0, 0) # black color
road = (67, 67, 67) # road color
sand = (139, 102, 46) # sand color
white = (255, 255, 255) # white color
red = (255, 0, 0) # red color
green = (0, 255, 0) # green color
blue = (0, 0, 255) # blue color
light_blue = (12, 50, 200) # light blue color
sky = (199, 234, 238) # sky color
cream = (250, 210, 188) # cream color
brick = (188, 60, 33) # brick color
silver_board = (146, 145, 144) # silver board color
grass = (36, 109, 20) # grass color
glass = (178, 212, 225) # glass color

# select some properties for display
screenSize = scrWidth, scrHeight = 1200, 680

# screen update
def screenUpdate () :
	pygame.time.wait (delay)
	pygame.display.update ()

# draw gate function
def drawGate () :
	# Institute Name Board
	pygame.draw.polygon (display_box, white, [(140, 160), (140, 200), (1060, 200), (1060, 160)])
	pygame.draw.polygon (display_box, black, [(140, 160), (140, 200), (1060, 200), (1060, 160)], 1)
	screenUpdate ()
	# Gate Roof
	pygame.draw.polygon (display_box, cream, [(140, 200), (1060, 200), (920, 215), (280, 215)])
	pygame.draw.polygon (display_box, black, [(140, 200), (1060, 200), (920, 215), (280, 215)], 1)
	screenUpdate ()
	# Center Pillar
	pygame.draw.polygon (display_box, brick, [(560, 200), (630, 200), (630, 460), (560, 460)])
	pygame.draw.polygon (display_box, black, [(560, 200), (630, 200), (630, 460), (560, 460)], 1)
	screenUpdate ()
	# White Board Center Pillar
	pygame.draw.polygon (display_box, white, [(561, 230), (561, 260), (629, 260), (629, 230)])
	pygame.draw.polygon (display_box, black, [(561, 230), (561, 260), (629, 260), (629, 230)], 1)
	screenUpdate ()
	# Side Walls - Left
	pygame.draw.polygon (display_box, white, [(160, 200), (160, 460), (180, 460), (180, 200)])
	pygame.draw.polygon (display_box, black, [(160, 200), (160, 460), (180, 460), (180, 200)], 1)
	pygame.draw.polygon (display_box, white, [(180, 200), (180, 460), (220, 445), (220, 205)])
	pygame.draw.polygon (display_box, black, [(180, 200), (180, 460), (220, 445), (220, 205)], 1)
	# Side Walls - Right
	pygame.draw.polygon (display_box, white, [(1010, 200), (1010, 460), (1030, 460), (1030, 200)])
	pygame.draw.polygon (display_box, black, [(1010, 200), (1010, 460), (1030, 460), (1030, 200)], 1)
	pygame.draw.polygon (display_box, white, [(1010, 200), (1010, 460), (970, 445), (970, 205)])
	pygame.draw.polygon (display_box, black, [(1010, 200), (1010, 460), (970, 445), (970, 205)], 1)
	screenUpdate ()
	# Roof of Security Rooms
	pygame.draw.polygon (display_box, white, [(170, 320), (320, 320), (350, 315), (220, 315)])
	pygame.draw.polygon (display_box, black, [(170, 320), (320, 320), (350, 315), (220, 315)], 1)
	pygame.draw.polygon (display_box, white, [(1020, 320), (870, 320), (840, 315), (970, 315)])
	pygame.draw.polygon (display_box, black, [(1020, 320), (870, 320), (840, 315), (970, 315)], 1)
	screenUpdate ()
	# Side Pillars - Left
	pygame.draw.polygon (display_box, white, [(240, 200), (240, 460), (320, 460), (320, 200)])
	pygame.draw.polygon (display_box, black, [(240, 200), (240, 460), (320, 460), (320, 200)], 1)
	pygame.draw.polygon (display_box, white, [(320, 200), (320, 460), (330, 450), (330, 205)])
	pygame.draw.polygon (display_box, black, [(320, 200), (320, 460), (330, 450), (330, 205)], 1)
	# Side Pillars - Right
	pygame.draw.polygon (display_box, white, [(870, 200), (870, 460), (950, 460), (950, 200)])
	pygame.draw.polygon (display_box, black, [(870, 200), (870, 460), (950, 460), (950, 200)], 1)
	pygame.draw.polygon (display_box, white, [(870, 200), (870, 460), (860, 450), (860, 205)])
	pygame.draw.polygon (display_box, black, [(870, 200), (870, 460), (860, 450), (860, 205)], 1)
	screenUpdate ()
	# Security Room - Left
	pygame.draw.polygon (display_box, white, [(170, 320), (170, 460), (320, 460), (320, 320)])
	pygame.draw.polygon (display_box, black, [(170, 320), (170, 460), (320, 460), (320, 320)], 1)
	pygame.draw.polygon (display_box, glass, [(200, 350), (200, 400), (320, 400), (320, 350)])
	pygame.draw.polygon (display_box, (50, 50, 50), [(200, 350), (200, 400), (320, 400), (320, 350)], 3)
	pygame.draw.polygon (display_box, white, [(320, 320), (320, 460), (350, 440), (350, 315)])
	pygame.draw.polygon (display_box, black, [(320, 320), (320, 460), (350, 440), (350, 315)], 1)
	# Security Room - Right
	pygame.draw.polygon (display_box, white, [(870, 320), (870, 460), (1020, 460), (1020, 320)])
	pygame.draw.polygon (display_box, black, [(870, 320), (870, 460), (1020, 460), (1020, 320)], 1)
	pygame.draw.polygon (display_box, glass, [(870, 350), (870, 400), (990, 400), (990, 350)])
	pygame.draw.polygon (display_box, (50, 50, 50), [(870, 350), (870, 400), (990, 400), (990, 350)], 3)
	pygame.draw.polygon (display_box, white, [(870, 320), (870, 460), (840, 440), (840, 315)])
	pygame.draw.polygon (display_box, black, [(870, 320), (870, 460), (840, 440), (840, 315)], 1)
	screenUpdate ()
	# Gate Floor
	pygame.draw.polygon (display_box, cream, [(320, 460), (350, 440), (840, 440), (870, 460)])
	pygame.draw.polygon (display_box, black, [(320, 460), (350, 440), (840, 440), (870, 460)], 1)
	screenUpdate ()
	# Grill Gates - Left
	pygame.draw.polygon (display_box, silver_board, [(322, 322), (438, 322), (438, 458), (322, 458)], 3)
	pygame.draw.line (display_box, silver_board, (322, 356), (438, 356), 3)
	pygame.draw.line (display_box, silver_board, (322, 390), (438, 390), 3)
	pygame.draw.line (display_box, silver_board, (322, 424), (438, 424), 3)
	pygame.draw.line (display_box, silver_board, (322, 434), (438, 434), 3)
	pygame.draw.line (display_box, silver_board, (322, 444), (438, 444), 3)
	for i in range (332, 438, 10) :
		pygame.draw.line (display_box, silver_board, (i, 322), (i, 458), 3)
	pygame.draw.polygon (display_box, silver_board, [(442, 322), (558, 322), (558, 458), (442, 458)], 3)
	pygame.draw.line (display_box, silver_board, (442, 356), (558, 356), 3)
	pygame.draw.line (display_box, silver_board, (442, 390), (558, 390), 3)
	pygame.draw.line (display_box, silver_board, (442, 424), (558, 424), 3)
	pygame.draw.line (display_box, silver_board, (442, 434), (558, 434), 3)
	pygame.draw.line (display_box, silver_board, (442, 444), (558, 444), 3)
	for i in range (452, 558, 10) :
		pygame.draw.line (display_box, silver_board, (i, 322), (i, 458), 3)
	# Grill Gates - Right
	pygame.draw.polygon (display_box, silver_board, [(632, 322), (748, 322), (748, 458), (632, 458)], 3)
	pygame.draw.line (display_box, silver_board, (632, 356), (748, 356), 3)
	pygame.draw.line (display_box, silver_board, (632, 390), (748, 390), 3)
	pygame.draw.line (display_box, silver_board, (632, 424), (748, 424), 3)
	pygame.draw.line (display_box, silver_board, (632, 434), (748, 434), 3)
	pygame.draw.line (display_box, silver_board, (632, 444), (748, 444), 3)
	for i in range (642, 748, 10) :
		pygame.draw.line (display_box, silver_board, (i, 322), (i, 458), 3)
	pygame.draw.polygon (display_box, silver_board, [(752, 322), (868, 322), (868, 458), (752, 458)], 3)
	pygame.draw.line (display_box, silver_board, (752, 356), (868, 356), 3)
	pygame.draw.line (display_box, silver_board, (752, 390), (868, 390), 3)
	pygame.draw.line (display_box, silver_board, (752, 424), (868, 424), 3)
	pygame.draw.line (display_box, silver_board, (752, 434), (868, 434), 3)
	pygame.draw.line (display_box, silver_board, (752, 444), (868, 444), 3)
	for i in range (762, 868, 10) :
		pygame.draw.line (display_box, silver_board, (i, 322), (i, 458), 3)
	screenUpdate ()
	# Brick Wall - Left
	pygame.draw.polygon (display_box, brick, [(170, 310), (170, 460), (120, 460), (120, 310)])
	pygame.draw.polygon (display_box, black, [(170, 310), (170, 460), (120, 460), (120, 310)], 1)
	# Brick Wall - Right
	pygame.draw.polygon (display_box, brick, [(1070, 310), (1070, 460), (1020, 460), (1020, 310)])
	pygame.draw.polygon (display_box, black, [(1070, 310), (1070, 460), (1020, 460), (1020, 310)], 1)
	screenUpdate ()
	# White Wall - Left
	pygame.draw.polygon (display_box, white, [(120, 340), (120, 460), (0, 460), (0, 340)])
	pygame.draw.polygon (display_box, black, [(120, 340), (120, 460), (0, 460), (0, 340)], 1)
	pygame.draw.polygon (display_box, (50, 50, 50), [(100, 370), (100, 440), (0, 440), (0, 370)])
	pygame.draw.polygon (display_box, black, [(100, 370), (100, 440), (0, 440), (0, 370)], 1)
	pygame.draw.polygon (display_box, silver_board, [(95, 375), (95, 435), (0, 435), (0, 375)])
	pygame.draw.polygon (display_box, black, [(95, 375), (95, 435), (0, 435), (0, 375)], 1)
	# White Wall - Right
	pygame.draw.polygon (display_box, white, [(1199, 340), (1199, 460), (1070, 460), (1070, 340)])
	pygame.draw.polygon (display_box, black, [(1199, 340), (1199, 460), (1070, 460), (1070, 340)], 1)
	screenUpdate ()
	# Grass
	for i in range (0, 320, 5) :
		height = 10 * random.randint (1, 5)
		width = 3 * random.randint (1, 3)
		pygame.draw.polygon (display_box, grass, [(i - width, 460), (i, 460 - height), (i + width, 460)])
	for i in range (880, 1200, 5) :
		height = 10 * random.randint (1, 5)
		width = 3 * random.randint (1, 3)
		pygame.draw.polygon (display_box, grass, [(i - width, 460), (i, 460 - height), (i + width, 460)])
	for i in range (570, 625, 5) :
		height = 10 * random.randint (1, 5)
		width = 3 * random.randint (1, 4)
		pygame.draw.polygon (display_box, grass, [(i - width, 460), (i, 460 - height), (i + width, 460)])
	pygame.draw.polygon (display_box, grass, [(0, 679), (320, 460), (0, 460)])
	pygame.draw.polygon (display_box, black, [(0, 679), (320, 460), (0, 460)], 1)
	pygame.draw.polygon (display_box, grass, [(1199, 679), (870, 460), (1199, 460)])
	pygame.draw.polygon (display_box, black, [(1199, 679), (870, 460), (1199, 460)], 1)
	screenUpdate ()
	# Road outside
	pygame.draw.polygon (display_box, road, [(0, 679), (320, 460), (870, 460), (1199, 679)])
	pygame.draw.polygon (display_box, black, [(0, 679), (320, 460), (870, 460), (1199, 679)], 1)
	screenUpdate ()
	# Divider outside
	pygame.draw.circle (display_box, sand, (600, 630), 45)
	pygame.draw.circle (display_box, black, (600, 630), 45, 1)
	pygame.draw.polygon (display_box, sand, [(555, 630), (645, 630), (657, 679), (543, 679)])
	pygame.draw.line (display_box, black, [555, 630], [543, 679], 1)
	pygame.draw.line (display_box, black, [645, 630], [657, 679], 1)
	screenUpdate ()
	for i in range (555, 657, 5) :
		height = 10 * random.randint (1, 10)
		width = 2 * random.randint (1, 4)
		pygame.draw.polygon (display_box, grass, [(i - width, 679), (i, 679 - height), (i + width, 679)])
	screenUpdate ()
	# Institute Name
	pygame.font.init ()
	myfont = pygame.font.SysFont ('monospace', 18, 1)
	textsurface = myfont.render ('INDIAN INSTITUTE OF INFORMATION TECHNOLOGY, DESIGN AND MANUFACTURING, KANCHEEPURAM', False, (0, 0, 0))
	display_box.blit (textsurface, (148, 170))
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
