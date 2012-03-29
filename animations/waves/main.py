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
    smRBase = 100.0
    smR = 100.0
    sleepTime = 0.19
    color1 = (500.0,500.0,500.0)
    color2 = (0.0,0.0,0.0)
    color3 = (0.0,0.0,0.0)
    color4 = (0.0,0.0,0.0)
    stage = 0
    reg = 1
    
    lowTol = 100
    highTol = 900
    for i in xrange(24):
        pix[i] = (0.0, 0.0, 0.0)
    out.write(pix)
    
    while True:
        color4 = color3
        color3 = color2
        color2 = color1
        
        guess = random.randint(0, 10)
        if guess > 5: 
            guess = 1
            smR = smRBase
        
        else: 
            guess = -1
            smR = smRBase
        
        if color1[0] < lowTol or color1[1] < lowTol or color1[2] < lowTol:
            guess = 1
            smR = 3*smRBase
        
        if color1[0] > highTol or color1[1] > highTol or color1[2] > highTol:
            guess = -1
            smR = 3*smRBase
        
        color1 = (color1[0] + guess*random.randint(0, smR),color1[1] + guess*random.randint(0, smR) + guess*color1[0]/100, color1[2] + guess*random.randint(0, smR)+ guess*color1[2]/100)
        

        
        pix[0] = color1
        
        pix[4] = color2
        pix[5] = color2
        pix[1] = color2
        
        pix[8] = color3
        pix[9] = color3
        pix[10] = color3
        pix[6] = color3
        pix[2] = color3
        
        pix[12] = color4
        pix[13] = color4
        pix[14] = color4
        pix[15] = color4
        pix[11] = color4
        pix[7] = color4
        pix[3] = color4

        out.write(pix)
        time.sleep(sleepTime)