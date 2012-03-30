#!/usr/bin/env python
import math
import random
import sys
from oscapi import ColorsOut

board = {}

# based on http://processing.org/learning/topics/plasma.html

def update(t):
    calc1 = math.sin(t * 0.61655617)
    calc2 = math.sin(t * -3.6352262)
    for cell in board:
        x, y = cell
        x = 25 + 2 * x
        y = 25 + 2 * y
        s1 = .5 + .5 * math.sin(x * calc1)
        s2 = .5 + .5 * math.sin(y * calc2)
        s3 = .5 + .5 * math.sin((x + y + 5 * t) / 2)
        s = (s1 + s2 + s3) / 3
        board[cell] = (s, 1 - s / 2, 1)

def init():
    for i in range(6):
        for j in range(4):
            board[(i,j)] = 1

def hsv_to_rgb(h, s, v):
    f = h / 60 - int(h / 60)
    p = int(255 * v * (1 - s))
    q = int(255 * v * (1 - s * f))
    t = int(255 * v * (1 - s* (1 - f)))
    v = int(255 * v)
    return ((v, t, p),
            (q, v, p),
            (p, v, t),
            (p, q, v),
            (t, p, v),
            (v, p, q))[int(h / 60) % 6]

if __name__ == "__main__":
    import time
    start = time.time()
    init()
    out = ColorsOut()
    while True:
        pix = []
        update((time.time() - start) * .03 + 10)
        for i in xrange(6):
            for j in xrange(4):
                h, s, v = board[(i, j)]
                r, g, b = hsv_to_rgb(h * 360., s, v)
                # print board[(i, j)],r, g, b
                pix.append((r * 4., g * 4., b * 4.))
        out.write(pix)
        time.sleep(1/30.)
