import sys
from animations import FadeAnimation


if __name__ == "__main__":
    import time
    import random

    stepDelay = 0.7
    stepFadeRate = 8
    fadeFadeRate = 20
    
    out = FadeAnimation()
    out.FADERATE = stepFadeRate
    out.start()
    pix = [(0.0,0.0,0.0)]*24
    colors = [(700.,0.,0.),
              (0.,700.,0.),
              (0.,0.,700.),
              (700.,700.,0.),
              (700.,0.,700.),
              (0.,700.,700.)
              ]
    path = [0,1,2,3,7,11,15,14,13,12,8,4,5,6,10,9]
    
    
    randOrder = random.sample(colors,len(colors))
    orderCount=0

    while True:
        for i in xrange(16):
            if i > 0:
                for j in xrange(i,0,-1):
                    pix[path[j]] = pix[path[j-1]]
            
            pix[0]=randOrder[orderCount]
            orderCount+=1
            if orderCount == len(colors):
                orderCount=0

            
            out.write(pix)
            time.sleep(stepDelay)
			
	    if i == 15:
	    	pix = [(0.0,0.0,0.0)]*24
    		out.FADERATE = fadeFadeRate
    		out.write(pix)
    		out.FADERATE = stepFadeRate
    		randOrder = random.sample(colors,len(colors))
                time.sleep(stepDelay)
