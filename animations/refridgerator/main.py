import sys, random
sys.path.append("./osc")
from oscapi import ColorsOut

falloffRate = 7.0

#author: Robert Pieta
if __name__ == "__main__":
    import time
    out = ColorsOut()
    pix = [(0.0,0.0,0.0)] * 24
    runInAnimation = True
    smoothnessRatio = 110
    sleepTime = .01
    while True:
        if runInAnimation:
            for i in xrange(12):
                pix[random.randint(0,23)] = (0.0, 0.0, pix[i][2] + 1023/smoothnessRatio)
            out.write(pix)
            if pix[i][2] > 900:
                    runInAnimation = False
            time.sleep(sleepTime)
        else:
            for i in xrange(12):
                pix[random.randint(0,23)] = (0.0, 0.0, pix[i][2] - 1023/smoothnessRatio)
            out.write(pix)
            if pix[i][2] < 100.0:
                runInAnimation = True
            time.sleep(sleepTime)