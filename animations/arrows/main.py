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
out = FadeAnimation()
out.start()
rev_sleep_time = .2
frame_sleep_time = .7


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
        time.sleep(frame_sleep_time)
    frame1_rev(lastColor)

def frame1_rev(lastColor):
    global layout
    layout = [[bgColor for col in range(4)] for row in range(4)]
    for x in range(3,-1,-1):
        for i in range(0,4):
            for j in range(0,4):
                if ((i == x and j <= x) or (i< x and j == x)):                    
                    layout[i][j] = lastColor
        out.write(makeLayout(layout))
        time.sleep(rev_sleep_time)

def frame2():
    randColor = random.sample(nice_pixels,3)
    lastColor = randColor[2]
    for x in range(3,-1,-1):
        mycol = transition_color(randColor[0],randColor[1],x,4)
        for i in range(0,4):
            for j in range(0,4):
                if ((i == x and j >= x) or (i> x and j == x)):                    
                    layout[i][j] = mycol
        out.write(makeLayout(layout))
        time.sleep(frame_sleep_time)
    frame2_rev(lastColor)

def frame2_rev(lastColor):
    global layout 
    layout = [[bgColor for col in range(4)] for row in range(4)]
    for x in range(0,4):
        for i in range(0,4):
            for j in range(0,4):
                if ((i == x and j >= x) or (i> x and j == x)):                    
                    layout[i][j] = lastColor
        out.write(makeLayout(layout))
        time.sleep(rev_sleep_time)

def frame3():
    randColor = random.sample(nice_pixels,3)
    lastColor = randColor[2]
    for x in range(3,-1,-1):
        mycol = transition_color(randColor[0],randColor[1],x,4)
        for i in range(0,4):
            for j in range(0,4):
                if ((i == x and j <= 3-x) or (i> x and j == 3-x)):                    
                    layout[i][j] = mycol
        out.write(makeLayout(layout))
        time.sleep(frame_sleep_time)
    frame3_rev(lastColor)

def frame3_rev(lastColor):
    global layout
    layout = [[bgColor for col in range(4)] for row in range(4)]
    for x in range(0,4):
        for i in range(0,4):
            for j in range(0,4):
                if ((i == x and j <= 3-x) or (i> x and j == 3-x)):                    
                    layout[i][j] = lastColor
        out.write(makeLayout(layout))
        time.sleep(rev_sleep_time)

def frame4():
    randColor = random.sample(nice_pixels,3)
    lastColor = randColor[2]
    for x in range(0,4):
        mycol = transition_color(randColor[0],randColor[1],x,4)
        for i in range(0,4):
            for j in range(0,4):
                if ((i == x and j >= 3-x) or (i< x and j == 3-x)):                    
                    layout[i][j] = mycol
        out.write(makeLayout(layout))
        time.sleep(frame_sleep_time)
    frame4_rev(lastColor)

def frame4_rev(lastColor):
    global layout
    layout = [[bgColor for col in range(4)] for row in range(4)]
    for x in range(3,-1,-1):
        for i in range(0,4):
            for j in range(0,4):
                if ((i == x and j >= 3-x) or (i< x and j == 3-x)):                    
                    layout[i][j] = lastColor
        out.write(makeLayout(layout))
        time.sleep(rev_sleep_time)

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
    # frame4()

    while True:
        frame1()
        frame2()
        frame3()
        frame4()
        # f = random.randint(1,4)
        # if f == 1:
        #     frame1()
        # elif f == 2:
        #     frame2()
        # elif f == 3: 
        #     frame3()
        # else:
        #     frame4()