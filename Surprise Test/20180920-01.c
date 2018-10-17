/*
	Date : 20/09/2018
	Surprise Test 01 - Draw a Half filled Glass.
		- Akshay Kumar (CED15I031)
*/

#include <stdio.h>
#include <graphics.h>

#define DELAY 10
#define PERCENT 50
#define WaterColor CYAN
#define GlassColor GREEN

int x_center, y_top_center, y_bottom_center, y_radius_bottom, x_radius_bottom, y_radius_top, x_radius_top;

void wait_for_char ()
{
	//Wait for a key press
	int in = 0;

	while (in == 0)
	{
		in = getchar ();
	}
}

void fillGlass (int percent)
{
	setcolor (GlassColor);
	int y_new = y_bottom_center - ((y_bottom_center - y_top_center) / 100) * percent;
	int y_radius = y_radius_bottom + ((y_radius_top - y_radius_bottom) / 100) * percent;
	int x_radius = x_radius_bottom + ((x_radius_top - x_radius_bottom) / 100) * percent;
	
	setcolor (WaterColor);
	ellipse (x_center, y_new, 0, 360, x_radius, y_radius);
	floodfill (x_center, y_new, WaterColor);
}

void drawGlass (int COLOR)
{
	setcolor (COLOR);
	ellipse (x_center, y_top_center, 0, 360, x_radius_top, y_radius_top);
	ellipse (x_center, y_bottom_center, 0, 360, x_radius_bottom, y_radius_bottom);
	line (x_center + x_radius_top, y_top_center, x_center + x_radius_bottom, y_bottom_center);
	line (x_center - x_radius_top, y_top_center, x_center - x_radius_bottom, y_bottom_center);
}

// main module
int main ()
{
	// initialise the graphics system
	int gd = DETECT, gm;
	initgraph (&gd, &gm, NULL);

	// initialize top and bottom points
	x_center = (getmaxx () + 1) / 2;
	y_top_center = 20;
	y_bottom_center = getmaxy () - 10;
	y_radius_bottom = 5;
	x_radius_bottom = 50;
	y_radius_top = 10;
	x_radius_top = 100;
	int percent = 0;

	// display a glass and fill it
	drawGlass (GlassColor);
	while (percent <= PERCENT)
	{
		if (!percent)
		{
			setcolor (BLACK);
			ellipse (x_center, y_bottom_center, 0, 180, x_radius_bottom, y_radius_bottom);
		}
		fillGlass (percent);
		percent++;
	}

	wait_for_char ();

	closegraph ();
	
	return 0;
}