# !/usr/bin/env python

#	Assignment 4.1 - Image using inbuilt command (IIITDM Gate)
#		- Akshay Kumar (CED15I031)

import pygame # importing pygame module for graphics and sound libraries
import sys # importing sys module for system-specific functions
import math # importing math module for sine and cosine functions
import random # importing random module to generate random numbers

# defining delay in terms of milliseconds
delay = 20

# defining some colors
black = (0, 0, 0) # black color
road = (67, 67, 67) # road color
sand = (139, 102, 46) # sand color
white = (255, 255, 255) # white color
red = (255, 0, 0) # red color
green = (0, 255, 0) # green color
blue = (0, 0, 255) # blue color
light_blue = (12, 50, 200) # light blue color
sky = (217, 235, 237) # sky color
cream = (250, 210, 188) # cream color
brick = (188, 60, 33) # brick color
silver_board = (146, 145, 144) # silver board color
grass = (36, 109, 20) # grass color

# select some properties for display
screenSize = scrWidth, scrHeight = 1200, 680

# draw gate function
def drawGate () :
	# Center Pillar
	pygame.draw.polygon (display_box, brick, [(560, 200), (630, 200), (630, 460), (560, 460)])
	pygame.draw.polygon (display_box, black, [(560, 200), (630, 200), (630, 460), (560, 460)], 1)
	# White Board Center Pillar
	pygame.draw.polygon (display_box, white, [(561, 230), (561, 260), (629, 260), (629, 230)])
	pygame.draw.polygon (display_box, black, [(561, 230), (561, 260), (629, 260), (629, 230)], 1)
	# Side Pillars - Left
	pygame.draw.polygon (display_box, white, [(240, 200), (240, 460), (320, 460), (320, 200)])
	pygame.draw.polygon (display_box, black, [(240, 200), (240, 460), (320, 460), (320, 200)], 1)
	# Side Pillars - Right
	pygame.draw.polygon (display_box, white, [(870, 200), (870, 460), (950, 460), (950, 200)])
	pygame.draw.polygon (display_box, black, [(870, 200), (870, 460), (950, 460), (950, 200)], 1)
	# Side Walls - Left
	pygame.draw.polygon (display_box, white, [(160, 200), (160, 460), (180, 460), (180, 200)])
	pygame.draw.polygon (display_box, black, [(160, 200), (160, 460), (180, 460), (180, 200)], 1)
	# Side Walls - Right
	pygame.draw.polygon (display_box, white, [(1010, 200), (1010, 460), (1030, 460), (1030, 200)])
	pygame.draw.polygon (display_box, black, [(1010, 200), (1010, 460), (1030, 460), (1030, 200)], 1)
	# Security Room - Left
	pygame.draw.polygon (display_box, white, [(170, 320), (170, 460), (320, 460), (320, 320)])
	pygame.draw.polygon (display_box, black, [(170, 320), (170, 460), (320, 460), (320, 320)], 1)
	# Security Room - Right
	pygame.draw.polygon (display_box, white, [(870, 320), (870, 460), (1020, 460), (1020, 320)])
	pygame.draw.polygon (display_box, black, [(870, 320), (870, 460), (1020, 460), (1020, 320)], 1)
	# Grill Gates - Left
	pygame.draw.polygon (display_box, silver_board, [(322, 322), (438, 322), (438, 458), (322, 458)], 3)
	for i in range (332, 438, 10) :
		pygame.draw.line (display_box, silver_board, (i, 322), (i, 458), 3)
	pygame.draw.polygon (display_box, silver_board, [(442, 322), (558, 322), (558, 458), (442, 458)], 3)
	for i in range (452, 558, 10) :
		pygame.draw.line (display_box, silver_board, (i, 322), (i, 458), 3)
	# Grill Gates - Right
	pygame.draw.polygon (display_box, silver_board, [(632, 322), (748, 322), (748, 458), (632, 458)], 3)
	for i in range (642, 748, 10) :
		pygame.draw.line (display_box, silver_board, (i, 322), (i, 458), 3)
	pygame.draw.polygon (display_box, silver_board, [(752, 322), (868, 322), (868, 458), (752, 458)], 3)
	for i in range (762, 868, 10) :
		pygame.draw.line (display_box, silver_board, (i, 322), (i, 458), 3)
	# Brick Wall - Left
	pygame.draw.polygon (display_box, brick, [(170, 320), (170, 460), (120, 460), (120, 320)])
	pygame.draw.polygon (display_box, black, [(170, 320), (170, 460), (120, 460), (120, 320)], 1)
	# Brick Wall - Right
	pygame.draw.polygon (display_box, brick, [(1080, 320), (1080, 460), (1020, 460), (1020, 320)])
	pygame.draw.polygon (display_box, black, [(1080, 320), (1080, 460), (1020, 460), (1020, 320)], 1)
	# White Wall - Left
	pygame.draw.polygon (display_box, white, [(120, 340), (120, 460), (0, 460), (0, 340)])
	pygame.draw.polygon (display_box, black, [(120, 340), (120, 460), (0, 460), (0, 340)], 1)
	pygame.draw.polygon (display_box, (50, 50, 50), [(100, 370), (100, 440), (0, 440), (0, 370)])
	pygame.draw.polygon (display_box, black, [(100, 370), (100, 440), (0, 440), (0, 370)], 1)
	pygame.draw.polygon (display_box, silver_board, [(95, 375), (95, 435), (0, 435), (0, 375)])
	pygame.draw.polygon (display_box, black, [(95, 375), (95, 435), (0, 435), (0, 375)], 1)
	# White Wall - Right
	pygame.draw.polygon (display_box, white, [(1199, 340), (1199, 460), (1080, 460), (1080, 340)])
	pygame.draw.polygon (display_box, black, [(1199, 340), (1199, 460), (1080, 460), (1080, 340)], 1)
	# Grass
	for i in range (0, 320, 5) :
		height = 10 * random.randint (1, 5)
		width = 3 * random.randint (1, 3)
		pygame.draw.polygon (display_box, grass, [(i - width, 460), (i, 460 - height), (i + width, 460)])
	for i in range (880, 1200, 5) :
		height = 10 * random.randint (1, 5)
		width = 3 * random.randint (1, 3)
		pygame.draw.polygon (display_box, grass, [(i - width, 460), (i, 460 - height), (i + width, 460)])
	for i in range (570, 630, 5) :
		height = 10 * random.randint (1, 5)
		width = 3 * random.randint (1, 4)
		pygame.draw.polygon (display_box, grass, [(i - width, 460), (i, 460 - height), (i + width, 460)])
	pygame.draw.polygon (display_box, grass, [(0, 679), (200, 460), (0, 460)])
	pygame.draw.polygon (display_box, black, [(0, 679), (200, 460), (0, 460)], 1)
	pygame.draw.polygon (display_box, grass, [(1199, 679), (990, 460), (1199, 460)])
	pygame.draw.polygon (display_box, black, [(1199, 679), (990, 460), (1199, 460)], 1)
	# Road outside
	pygame.draw.polygon (display_box, road, [(0, 679), (200, 460), (990, 460), (1199, 679)])
	pygame.draw.polygon (display_box, black, [(0, 679), (200, 460), (990, 460), (1199, 679)], 1)
	# Divider outside
	pygame.draw.circle (display_box, sand, (600, 630), 45)
	pygame.draw.circle (display_box, black, (600, 630), 45, 1)
	pygame.draw.polygon (display_box, sand, [(555, 630), (645, 630), (657, 679), (543, 679)])
	pygame.draw.line (display_box, black, [555, 630], [543, 679], 1)
	pygame.draw.line (display_box, black, [645, 630], [657, 679], 1)
	# Institute Name Board
	pygame.draw.polygon (display_box, white, [(140, 160), (140, 200), (1060, 200), (1060, 160)])
	pygame.draw.polygon (display_box, black, [(140, 160), (140, 200), (1060, 200), (1060, 160)], 1)
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
