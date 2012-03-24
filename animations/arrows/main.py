import sys
sys.path.append("./osc")
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
out = FadeAnimation()
out.start()


def frame1():
    randColor = random.sample(nice_pixels,3)
    lastColor = randColor[2]
    for x in range(0,4):
        mycol = transition_color(randColor[0],randColor[1],x,4)
        for i in range(0,4):
            for j in range(0,4):
                if ((i == x and j <= x) or (i< x and j == x)):                    
                    layout[i][j] = mycol
        out.write(makeLayout(layout))
        time.sleep(.2)
    frame1_rev(lastColor)

def frame1_rev(lastColor):
    layout = [[bgColor for col in range(4)] for row in range(4)]
    for x in range(3,-1,-1):
        for i in range(3,-1,-1):
            for j in range(3,-1,-1):
                if ((i == x and j <= x) or (i< x and j == x)):                    
                    layout[i][j] = lastColor
        out.write(makeLayout(layout))
        time.sleep(.1)

def frame2():
    randColor = random.sample(nice_pixels,3)
    lastColor = randColor[2]
    for x in range(3,-1,-1):
        mycol = transition_color(randColor[0],randColor[1],x,4)
        for i in range(3,-1,-1):
            for j in range(3,-1,-1):
                if ((i == x and j >= x) or (i> x and j == x)):                    
                    layout[i][j] = mycol
        out.write(makeLayout(layout))
        time.sleep(.2)
    frame2_rev(lastColor)

def frame2_rev(lastColor):
    layout = [[bgColor for col in range(4)] for row in range(4)]
    for x in range(0,4):
        for i in range(0,4):
            for j in range(0,4):
                if ((i == x and j >= x) or (i> x and j == x)):                    
                    layout[i][j] = lastColor
        out.write(makeLayout(layout))
        time.sleep(.1)

def blink():
    x = random.choice(nice_pixels)
    layout = [[x for col in range(4)] for row in range(4)]
    out.write(makeLayout(layout))
    time.sleep(1)

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
    # frame1()
    # frame2()


    while True:
        frame1()
        frame2()