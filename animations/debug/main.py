import sys
from animations import FadeAnimation


if __name__ == "__main__":
    import time
    out = FadeAnimation()
    out.FADERATE = 8.0
    out.start()

    while True:
        for i in range(24):
            pix = [(0.0,0.0,0.0)]*24
            if i%8 == 0:
                pix[i] = (1023.0,0.0,0.0)
            else:
                pix[i] = (0.0,1023.0,1023.0)
            out.write(pix)
            time.sleep(0.7)
            #time.sleep(0.2)
