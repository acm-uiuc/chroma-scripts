import sys
from animations import FadeAnimation
from math import sin, radians, degrees
from colorsys import hsv_to_rgb

speed = 40.0

if __name__ == "__main__":
    import time
    out = FadeAnimation()
    out.FADERATE = 1.0 # seconds
    out.start()

    counter = 0.0

    while True:
        pix = [(0.0,0.0,0.0)]*24
        for i in range(4):
            for j in range(4):
                rgb = hsv_to_rgb((sin(radians(counter)/2.0+float(i)/6.0)+1.0)/2.0, 1.0, 1.0)
                pix[i*4+j] = (rgb[0]*1023.0, rgb[1]*1023.0, rgb[2]*1023.0)
        out.write(pix)
        time.sleep(1.0/speed)
        counter += 0.8
