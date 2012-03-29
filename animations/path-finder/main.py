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
bool_layout = [[True for col in range(4)] for row in range(4)]
max_x = 3
max_y = 3
out = FadeAnimation()
out.start()
rev_sleep_time = .5
frame_sleep_time = .3

def findPath():
    layout = [[bgColor for col in range(4)] for row in range(4)]
    bool_layout = [[True for col in range(4)] for row in range(4)]
    pos_x = random.randint(0,3)
    pos_y = random.randint(0,3)

    #some rigging
    if (pos_x == 1 and pos_y == 2):
        pos_x += 1
    if (pos_x == 3 and pos_y == 1):
        pos_y += 1

    randColor = random.sample(nice_pixels,5)
    col_chooser = 0
    col_chooser2 = 0
    col_chooser_max = random.randint(6,9)

    while True:
        #can go right
        if (pos_x < max_x and bool_layout[pos_x+1][pos_y]):
            pos_x = pos_x+1
        #can go down
        elif (pos_y < max_y and bool_layout[pos_x][pos_y+1]):
            pos_y = pos_y+1
        #can go left
        elif (pos_x > 0 and bool_layout[pos_x-1][pos_y]):
            pos_x = pos_x-1
        #can go up
        elif (pos_y > 0 and bool_layout[pos_x][pos_y-1]):
            pos_y = pos_y-1
        else:
            break
        col_chooser += 1
        bool_layout[pos_x][pos_y] = False
        layout[pos_x][pos_y] = transition_color(randColor[col_chooser2],randColor[col_chooser2+1],col_chooser,col_chooser_max)
        if(col_chooser == col_chooser_max):
            col_chooser = 0
            col_chooser2 += 1
        if (col_chooser2 == 3):
            col_chooser2 = 0



        #printLayout(layout)
        out.write(makeLayout(layout))
        time.sleep(frame_sleep_time)
    blink(randColor[4])


def blink(x):
    layout = [[x for col in range(4)] for row in range(4)]
    out.write(makeLayout(layout))
    time.sleep(1)

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

    #findPath()

    while True:
        findPath()
