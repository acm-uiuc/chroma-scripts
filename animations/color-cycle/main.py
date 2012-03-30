import sys
from oscapi import ColorsOut


if __name__ == "__main__":
    import time
    out = ColorsOut()
    hue = 0.0
    while True:
        pix = []
        c = 1.0
        x = c * (1.0 - abs(hue % 2.0 - 1.0))
        if hue > 6.0:
            hue = 0.0
        if hue < 1.0:
            pix = [(1023.0 * c,1023.0 * x,0.0)]*24
        elif hue < 2.0:
            pix = [(1023.0 * x,1023.0 * c,0.0)]*24
        elif hue < 3.0:
            pix = [(0.0,1023.0 * c,1023.0 * x)]*24
        elif hue < 4.0:
            pix = [(0.0,1023.0 * x,1023.0 * c)]*24
        elif hue < 5.0:
            pix = [(1023.0 * x,0.0,1023.0 * c)]*24
        elif hue < 6.0:
            pix = [(1023.0 * c,0.0,1023.0 * x)]*24
        out.write(pix)
        hue += 0.02
        print pix[0]
        time.sleep(0.1)
