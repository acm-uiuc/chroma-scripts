#!/usr/bin/env python
import sys, random
from animations import FadeAnimation 

red   = (1023.0,0.0,0.0)
white = (1023.0,1023.0,1023.0)
blue  = (0.0,0.0,1023.0)

flag = [blue, blue, red,   red,
        blue, blue, white, white,
        red,  red,  red,   red,
        white, white, white, white,
        red, red, red, red,
        white, white, white, white]

if __name__ == "__main__":
    import time

    out = FadeAnimation()
    out.start()
    while True:
        out.write(flag)
        time.sleep(1.0)

