/*
	Assignment 1.2 - Digital Differential Analyzer Algorithm for Straight Line
		- Akshay Kumar (CED15I031)
*/

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <graphics.h>

// to swap two integers
void swap (int a, int b)
{
	a ^= b;
	b ^= a;
	a ^= b;
}

/* Using DDA Line Algorithm to draw a line between (x_one, y_one) and (x_two, y_two) */
void ddaLine (int x_one, int y_one, int x_two, int y_two, int COLOR)
{
	int diff_x, diff_y;
	diff_x = x_two - x_one;
	diff_y = y_two - y_one;

	float step;

	// point one and point 2
	if ((diff_x == diff_y) && (diff_x == 0))
		putpixel(x_one, y_one, COLOR);
	else // step in x direction, diff_x=1, diff_y=m
		if (abs (diff_x) >= abs (diff_y))
		{
			if (x_one > x_two)
			{
				swap (x_one, x_two);
				swap (y_one, y_two);

				diff_x *= -1;
				diff_y *= -1;
			}

			step = diff_y*1.0 / diff_x;

			int x;
			float y;

			for (x = x_one, y = y_one; x <= x_two; x++)
			{
				putpixel (x, (int)round(y), COLOR);
				y += step;
			}
		}
		else // step in y direction, diff_y=1, diff_x=1/m
			{
				if (y_one > y_two)
				{
					swap (x_one, x_two);
					swap (y_one, y_two);

					diff_x *= -1;
					diff_y *= -1;
				}

				step = diff_x*1.0 / diff_y;
		
				int y;
				float x;

				for (y = y_one, x = x_one; y <= y_two; y++)
				{
					putpixel ((int)round(x), y, COLOR);
					x += step;
				}
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

int main ()
{
	int gd = DETECT, gm;
	initgraph (&gd, &gm, NULL);

	// draw lines using the ddaLine function
	ddaLine (120, 100, 420, 400, RED);
	ddaLine (110, 150, 450, 226, YELLOW);
	ddaLine (200, 100, 200, 250, BLUE);
	ddaLine (100, 120, 400, 420, GREEN);
	ddaLine (150, 110, 226, 450, CYAN);
	ddaLine (100, 200, 250, 200, MAGENTA);

	delay (5000);
	wait_for_char ();
	closegraph ();

	return 0;
}