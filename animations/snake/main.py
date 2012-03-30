import sys
from oscapi import ColorsOut


if __name__ == "__main__":
    import time
    out = ColorsOut()
    bgColor=(0.0,0.0,0.0)
    fgColor=(1023.0,0.0,0.0)
    pix = [bgColor]*24
    c = 0
    while True:
        for x in range(0,24):
            if( x == c ):
                pix[x] = fgColor
            else:
                pix[x] = bgColor
        out.write(pix)
        if( (0 <= c < 3) or (8 <= c < 11) or (16 <= c < 19) ):
            c += 1
        elif( (4 < c <= 7) or (12 < c <= 15) or (20 < c <= 23) ):
            c -= 1
        elif( (c == 3) or (c == 4) or (c == 11) or (c == 12) or (c == 19) ):
            c+=4
        elif( c == 20 ):
            c=0;
        time.sleep(0.2)
