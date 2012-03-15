import threading
from oscapi import ColorsOut
import time


class FadeAnimation(threading.Thread):
    curcolors = [(0.0,0.0,0.0)]*24
    targetcolors= [(0.0,0.0,0.0)]*24
    CHANGERATE = 3.0
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
        r = r + (s-r)/self.CHANGERATE
        g = g + (t-g)/self.CHANGERATE
        b = b + (q-b)/self.CHANGERATE
        return (r,g,b)
