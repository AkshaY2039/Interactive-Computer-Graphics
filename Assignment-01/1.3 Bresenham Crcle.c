/*
	Assignment 1.3 - Bresenham's Circle Algorithm
		- Akshay Kumar (CED15I031)
*/

#include <stdio.h>
#include <graphics.h>

/* Using Bresenham's Circle Algorithm to draw a circle with centre (c_x,c_y) and radius (r) */
void bhmCircle (int c_x, int c_y, int r)
{
	// Quadrant Coordinates
	putpixel (c_x, c_y + r, RED);
	putpixel (c_x, c_y - r, RED);
	putpixel (c_x + r, c_y, RED);
	putpixel (c_x - r, c_y, RED);

	int d_p; // decision parameter
	d_p = 1 - r;

	int x, y;
	for (x = 1, y = r; x <= y; x++)
	{
		if (d_p >= 0)
		{
			y -= 1;
			d_p += 2 * (x - y) + 5;
		}
		else
			d_p += 2 * x + 3;

		// Arc near the North and South Coordinates
		putpixel (c_x + x, c_y + y, YELLOW);
		putpixel (c_x - x, c_y + y, YELLOW);
		putpixel (c_x + x, c_y - y, YELLOW);
		putpixel (c_x - x, c_y - y, YELLOW);

		// Arc near the East and West Coordinates
		putpixel (c_x + y, c_y + x, CYAN);
		putpixel (c_x - y, c_y + x, CYAN);
		putpixel (c_x + y, c_y - x, CYAN);
		putpixel (c_x - y, c_y - x, CYAN);
	}
}

void wait_for_char ()
{
	//Wait for a key press
	int in = 0;

	while (in == 0)
	{
		in = getchar ();
	}
}

// main module
int main ()
{
	// initialise the graphics system
	int gd = DETECT, gm;
	initgraph (&gd, &gm, NULL);

	// draw a example illustrating all cases
	bhmCircle (310, 210, 5);
	bhmCircle (310, 210, 10);
	bhmCircle (310, 210, 20);
	bhmCircle (310, 210, 40);
	bhmCircle (310, 210, 70);
	bhmCircle (310, 210, 150);
	bhmCircle (310, 210, 200);

	// delay(5000);
	wait_for_char ();
	closegraph ();
	
	return 0;
}