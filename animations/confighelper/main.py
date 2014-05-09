import sys
from oscapi import ColorsOut 
import config


selected = 0



class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()




if __name__ == "__main__":
    import time
    out = ColorsOut()
    #out.FADERATE = 8.0
    #out.start()

    s = 's'
    while s:
        pix = [(0.0,0.0,0.0)]*48
        pix[selected] = (1023.0,1023.0,1023.0)
        out.write(pix)
        print "enter 'r' to move right, 'l' to move left, enter to stop: "
        s = getch()
        s = s.strip()
        if s == 'l':
            selected = (selected - 1)%48
        if s == 'r':
            selected = (selected + 1)%48
        print 'selected light: '+str(selected)+' and the octobar index it maps to: '+str(config.order[selected])
