import sys, random
from oscapi import ColorsOut

falloffRate = 7.0

#author: Robert Pieta
if __name__ == "__main__":
    import time
    out = ColorsOut()
    pix = [(0.0,0.0,0.0)] * 24
    runInAnimation = True
    smoothnessRatio = 200
    sleepTime = .01
    while True:
        # Make some rain
        #    if random.randint(0,5) < 3:
        #   pix[random.randint(0,23)] = (random.randint(0,1023.0),random.randint(0,1023.0),random.randint(0,1023.0))
        #out.write(pix)
        #for i in xrange(24):
        #   if pix[i][2] > 0.0:
        #       pix[i] = (pix[i][0] - falloffRate, pix[i][1] - falloffRate,pix[i][2] - falloffRate)
        #else:
        #       pix[i] = (0.0,0.0,0.0)
        if runInAnimation:
            for i in xrange(12):
                pix[random.randint(0,23)] = (pix[i][0] + 1023/smoothnessRatio, 0.0, 0.0)
            out.write(pix)
            if pix[i][0] > 900:
                    runInAnimation = False
            time.sleep(sleepTime)
        else:
            for i in xrange(12):
                pix[random.randint(0,23)] = (pix[i][0] - 1023/smoothnessRatio, 0.0, 0.0)
            out.write(pix)
            if pix[i][0] < 100.0:
                runInAnimation = True
            time.sleep(sleepTime)
