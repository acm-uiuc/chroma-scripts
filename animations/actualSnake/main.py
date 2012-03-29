import sys, random
sys.path.append("./osc")
from oscapi import ColorsOut


if __name__ == "__main__":
    import time
    out = ColorsOut()
    pix = [(0.0,0.0,0.0)] * 24
    fadeConstant = 210.0
    sleepTime = 1.0
    newSnake = True
    lastLocation = 0
    lastDirection = 0
    while True:
        if newSnake:
            guess = random.randint(0,14)
            
            while guess == 5 or guess == 6 or guess == 9 or guess == 10:
                guess = random.randint(0, 14)
                
            newSnake = False
            
            pix[guess] = (1023.0, 0.0, 0.0)
            lastLocation = guess

                
        else:
            direction = random.randint(1,4)
            
            inValidDirection = True
            while inValidDirection:
                inValidDirection = False
                direction = random.randint(1,4)
                
                if direction == lastDirection:
                    inValidDirection = True
                
                if lastLocation % 4 == 3 and direction == 1:
                    inValidDirection = True
            
                if lastLocation % 4 == 0 and direction == 2:
                    inValidDirection = True
            
                if lastLocation < 4 and direction == 4:
                    inValidDirection = True
                        
                if lastLocation > 11 and direction == 3:
                    inValidDirection = True
                    
            if direction == 1:
                try:
                    pix[lastLocation + 1] = (1023.0, 0.0, 0.0) 
                    pix[lastLocation] = (pix[lastLocation][0] - fadeConstant, 0.0, 0.0)
                    lastLocation = lastLocation + 1
                    lastDirection = 2
                except IndexError:
                    pix[lastLocation] = (pix[lastLocation][0] - fadeConstant, 0.0, 0.0)
                    pass
            
            if direction == 2:
                try:
                    pix[lastLocation - 1] = (1023.0, 0.0, 0.0) 
                    pix[lastLocation] = (pix[lastLocation][0] - fadeConstant, 0.0, 0.0)
                    lastLocation = lastLocation - 1
                    lastDirection = 1
                except IndexError:
                    pix[lastLocation] = (pix[lastLocation][0] - fadeConstant, 0.0, 0.0)
                    pass
                        
            if direction == 3:
                try:
                    pix[lastLocation + 4] = (1023.0, 0.0, 0.0) 
                    pix[lastLocation] = (pix[lastLocation][0] - fadeConstant, 0.0, 0.0)
                    lastLocation = lastLocation + 4
                    lastDirection = 4
                except IndexError:
                    pix[lastLocation] = (pix[lastLocation][0] - fadeConstant, 0.0, 0.0)
                    pass
        
            if direction == 4:
                try:
                    pix[lastLocation - 4] = (1023.0, 0.0, 0.0) 
                    pix[lastLocation] = (pix[lastLocation][0] - fadeConstant, 0.0, 0.0)
                    lastLocation = lastLocation - 4
                    lastDirection = 3
                except IndexError:
                    pix[lastLocation] = (pix[lastLocation][0] - fadeConstant, 0.0, 0.0)
                    pass
                
        allDark = True
        for i in xrange(24):
            if pix[i][0] > 0 and i != lastLocation:
               pix[i] = (pix[i][0] - fadeConstant, 0.0, 0.0)
            if pix[i][0] > 2: allDark = False  

        if allDark: newSnake = True

        out.write(pix)
        time.sleep(sleepTime)