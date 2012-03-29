import sys, random
import time
import colorsys
sys.path.append("./osc")
from oscapi import ColorsOut
from animations import FadeAnimation



falloffRate = 1.7

if __name__ == "__main__":
    out = ColorsOut()
    hsv    = [(0.0,0.0,0.0)] * 24
    hsv01  = [(0.0,0.0,0.0)] * 24
    rgb01  = [(0.0,0.0,0.0)] * 24
    pixOut = [(0.0,0.0,0.0)] * 24
    numIterations = 0
    while True:
        numIterations += 1
        if (numIterations % 20) == 0:
            for i in xrange(24):
                hsv[i] = (random.gauss(31.0,5.0) % 360,random.randint(30,100),random.randint(95,100))
        
        for i in xrange(24):
            hsv[i] = (hsv[i][0],hsv[i][1]-falloffRate,hsv[i][2])
            
        # Convert from hsv to 10 bit rgb:
        for i in xrange(24):
            hue = hsv[i][0] * 1.0 / 360.0
            sat = hsv[i][1] * 1.0 / 100.0
            lum = hsv[i][2] * 1.0 / 100.0
            
            hsv01[i] = (hue,sat,lum)
            
            rgb01[i] = colorsys.hsv_to_rgb(hsv01[i][0],hsv01[i][1],hsv01[i][2])
            
            pixOut[i] = (rgb01[i][0] * (1023.0),rgb01[i][1] * (1023.0),rgb01[i][2] * (1023.0))
        
        out.write(pixOut)
        time.sleep(0.02)
