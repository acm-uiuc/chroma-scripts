import sys
from oscapi import ColorsOut
import random
import math
import time
from animations import FadeAnimation 
import operator

#author: Harsh Singh
nice_pixels = [
    (1023.0,0.0,0.0),
    (0.0,1023.0,0.0),
    (0.0,0.0,1023.0),
    (0.0,1023.0,1023.0),
    (1023.0,0.,1023.0),
    (1023.0,1023.0,0.)  
]
bgColor=(0.0,0.0,0.0)
layout = [[bgColor for col in range(4)] for row in range(4)]
randColor = random.sample(nice_pixels,6)
bool_layout = [[True for col in range(4)] for row in range(4)]
max_x = 3

out = FadeAnimation()
out.start()
frame_sleep_time = .05

def makeX(col1, col2, col3):
    for x in xrange(4):
        for y in xrange(4):
            if (x==y or x==max_x-y):
                if x <= 1:
                    layout[x][y] = col1
                else:
                    layout[x][y] = col2
            else:
                layout[x][y] = col3

def makeX2(col1, col2, col3):
    for y in xrange(4):
        for x in xrange(4):
            if (x==y or x==max_x-y):
                if y <= 1:
                    layout[x][y] = col1
                else:
                    layout[x][y] = col2
            else:
                layout[x][y] = col3

def makeRandColor():
    global randColor
    randColor = random.sample(nice_pixels,6)

def transitionX():
    times = 40
    for a in xrange(0,times,1):
        makeX(transition_color(randColor[0], randColor[1], a, times),transition_color(randColor[1], randColor[0], a, times),transition_color(randColor[2], randColor[3], a, times))
        out.write(makeLayout(layout))
        time.sleep(frame_sleep_time)
    for a in xrange(0,times,1):
        makeX2(transition_color(randColor[1], randColor[0], a, times),transition_color(randColor[0], randColor[1], a, times),transition_color(randColor[3], randColor[2], a, times))
        out.write(makeLayout(layout))
        time.sleep(frame_sleep_time)
        # makeX2(transition_color(randColor[0], randColor[1], a+1, 6),transition_color(randColor[1], randColor[0], a+1, 6),transition_color(randColor[2], randColor[3], a+1, 6))
        # out.write(makeLayout(layout))
        # time.sleep(frame_sleep_time)
def makeInverse(col1, step, steps):
    col2 = tuple([invert(x) for x in list(col1)])
    step +=1
    col1 = tuple( [ float( e- (e * step/steps) ) for e in col1 ] )
    col2 = tuple( [ float( e*step/steps ) for e in col2 ] )
    return map(operator.add, col1,col2)

def invert(x):
    if x == 0:
        return 1024
    else:
        return 0




def transition_color(col1, col2, step, steps):
    step +=1
    col1 = tuple( [ float( e- (e * step/steps) ) for e in col1 ] )
    col2 = tuple( [ float( e*step/steps ) for e in col2 ] )
    return map(operator.add, col1,col2)

def makeLayout(lay):
    temp_layout = []
    for i in range(len(lay)):
        for j in range(len(lay[0])):
            temp_layout.append(lay[i][j])
    return temp_layout

def printLayout(lay):
    for x in range(0,4):
        print str(lay[x][0])+" "+str(lay[x][1])+" "+str(lay[x][2])+" "+str(lay[x][3])
    print "---------------------------------"


if __name__ == "__main__":
    while True:
        makeRandColor();
        makeX(randColor[0],randColor[1],randColor[2]);
        transitionX();
