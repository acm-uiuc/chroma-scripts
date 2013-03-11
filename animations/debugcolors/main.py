import sys
from animations import FadeAnimation
import colorsys


if __name__ == "__main__":
    import time
    out = FadeAnimation()
    out.FADERATE = 8.0
    out.start()

    hue = 0

    while True:
        for i in range(48):
            color = colorsys.hsv_to_rgb(hue,1,1)
            color = (color[0]*1023, color[1]*1023, color[2]*1023)
            pix = [color]*48
            out.write(pix)
            hue += 0.01
            if hue > 1: 
                hue = 0
            time.sleep(0.1)
            #time.sleep(0.2)
