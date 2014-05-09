import sys
from oscapi import ColorsOut
import random
import math

steps = 24
time_per_cycle = 3.0
real_steps = steps * time_per_cycle

nice_pixels = [
    (1023,0,0),
    (0,1023,0),
    (0,0,1023),
    (823,823,0),
    (823,0,823),
    (0,823,823),
]

if __name__ == "__main__":
    import time
    out = ColorsOut()
    pix_A = [(0.0,0.0,0.0)]*24
    pix_B = [(0.0,0.0,0.0)]*24
    while True:
        pix_A = pix_B[:]
        for i in range(24):
            while pix_B[i] == pix_A[i]:
                pix_B[i] = random.choice(nice_pixels)
        
        pix = [(0.0,0.0,0.0)]*24
        for i in range(int(real_steps+1)):
            d = float(i)/float(real_steps)
            d = math.sin(d * math.pi * 0.5)
            dp = 1-d
            for j in range(24):
                (r1,g1,b1) = pix_A[j]
                (r2,g2,b2) = pix_B[j]
                pix[j] = (r1*dp + r2*d, g1*dp + g2*d, b1*dp + b2*d)
            out.write(pix)
            #time.sleep(1.0)
            time.sleep(1.0/steps)
