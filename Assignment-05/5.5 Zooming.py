# !/usr/bin/env python

#	Assignment 5.5 - Affine Transformation - Zooming
#		- Akshay Kumar (CED15I031)

import pygame # importing pygame module for graphics and sound libraries
import sys # importing sys module for system-specific functions

# defining delay in terms of milliseconds
delay = 20

# defining some colors
backGroundColor = (0, 0, 0) # background color as black
white = (255, 255, 255) # white color
red = (255, 0, 0) # red color
green = (0, 255, 0) # green color
blue = (0, 0, 255) # blue color

# select some properties for display
screenSize = scrWidth, scrHeight = 1024, 512
originX = int (scrWidth / 2)
originY = int (scrHeight / 2)
