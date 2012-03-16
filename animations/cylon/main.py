#!/usr/bin/env python
import sys, random
sys.path.append("./osc")
from animations import FadeAnimation 

if __name__ == "__main__":
    import time

    out = FadeAnimation()
    out.start()
    n = 0
    while True:
        pix = []
        alive = 0
        if n == 4:
            n == 0
        for i in xrange(6):
            for j in xrange(4):
                if j == n:
                    pix.append((1023.0,0.0,0.0))
                else:
                    pix.append((0.0,0.0,0.0))
        out.write(pix)
        time.sleep(0.3)
        n += 1

