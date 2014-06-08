#Written by Milan Dasgupta

from Queue import Queue
import time
from animations import FadeAnimation
import sys
from oscapi import ColorsOut


def check_speed(curr, speed, end): #Helper function that keeps the ball in bounds
	delta = 1
	if curr + speed >= end:
		delta = -1

	if curr + speed <= -1:
		delta = -1

	return delta * speed

if __name__ == "__main__":
	MAX_X = 6		   #Width and length of Chroma
        MAX_Y = 8
	tailsize = 4		   #Size of ping-pong ball's tail
	speed = 15.		   #Speed of the Ball

	green_x = 0		   #The Ball starts at (0,0) going bottom-right
	green_y = 0
	green_dir_x = 1
        green_dir_y = 1
	
	off = (0.0,0.0,0.0)        #We define three states the lights can be in
	half = (0.0, 512.0, 0.0)
	green = (0.0, 1023.0, 0.0)
	pix = []		   #Set up data structures that hold light information
	x_vals = Queue(maxsize=tailsize)
	y_vals = Queue(maxsize=tailsize)
	out = FadeAnimation()	   #Set up the fade animation
	out.FADERATE = 5.0
	out.start()
	
	for i in range(MAX_X * MAX_Y):
                pix.append(off)	   #Turns Off all Lights
	x_vals.put(green_x)	   #Put the first light on the array and turns it on
	y_vals.put(green_y)
	pix[(green_y * MAX_X) + green_x] = green
        out.write(pix)

	while True:
		time.sleep(1/speed)	#Sleeps to keep the animation running at speed

		green_dir_x = check_speed(green_x, green_dir_x, MAX_X)	#Find the next direction we're going
                green_dir_y = check_speed(green_y, green_dir_y, MAX_Y)
		pix[(green_y * MAX_X) + green_x] = half		#Set the last light to half
		if x_vals.full():				#If we're at tailsize, we turn off the last light in the tail
			pix[(y_vals.get() * MAX_X) + x_vals.get()] = off
                green_x += green_dir_x				#Set coordinates to the next light
                green_y += green_dir_y
		if (green_x == 0 and green_y == 0) or (green_x == MAX_X-1 and green_y == MAX_Y-1):
			 while not x_vals.empty():		#If we're in a corner, we turn off the tail
				pix[(y_vals.get() * MAX_X) + x_vals.get()] = off
		x_vals.put(green_x)	#Put the new coordinates on the queue
		y_vals.put(green_y)
                pix[(green_y * MAX_X) + green_x] = green	#Turn on the light

        	out.write(pix)
