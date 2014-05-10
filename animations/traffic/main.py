import sys
from oscapi import ColorsOut
import random
import math
import time
from animations import FadeAnimation 


#author: Harsh Singh
nice_pixels = [
    (1023.0,0.0,0.0),
    (0.0,1023.0,0.0),
    (1023,1023,0),
]

scale = 1
out = FadeAnimation()
out.start()
light_count = 48


def frame1():
    scale = random.randint(1,4)
    layout = [nice_pixels[0]]*light_count
    out.write(layout)
    time.sleep(3*scale)
    layout = [nice_pixels[1]]*light_count
    out.write(layout)
    time.sleep(5*scale)
    layout = [nice_pixels[2]]*light_count
    out.write(layout)
    time.sleep(1*scale)



if __name__ == "__main__":
    while True:
        frame1()
