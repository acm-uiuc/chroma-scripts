import sys
import random
import time
from animations import FadeAnimation 

nice_pixels = [
    (1023.0,0.0,0.0),
    (0.0,1023.0,0.0),
    (0.0,0.0,1023.0),
    (823.0,823.0,0.0),
    (823.0,0.0,823.0),
    (0.0,823.0,823.0),
]
template = [[0,1,4,5],[2,3,6,7],[8,9,12,13],[10,11,14,15],[16,17,20,21],[18,19,22,23],[0,1,2,3,4,7,8,11,12,13,14,15],[5,6,9,10],]
bgColor=(0.0,0.0,0.0)
out = FadeAnimation()
out.start()
layout = [bgColor]*24

"""
Spirals! Start from 0-3,3-15,15-12,12-4,4-6,6-10,10-9, then do it in reverse
"""
def spirals():
    path = [0,1,2,3,7,11,15,14,13,12,8,4,5,6,10,9]
    
    rand = random.sample(nice_pixels,4)
    for i in range(len(path)):
        layout[path[i]] = rand[0]
        #try commenting out these if statement and see if you like it better
        if (i != 0):
            layout[path[i-1]] = rand[1]
        out.write(layout)
        time.sleep(0.05)
    for i in range(len(path)):
        layout[path[len(path)-1-i]] = rand[2]
        #try commenting out these if statement and see if you like it better
        if (i != 0):
            layout[path[len(path)-i]] = rand[3]
        out.write(layout)
        time.sleep(0.05)
"""
Make the center box blink and fade out.
"""

def blinky():
    layout = [bgColor]*24

    rand = random.sample(nice_pixels,2)
    for i in template[len(template)-2]:
        layout[i] = rand[0]
    out.write(layout)
    time.sleep(0.3)
    for i in template[len(template)-1]:
        layout[i] = rand[1]    
    out.write(layout)
    time.sleep(0.3)
    temp = layout
    layout = [bgColor]*24
    #recycle code later
    # for i in range(3):
    #     if (i%2 == 0):
    #         layout = [bgColor]*24
    #     else :
    #         layout = temp
    #     out.write(layout)
    #     time.sleep(0.1)

if __name__ == "__main__":
    while True:
        spirals()
        blinky()
