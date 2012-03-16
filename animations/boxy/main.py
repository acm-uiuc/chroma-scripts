import sys
sys.path.append("./osc")
from oscapi import ColorsOut
import random
import math
import time


nice_pixels = [
    (1023.0,0.0,0.0),
    (0.0,1023.0,0.0),
    (0.0,0.0,1023.0),
    (823.0,823.0,0.0),
    (823.0,0.0,823.0),
    (0.0,823.0,823.0),
]
bgColor=(0.0,0.0,0.0)
template = [[0,1,4,5],[2,3,6,7],[8,9,12,13],[10,11,14,15],[16,17,20,21],[18,19,22,23],[0,1,2,3,4,7,8,11,12,13,14,15],[5,6,9,10],]
#inuse = [False] * 6
out = ColorsOut()


def repeat(**options):
    times = 1
    n = 0
    if (options.get("times") > 1):
        times = options.get("times")
    if (options.get("frames")):
        while (n<times):
            options.get("frames")
            n+=1

def frame1():
    layout = [random.choice(nice_pixels)]*24
    out.write(layout)
    for i in [0,1,3,2]:
        rand = random.choice(nice_pixels)

        for j in range(4):
            layout[template[i][j]] = rand
        #printlayout(layout)
        out.write(layout)
        time.sleep(0.2)


# def frame2():
#     layout = bgColor*24
#     for i in [0,1,3,4]:
#         rand = random.choice(nice_pixels)
#         for j in range(4):
#             layout[template[i][j]] = rand
#         out.write(layout)
#         time.sleep(0.2)

def printlayout(layout):
    for i in range(0,5):
        print (str(layout[i*4+0])+ " " +str(layout[i*4+1])+ " " +str(layout[i*4+2])+ " " +str(layout[i*4+3]))
    print 

if __name__ == "__main__":
    while True:
        frame1()
    #print "called"
