import sys
from oscapi import ColorsOut


if __name__ == "__main__":
    import time
    out = ColorsOut()
    r = 255.0
    g = 255.0
    b = 255.0
    #r = 60.0
    #g = 255.0
    #b = 70.0
    while True:
        pix = [(4.0 * r, 4.0 * g, 4.0 * b)] * 24
        out.write(pix)
        time.sleep(0.2)
