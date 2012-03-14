import sys
sys.path.append("./osc")
from osc import ColorsOut


def printHelp():
    print """debugLights.py [debug type] [animation time] [other]
    debug type: sweep, pattern, solid
    animation time: time in ms between frames
    other: for solid, the color to be displayed.  RGB, 0-1023
    """


if __name__ == "__main__":
    import time
    out = ColorsOut()

    if len(sys.argv) < 2:
        printHelp()

    elif sys.argv[1] == "sweep":
        while True:
            for i in range(24):
                pix = [(0.0,0.0,0.0)]*24
                if i%8 == 0:
                    pix[i] = (1023,0,0)
                else:
                    pix[i] = (0,1023,1023)
                out.write(pix)
                #time.sleep(1.0)
                time.sleep(float(sys.argv[2]))
    elif sys.argv[1] == "pattern":
        lightspattern = [
                (1023,0,0),
                (1023,1023,0),
                (523,1023,0),
                (0,1023,0),
                (0,1023,1023),
                (0,523,1023),
                (0,0,1023),
                (1023,0,1023),
                ]
        while True:
            pix = [(0.0,0.0,0.0)]*24
            for i in range(24):
                pix[i] = lightspattern[i%8]
            out.write(pix)
            #time.sleep(1.0)
            time.sleep(float(sys.argv[2]))
    elif sys.argv[1] == "solid":
        color = (float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]))
        while True:
            pix = [(0.0,0.0,0.0)]*24
            for i in range(24):
                pix[i] = color
            out.write(pix)
            #time.sleep(1.0)
            time.sleep(float(sys.argv[2]))
    else:
        printHelp()
