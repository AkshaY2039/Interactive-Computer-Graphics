# !/usr/bin/env python

#	Assignment 2.1 - Bayer's Filter - Filtered and Demosaiced Image
#		- Akshay Kumar (CED15I031)

import numpy # importing numpy module for matrix computation
from random import randint # importing randint function from random module
from PIL import Image # importing Image module from Python Image Library

# big pixel function to make a square of given pixel size
def big_pixel (img, pixel_size) :
	rows, columns, temp = img.shape
	image_space = numpy.zeros ((rows * pixel_size, columns * pixel_size, 3), dtype = numpy.uint8)
	for y in range (rows) :
		for x in range (columns) :
				image_space[y * pixel_size : y * pixel_size + (pixel_size),
						x * pixel_size : x * pixel_size + (pixel_size)] = img[y, x]
	return image_space

# dumping pixel data in to file
def printPixelDataToFile (fileDesc, pixel_data, filename) :
	f = open (filename, 'w')
	print (fileDesc, file = f)
	for row_num in pixel_data:
		print (row_num.tolist (), file = f)
	f.close ()

# start here
if __name__ == '__main__' :
	# take pixel size, image size as inputs
	pixel_size = int (input ('Enter the size of a pixel square : ').strip ())
	columns = int (input ('Enter the width (in number of columns) : ').strip ())
	rows = int (input ('Enter the height (in number of rows) : ').strip ())

# creating empty matrix for image
img = numpy.zeros ((rows, columns, 3), dtype = numpy.uint8)

# generate a random image by using RGBG filter
for y in range (rows) :
	for x in range (columns) :
		if y%2 == 0 and x%2 == 0 :
			img[y, x, 0] = randint (0, 255)
		else :
			if y%2 == 1 and x%2 == 1 :
				img[y, x, 2] = randint (0, 255)
			else :
				img[y, x, 1] = randint (0, 255)

# save and show the filtered image
printPixelDataToFile ('Bayer\'s filter generated image:', img, 'filtered.txt')
image_space = big_pixel (img, pixel_size)
Image.fromarray (image_space, 'RGB').save ('filtered.png')
filtered = Image.open ('filtered.png')
filtered.show ()
print ('Filtered Image saved in the program directory.')

# demosaicing
dmx_image = numpy.zeros (img.shape, dtype = numpy.uint8)
# we leave edges so it 0, rows-1 and 0, columns-1 is excluded
for y in range (1, rows-1) :
	for x in range (1, columns-1) :
		if y%2 == 0 and x%2 == 0 :
			# ceter is red
			red = img[y, x]
			green = (numpy.uint16 (img[y-1, x]) + numpy.uint16 (img[y+1, x]) + numpy.uint16 (img[y, x-1]) + numpy.uint16 (img[y, x+1])) / 4
			blue = (numpy.uint16 (img[y-1, x-1]) + numpy.uint16 (img[y-1, x+1]) + numpy.uint16 (img[y+1, x-1]) + numpy.uint16 (img[y+1, x+1])) / 4
		else :
			if y%2 == 1 and x%2 == 1 :
				# centre is blue
				red = (numpy.uint16 (img[y-1, x-1]) + numpy.uint16 (img[y-1, x+1]) + numpy.uint16 (img[y+1, x-1]) + numpy.uint16 (img[y+1, x+1]))/4
				green = (numpy.uint16 (img[y-1, x]) + numpy.uint16 (img[y+1, x]) + numpy.uint16 (img[y, x-1]) + numpy.uint16 (img[y, x+1]))/4
				blue = img[y, x]
			else :
				# centre is green
				red = (numpy.uint16 (img[y-1, x]) + numpy.uint16 (img[y+1, x]))/2
				green = img[y, x]
				blue = (numpy.uint16 (img[y, x-1]) + numpy.uint16 (img[y, x+1]))/2
		dmx_image[y, x] = red + green + blue

# save and show demosaiced image
printPixelDataToFile ('Demosaiced Image:', dmx_image, 'demosaiced.txt')
dmx_image_box = big_pixel (dmx_image, pixel_size)
Image.fromarray (dmx_image_box, 'RGB').save ('demosaiced.png')
demosaiced = Image.open ('demosaiced.png')
demosaiced.show ()
print ('Demosaiced Image saved in the program directory.')
