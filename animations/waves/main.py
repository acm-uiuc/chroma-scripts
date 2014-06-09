import sys
from random import randint, gammavariate
from animations import FadeAnimation
from math import sin, radians, degrees
from colorsys import hsv_to_rgb
speed = 40.0
light_count = 48


def randomness():
    return 1. if randint(1, 9*15*5) != 1 else 2

if __name__ == "__main__":
    import time
    out = FadeAnimation()
    out.FADERATE = 1.0  # seconds
    out.start()

    counter = 0.0

    while True:
        pix = [(0.0, 0.0, 0.0)] * light_count
        for i in range(9):
            for j in range(16):
                r = randomness()
                rgb = hsv_to_rgb(
                    (sin(radians(counter) / 2.0 + float(i) / 6.0) + 1.0) / 6.0, 1.0, 1.0)
                pix[i * 4 + j] = (rgb[0] * 1023.0, rgb[1] * 1023.0 / r, rgb[2] * 1023.0 / r)
        out.write(pix)
        time.sleep(1.0 / speed)
        counter += 0.8
