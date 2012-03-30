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
    (0.0,0.0,1023.0),
    (0.0,1023.0,1023.0),
    (1023.0,0.,1023.0),
    (1023.0,1023.0,0.),    
    (823.0,823.0,0.0),
    (823.0,0.0,823.0),
    (0.0,823.0,823.0),    
]
bgColor=(0.0,0.0,0.0)
template = [[0,1,4,5],[2,3,6,7],[8,9,12,13],[10,11,14,15],[16,17,20,21],[18,19,22,23],[0,1,2,3,4,7,8,11,12,13,14,15],[5,6,9,10],]
out = FadeAnimation()
out.start()
layout = [bgColor]*24


def repeat(**options):
    times = 1
    n = 0
    if (options.get("times") > 1):
        times = options.get("times")
    if (options.get("frames")):
        while (n<times):
            options.get("frames")
            n+=1

# set color in box 1,2,3,4 with .4 second interval
def frame1():
    rand = random.sample(nice_pixels,5)
    layout = [rand[4]]*24
    out.write(layout)
    time.sleep(0.4)    
    for i in [0,1,3,2]:
        for j in range(4):
            layout[template[i][j]] = rand[i]
        #printlayout(layout)
        out.write(layout)
        time.sleep(0.4)


# set color outer box, then inner box .2 delay
def frame2():
    rand = random.sample(nice_pixels,3)
    layout = [rand[2]]*24
    for i in [6,7]:
        for j in range(len(template[i])):
            layout[template[i][j]] = rand[i-6]
        out.write(layout)
        time.sleep(0.2)




# spin colors at 5,6,9,10 at .1 second interval
def frame3():
    rand = random.sample(nice_pixels,5)
    layout = [rand[4]]*24
    #printlayout(layout)
    #out.write(layout)
    #time.sleep(0.4)  
    i = 0  
    for j in range(len(template[i])):

        #print "i= "+str(i)+" j ="+str(j)
        layout[template[7][j]] = rand[i]
        out.write(layout)
        time.sleep(0.1)
        i+=1
        #printlayout(layout)
        
# spin colors at 5,6,9,10 at .1 second interval
def frame3():
    rand = random.sample(nice_pixels,5)
    layout = [rand[4]]*24
    #printlayout(layout)
    #out.write(layout)
    #time.sleep(0.4)  
    i = 0  
    for j in range(len(template[i])):

        #print "i= "+str(i)+" j ="+str(j)
        layout[template[7][j]] = rand[i]
        out.write(layout)
        time.sleep(0.1)
        i+=1
        #printlayout(layout)

#spiral function from 0 to 9
def frame4():
    path = [0,1,2,3,7,11,15,14,13,12,8,4,5,6,10,9]
    
    rand = random.sample(nice_pixels,4)
    for i in range(len(path)):
        layout[path[i]] = rand[0]
        if (i != 0):
            layout[path[i-1]] = rand[1]
        # else:
        #     layout[path[len(path)-1]] = rand[1]
        #printlayout(layout)    
        out.write(layout)
        time.sleep(0.05)
    for i in range(len(path)):
        layout[path[len(path)-1-i]] = rand[2]
        if (i != 0):
            layout[path[len(path)-i]] = rand[3]
        # else:
        #     layout[path[len(path)-1]] = rand[1]
        #printlayout(layout)    
        out.write(layout)
        time.sleep(0.05)

def color_picker():
    r = random.random()*1000
    b, g = (0., 0.)
    while True:
        if (b > 1000):
            r = random.random()*1000
            b = 0
            g = random.random()*1000
        if (g > 1000):
            r = random.random()*1000
            b = random.random()*1000
            g = 0
        if (r > 1000):
            g = random.random()*1000
            b = random.random()*1000
            r = 0

        r+= 10.
        b+= 10.
        g+= 10.
        layout = [(r,g,b)]*24
        print (r,g,b)
        out.write(layout)
        time.sleep(.01)


def printlayout(layout):
    for i in range(0,5):
        print (str(layout[i*4+0])+ " " +str(layout[i*4+1])+ " " +str(layout[i*4+2])+ " " +str(layout[i*4+3]))
    print

if __name__ == "__main__":
    while True:
        frame1()
        frame2()
        frame3()
        frame4()
