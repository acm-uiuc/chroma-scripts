import sys, random
sys.path.append("./osc")
from oscapi import ColorsOut

#author: Robert Pieta
if __name__ == "__main__":
    import time
    out = ColorsOut()
    pix = [(0.0,0.0,0.0)] * 24
    fallRate = 7.0
    sleepTimer = 0.02
    frameMax = 40
    frames = 0
    for i in xrange(24):    
        pix[i] = (0.0 , 0.0, 0.0)

    while True:
        if frames < 0:
            pix[random.randint(0, 23.0)] = (1023.0, 1023.0, 1023.0)
            frames = random.randint(0, frameMax)
        
        else:
            frames = frames - 1

        out.write(pix)

        for i in xrange(24):
            pix[i] = (pix[i][0] - fallRate, pix[i][1] - fallRate, pix[i][2] - fallRate)

        time.sleep(sleepTimer)