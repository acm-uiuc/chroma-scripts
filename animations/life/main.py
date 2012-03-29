#!/usr/bin/env python
import sys, random
from animations import FadeAnimation 

board = {}

def c(cell):
    n = [(cell[0]-1,cell[1]), (cell[0]-1,cell[1]-1),
         (cell[0],cell[1]-1), (cell[0]+1,cell[1]-1),
         (cell[0]+1,cell[1]), (cell[0]+1,cell[1]+1),
         (cell[0],cell[1]+1), (cell[0]-1,cell[1]+1)]
    count = 0
    for i in n:
        if i in board.keys():
            if board[i] in [1,-1]: count += 1
    return count

def update():
    for cell in board:
        n = c(cell)
        if board[cell] == 0 and n == 3:
            board[cell] = 2
        elif board[cell] == 1 and not n in [2,3]:
            board[cell] = -1
    for cell in board:
        if board[cell] == 2:
            board[cell] = 1
        if board[cell] == -1:
            board[cell] = 0

def init():
    for i in range(-3,10):
        for j in range(-3,10):
            if random.random() < 0.5:
                board[(i,j)] = 1
            else:
                board[(i,j)] = 0


if __name__ == "__main__":
    import time

    init()

    out = FadeAnimation()
    out.start()
    twoback = {}
    oldpix = {}
    while True:
        pix = []
        alive = 0
        for i in xrange(6):
            for j in xrange(4):
                if board[(i,j)] > 0:
                    pix.append((1023.0,0.0,0.0))
                    alive += 1
                else:
                    pix.append((0.0,0.0,1023.0))
        out.write(pix)
        update()
        time.sleep(0.3)
        if alive == 0 or oldpix == board or twoback == board:
            out.write([(0.0,1023.0,0.0)] * 24)
            time.sleep(0.4)
            init()
        twoback = oldpix.copy()
        oldpix = board.copy()

