import sys
sys.path.append("./osc")
from animations import FadeAnimation


if __name__ == "__main__":
    import time
    out = FadeAnimation()
    out.FADERATE = 32.0
    out.start()
    
    pix = [(1023.0,1023.0,1023.0)]*48
    path = [0,1,2,3,4,5,11,17,23,29,35,41,47,46,45,44,43,42,36,30,24,18,12,6]
    
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
