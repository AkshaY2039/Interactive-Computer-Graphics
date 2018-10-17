/*
	Date : 20/09/2018
	Surprise Test 02 - Display an Arrow and let it move/fly from left to right on screen.
		- Akshay Kumar (CED15I031)
*/

#include <stdio.h>
#include <graphics.h>

#define DELAY 10

void drawArrowFromLeft (int x, int y, int COLOR)
{
	int points[] = {x, y, x+10, y-20, x+20, y, x+12, y, x+12, y+20, x+8, y+20, x+8, y, x, y};
	setcolor (COLOR);
	drawpoly (8, points);
	floodfill (x+10, y, COLOR);
}

// main module
int main ()
{
	// initialise the graphics system
	int gd = DETECT, gm;
	initgraph (&gd, &gm, NULL);

	// get max_x and max_y & in terms of squares of 10px
	int max_x = (getmaxx () + 1);
	int x = 0, y = 150;

	// display and move an ARROW
	while (1)
	{
		drawArrowFromLeft (x, y, BLUE);
		delay (DELAY);
		drawArrowFromLeft (x, y, BLACK);
		x++;
		if (x == max_x-20)
			x = 0;
	}

	closegraph ();
	
	return 0;
}