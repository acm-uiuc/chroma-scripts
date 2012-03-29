import sys, random
import time
import colorsys
from math import floor
sys.path.append("./osc")
from oscapi import ColorsOut
from animations import FadeAnimation

fps = 60.0

# numerical rate is in % points/second
falloffRate = 20.0 /fps

if __name__ == "__main__":
    # writing pixel values every time:
    out = ColorsOut()
    
    # yeah I know it's an inefficient use of space, but hey, it's constant space!
    hsv    = [(0.0,0.0,0.0,0.0)] * 24
    # because hsv_to_rgb takes values scaled from 0-1
    hsv01  = [(0.0,0.0,0.0)] * 24
    # because hsv_to_rgb returns values scaled from 0-1
    rgb01  = [(0.0,0.0,0.0)] * 24
    # because ColorsOut() is of course, 10-bit rgb
    pixOut = [(0.0,0.0,0.0)] * 24
    
    # main loop:
    while True:
        # using Kevin's "raindrop" algorithm:
        if random.randint(0,5) < 4:
            i = random.randint(0,23)
            
            # make so that a pixel never gets replaced by one of lower saturation:
            floorOfSat = floor(max(40,hsv[i][1]))
            sat = random.randint(floorOfSat,100)
            
            #secs = time.localtime().tm_sec
            hue = random.gauss(37.0,5.0) % 360
            lum = random.randint(95,100)
            fun = 0.0
            
            hsv[i] = (hue,sat,lum,fun)
        
        # make the saturation fall out with time
        # (could do something with hue and luminance too):
        for i in xrange(24):
            hue = hsv[i][0]
            sat = hsv[i][1] - falloffRate
            lum = hsv[i][2]
            fun = hsv[i][3]
            
            hsv[i] = (hue,sat,lum,fun)
            
        # Convert from hsv to 10 bit rgb:
        for i in xrange(24):
            hue = hsv[i][0] * 1.0 / 360.0
            sat = hsv[i][1] * 1.0 / 100.0
            lum = hsv[i][2] * 1.0 / 100.0
            
            hsv01[i] = (hue,sat,lum)
            
            rgb01[i] = colorsys.hsv_to_rgb(hsv01[i][0],hsv01[i][1],hsv01[i][2])
            
            pixOut[i] = (rgb01[i][0] *1023.0,rgb01[i][1] *1023.0,rgb01[i][2] *1023.0)
        
        out.write(pixOut)
        time.sleep(1.0/fps)
