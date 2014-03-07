import sys, random
from oscapi import ColorsOut

falloffRate = 7.0

#author: Robert Pieta
#modified by: Cole Gleason
if __name__ == "__main__":
    import time
    out = ColorsOut()
    pix = [(0.0,0.0,0.0)] * 48
    runInAnimation = True
    smoothnessRatio = 200
    sleepTime = .01
    while True:
        if runInAnimation:
            for i in xrange(12):
                pix[random.randint(0,47)] = (0.0, pix[i][0] + 1023/smoothnessRatio, 0.0)
            out.write(pix)
            if pix[i][1] > 900:
                    runInAnimation = False
            time.sleep(sleepTime)
        else:
            for i in xrange(12):
                pix[random.randint(0,47)] = (0.0, pix[i][0] - 1023/smoothnessRatio, 0.0)
            out.write(pix)
            if pix[i][1] < 100.0:
                runInAnimation = True
            time.sleep(sleepTime)
