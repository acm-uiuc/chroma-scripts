import sys, random
from oscapi import ColorsOut

falloffRate = 7.0

if __name__ == "__main__":
    import time
    out = ColorsOut()
    pix = [(0.0,0.0,0.0)] * 24
    while True:
        # Make some rain
        if random.randint(0,5) < 3:
            pix[random.randint(0,23)] = (0.0,0.0,1023.0)
        out.write(pix)
        for i in xrange(24):
            if pix[i][2] > 0.0:
                pix[i] = (0.0,0.0,pix[i][2] - falloffRate)
            else:
                pix[i] = (0.0,0.0,0.0)
        time.sleep(0.02)
