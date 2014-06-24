#!/usr/bin/env python
import sys, random
from animations import FadeAnimation 

red   = (1023.0,0.0,0.0)
white = (1023.0,1023.0,1023.0)
blue  = (0.0,0.0,1023.0)

flag = [white, red, white, blue, blue, blue,
	white, red, white, blue, blue, blue,
	white, red, white, blue, blue, blue,
	white, red, white, blue, blue, blue,
	white, red, white, red, white, red,
	white, red, white, red, white, red,
	white, red, white, red, white, red,
	white, red, white, red, white, red]

if __name__ == "__main__":
    import time

    out = FadeAnimation()
    out.start()
    while True:
        out.write(flag)
        time.sleep(1.0)

