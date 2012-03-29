import sys
sys.path.append("./osc")
from animations import FadeAnimation


if __name__ == "__main__":
    import time
    out = FadeAnimation()
    out.FADERATE = 32.0
    out.start()
    
    pix = [(1023.0,1023.0,1023.0)]*24
    path = [0,1,2,3,7,11,15,14,13,12,8,4]
    
    sleeptime = 0.02
    
    counter = 1
    while True:
        for i in range(len(path)):
            counter = counter + 1
            pix[path[i]] = (1023.0,0.0,0.0)
            pix[path[i-1]] = (511.5,511.5,0.0)
            pix[path[i-2]] = (0.0,1023.0,0.0)
            pix[path[i-3]] = (0.0,511.5,511.5)
            pix[path[i-4]] = (0.0,0.0,1023.0)
            pix[path[i-5]] = (511.5,0.0,511.5)
            pix[path[i-6]] = (1023.0,1023.0,1023.0)
            out.write(pix)
            sleeptime = sleeptime + 0.002
            time.sleep(sleeptime)
