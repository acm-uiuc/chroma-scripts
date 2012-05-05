import sys
from animations import FadeAnimation
from math import sin, radians, degrees
from colorsys import hsv_to_rgb

speed = 40.0

if __name__ == "__main__":
    import time
    out = FadeAnimation()
    out.FADERATE = 1.0 # seconds
    out.start()

    counter = 0

    green = [(0.2, 0.5, 0.2)]
    blue = [(0.0,0.0,0.8)]
    red = [(0.7, 0.2, 0.2)]
    yellow = [(0.9, 0.9, 0.1)]

    while True:
      pix = [(0.0,0.0,0.0)]*24
      if counter ==0:
        pix[0:4] = green
        counter++
      elif counter ==1:
        pix[4:8] = green
        counter++
      elif counter ==2:
        pix[8:12] = green
        counter++
      elif counter ==3:
        pix[12:16] = green
        counter++
      elif counter ==4:
        pix[16:20] = green
        counter++
      elif counter ==5:
        pix[20:24] = green
        counter =0
      out.write(pix)
      time.sleep(1.0/speed)
