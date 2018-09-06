/*
	Assignment 1.1 - Bresenham's Line Algorithm
		- Akshay Kumar (CED15I031)
*/

#include <stdio.h>
#include <graphics.h>

#define DELAY 5000

// to swap two integers
void swap (int a, int b)
{
	a ^= b;
	b ^= a;
	a ^= b;
}

/* Using Bresenham's Line Algorithm to draw a line between (x_one, y_one) and (x_two, y_two) */
void bhmLine (int x_one, int y_one, int x_two, int y_two, int color)
{
	// standardize one and two points
	if (x_one > x_two)
	{
		swap (x_one, x_two);
		swap (y_one, y_two);
	}
	else
		if ((x_one == x_two) && (y_two > y_one))
		{
			swap (y_one, y_two);
		}

	putpixel (x_one, y_one, color);

	int diff_x, diff_y;
	diff_x = x_two - x_one;
	diff_y = y_two - y_one;

	int d_p, temp1, temp2; // decision parameter, 2 temporary parameters for different cases
	int i, j;

	if (diff_y >= 0)
	{
		if (diff_x > diff_y) // Case 1: 0 degrees <= Slope(m) < 45 degrees
		{
			d_p = 2*diff_y - diff_x;

			temp2 = 2*diff_y;
			temp1 = temp2 - 2*diff_x;

			for (i = x_one + 1, j = y_one; i <= x_two; i++)
			{
				if (d_p >= 0)
				{
					j += 1;
					d_p += temp1;
				}
				else
					d_p += temp2;

				putpixel(i, j, color);
			}
		}
		else // Case 2: 45 degrees <= Slope(m) < 90 degrees
			{
				d_p = 2*diff_x - diff_y;

				temp2 = 2*diff_x;
				temp1 = temp2 - 2*diff_y;

				for (i = x_one, j = y_one + 1; j <= y_two; j++)
				{
					if (d_p >= 0)
					{
						i += 1;
						d_p += temp1;
					}

					else
						d_p += temp2;

					putpixel(i, j, color);
				}
			}
	}
	else
		{
			if (-1*diff_y > diff_x) // Case 3: 90 degrees <= Slope(m) < 135 degrees
			{
				d_p = -2*diff_x - diff_y;

				temp2 = -2*diff_x;
				temp1 = temp2 - 2*diff_y;

				for (i=x_one, j=y_one-1; j>=y_two; j--)
				{
					if (d_p <= 0)
					{
						i += 1;
						d_p += temp1;
					}
					else
						d_p += temp2;

					putpixel(i, j, color);
				}
			}
			else // Case 4: 135 degrees <= Slope(m) < 180 degrees
			{
				d_p = -1*diff_x - 2*diff_y;

				temp2 = -2*diff_y;
				temp1 = temp2 - 2*diff_x;

				for (i = x_one+1, j = y_one; i <= x_two; i++) {

					if (d_p >= 0)
					{
						j -= 1;
						d_p += temp1;
					}
					else
						d_p += temp2;

					putpixel(i, j, color);
				}
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
	// initialise the graphics system
	int gd = DETECT, gm;
	initgraph (&gd, &gm, NULL);

	// draw lines using the bhmLine function
	bhmLine (100, 100, 400, 400, RED);
	bhmLine (110, 150, 500, 226, YELLOW);
	bhmLine (200, 100, 200, 250, BLUE);

	delay (DELAY);
	wait_for_char ();
	closegraph ();

	return 0;
}