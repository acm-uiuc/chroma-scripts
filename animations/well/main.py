import sys
sys.path.append("./osc")
from oscapi import ColorsOut
import random
import math
import time
from animations import FadeAnimation 
import operator

#NOTE: This is some pretty shitty code i hacked up. Don't use it as an example, still a work in progress

#author: Harsh Singh
cool_trans = [[(1023.0,0.0,0.0),(1023.0,1023.0,0)], [(0.0,0.0,1023.0),(1023.0,0,1023.0)]]

bgColor=(0.0,0.0,0.0)
layout = [[bgColor for col in range(4)] for row in range(4)]
out = FadeAnimation()
out.start()
times = 30

def well(col1, col2):
    global layout

    for a in xrange(times):
        set_layout(col1, col2, a, times)
        out.write(makeLayout(layout))
        time.sleep(.05)
    for a in xrange(times):
        set_layout(col2, col1, a, times)
        out.write(makeLayout(layout))
        time.sleep(.05)

def fade_out():
    for a in xrange(times):
        for x in xrange(4):
            for y in xrange(4):
                layout[x][y] = transition_color(layout[x][y], bgColor, a, times)
        out.write(makeLayout(layout))
        time.sleep(.05)

def fade_in():
 
    for a in xrange(times):
        for x in xrange(4):
            for y in xrange(4):
                layout[x][y] = transition_color(bgColor, layout[x][y], a, times)
        printLayout(layout)
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

def set_layout(col1, col2, a, times):

    for x in xrange(4):
        for y in xrange(4):
            if (0<x<3 and 0<y<3):
                layout[x][y] = transition_color(col1, col2, a, times)
            else:
                layout[x][y] = transition_color(col2, col1, a, times)

if __name__ == "__main__":
    while True:
        well(cool_trans[0][0], cool_trans[0][1])
        # fade_out()
        # set_layout(cool_trans[1][0], cool_trans[1][1], 4, 4)
        # fade_in()
        # well(cool_trans[1][0], cool_trans[1][1])