import sys
from animations import FadeAnimation
from math import sin, radians, degrees
from colorsys import hsv_to_rgb

speed = 2.0

if __name__ == "__main__":
    import time
    out = FadeAnimation()
    out.FADERATE = 1.0 # seconds
    out.start()

    counter = 0

    green = (1024*0.2, 1024*0.6, 1024*0.2)
    blue = (1024*0.2, 1024*0.2, 1024*0.7)

    while True:
      pix = [(0.0,0.0,0.0)]*24
      if counter ==0:
        pix[20] = blue
        pix[21] = blue
        pix[22] = blue
        pix[23] = blue
        pix[0] = green
        pix[1] = green
        pix[2] = green
        pix[3] = green
        counter += 1
      elif counter ==1:
        pix[0] = blue
        pix[1] = blue
        pix[2] = blue
        pix[3] = blue
        pix[4] = green
        pix[5] = green
        pix[6] = green
        pix[7] = green
        counter += 1
      elif counter ==2:
        pix[4] = blue
        pix[5] = blue
        pix[6] = blue
        pix[7] = blue
        pix[8] = green
        pix[9] = green
        pix[10] = green
        pix[11] = green
        counter += 1
      elif counter ==3:
        pix[8] = blue
        pix[9] = blue
        pix[10] = blue
        pix[11] = blue
        pix[12] = green
        pix[13] = green
        pix[14] = green
        pix[15] = green
        counter += 1
      elif counter ==4:
        pix[12] = blue
        pix[13] = blue
        pix[14] = blue
        pix[15] = blue
        pix[16] = green
        pix[17] = green
        pix[18] = green
        pix[19] = green
        counter += 1
      elif counter ==5:
        pix[16] = blue
        pix[17] = blue
        pix[18] = blue
        pix[19] = blue
        pix[20] = green
        pix[21] = green
        pix[22] = green
        pix[23] = green
        counter =0
      out.write(pix)
      time.sleep(1.0/speed)
