import sys
from oscapi import ColorsOut
import random
import math
import time
from animations import FadeAnimation 
import operator

#author: Harsh Singh
red = (1023.0,0.0,0.0)
yello = (1023.0,1023.0,0)

bgColor=(0.0,0.0,0.0)
layout = [[bgColor for col in range(4)] for row in range(4)]
out = FadeAnimation()
out.start()

def well():
    global layout
    times = 40
    for a in xrange(times):
        for x in xrange(4):
            for y in xrange(4):
                if (0<x<3 and 0<y<3):
                    layout[x][y] = transition_color(red, yello, a, times)
                else:
                    layout[x][y] = transition_color(yello, red, a, times)
        out.write(makeLayout(layout))
        time.sleep(.05)
    for a in xrange(times):
        for x in xrange(4):
            for y in xrange(4):
                if (0<x<3 and 0<y<3):
                    layout[x][y] = transition_color(yello, red, a, times)
                else:
                    layout[x][y] = transition_color(red, yello, a, times)
        out.write(makeLayout(layout))
        time.sleep(.05)

def transition_color(col1, col2, step, steps):
    step +=1
    col1 = tuple( [ int( e- (e * step/steps) ) for e in col1 ] )
    col2 = tuple( [ int( e*step/steps ) for e in col2 ] )
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
        well()
