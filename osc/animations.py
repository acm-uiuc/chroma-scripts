import threading
from oscapi import ColorsOut
import time


"""
FadeAnimation:
    basically just fades pixels in and out

    FADEINRATE is the (invese) rate in which things fade in (to a larger value).  1 is instant, > 1 gets slower and slower
    FADEINRATE is the (invese) rate in which things fade out (to a smaller value).  1 is instant, > 1 gets slower and slower
"""
class FadeAnimation(threading.Thread):
    curcolors = [(0.0,0.0,0.0)]*24
    targetcolors= [(0.0,0.0,0.0)]*24
    FADEINRATE = 3.0
    FADEOUTRATE = 3.0
    FRAMERATE = 30.0
    dorun = True

    def __init__(self):
        threading.Thread.__init__(self)
        self.out = ColorsOut()

    def write(self, pixels):
        self.targetcolors = pixels[:]

    def run(self):
        while self.dorun:
            self.curcolors = self.animate(self.curcolors, self.targetcolors)
            self.out.write(self.curcolors)
            time.sleep(1.0/self.FRAMERATE)

    def animate(self, pixels, pixelsmod):
        for index,pixel in enumerate(pixelsmod):
            pixels[index] = self.animatePixel(pixels[index], pixel)
        #pixels = pixelsmod[:]
        return pixels 

    def animatePixel(self,pixel, pixelmod):
        (r,g,b) = pixel
        (s,t,q) = pixelmod
        rdiff = (s-r)/(self.FADEINRATE if s-r > 0 else self.FADEOUTRATE)
        r = r + rdiff 
        gdiff = (t-g)/(self.FADEINRATE if t-g > 0 else self.FADEOUTRATE)
        g = g + gdiff 
        bdiff = (q-b)/(self.FADEINRATE if q-b > 0 else self.FADEOUTRATE)
        b = b + bdiff
        return (r,g,b)
