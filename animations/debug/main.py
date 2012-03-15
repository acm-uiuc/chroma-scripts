import sys
sys.path.append("./osc")
from oscapi import ColorsOut


if __name__ == "__main__":
    import time
    out = ColorsOut()

    while True:
        for i in range(24):
            pix = [(0.0,0.0,0.0)]*24
            if i%8 == 0:
                pix[i] = (1023.0,0.0,0.0)
            else:
                pix[i] = (0.0,1023.0,1023.0)
            out.write(pix)
            #time.sleep(1.0)
            time.sleep(0.2)
