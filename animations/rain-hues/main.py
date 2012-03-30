import sys, random
import time
import colorsys
from math import floor, sin
sys.path.append("./osc")
from oscapi import ColorsOut
from animations import FadeAnimation

MAX_BULBS = 24

fps = 30.0

# numerical rate is in % points/second
falloffRate = (360.0/11.0) /fps

if __name__ == "__main__":
    # writing pixel values every time:
    out = ColorsOut()
    
    # yeah I know it's an inefficient use of space, but hey, it's constant space!
    hsv    = [(0.0,0.0,0.0,0.0)] * MAX_BULBS
    # because hsv_to_rgb takes values scaled from 0-1
    hsv01  = [(0.0,0.0,0.0)] * MAX_BULBS
    # because hsv_to_rgb returns values scaled from 0-1
    rgb01  = [(0.0,0.0,0.0)] * MAX_BULBS
    # because ColorsOut() is of course, 10-bit rgb
    pixOut = [(0.0,0.0,0.0)] * MAX_BULBS
    
    # basically a function that puts the outer loop values in order:
    outerLoop = (0,1,2,3,7,11,15,14,13,12,8,4)
    
    loopCounter = 0
    # main loop:
    while True:
        loopCounter += 1
    
        secHand = time.localtime().tm_sec
        minHand = time.localtime().tm_min
        ourHand = time.localtime().tm_hour
        weekDay = time.localtime().tm_wday
        
        hue = 0.0
        sat = 100
        lum = 100
        fun = 0.0
    
        hsv[outerLoop[secHand %12]] = (hue,sat,lum,fun)
    
        # make the saturation fall out with time
        for i in xrange(MAX_BULBS):
            hue = hsv[i][0] - falloffRate
            sat = abs(40 *sin(loopCounter /fps)) + 60
            lum = hsv[i][2]
            fun = hsv[i][3]
            
            hsv[i] = (hue,sat,lum,fun)
        
        
        
        # --------------------------------------------------------------------------
        # Everything below this is strictly utilitarian (changing hsv to 10bit rgb):
        # --------------------------------------------------------------------------
        
        # Convert from hsv to 10 bit rgb:
        for i in xrange(MAX_BULBS):
            hue = (hsv[i][0] %360) * 1.0 / 360.0
            sat = min(100,abs(hsv[i][1])) * 1.0 / 100.0
            lum = min(100,abs(hsv[i][2])) * 1.0 / 100.0
            
            hsv01[i] = (hue,sat,lum)
            
            rgb01[i] = colorsys.hsv_to_rgb(hsv01[i][0],hsv01[i][1],hsv01[i][2])
            
            pixOut[i] = (rgb01[i][0] *1023.0,rgb01[i][1] *1023.0,rgb01[i][2] *1023.0)
        
        out.write(pixOut)
        time.sleep(1.0/fps)


