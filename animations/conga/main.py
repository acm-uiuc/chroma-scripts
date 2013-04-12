import sys, random, time
from oscapi import ColorsOut
from animations import FadeAnimation
    
lower = 500
##TODO: Make the colors not hideous
def main():
    out = ColorsOut()
    pix = [(0.0,0.0,0.0)]*48

    curr = 0
    r = (float)(random.randrange(lower, 1024))
    g = (float)(random.randrange(lower, 1024))
    b = (float)(random.randrange(lower, 1024))
    pix[curr] = (r, g, b)
    curr += 1
    out.write(pix)
    time.sleep(1)

    while True:
        while (curr < 47):
            r, g, b = colorAdd(r, g, b)
            pix[curr] = (r, g, b)
            out.write(pix)
            time.sleep(0.2)
            curr += 1
        while (curr > 0):
            r, g, b = colorAdd(r, g, b)
            pix[curr] = (r, g, b)
            out.write(pix)
            time.sleep(0.2)
            curr -= 1

def colorAdd(r, g, b):
    newR = (float)(random.randrange(-50, 50, 10))
    if newR + r < lower:
        r -= newR
    else:
        r += newR
    newG = (float)(random.randrange(-50, 50, 5))
    if newG + g < lower:
        g -= newG
    else:
        g += newG
    newB = (float)(random.randrange(-50, 50, 10))
    if newB + b < lower:
        b -= newB
    else:
        b += newB
    return (r, g, b)

if __name__ == "__main__":
    main()


