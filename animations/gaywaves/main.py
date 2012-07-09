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

    red = (1024*0.9, 1024*0.1, 1024*0.1)
    orange = (1024*0.9, 1024*0.4, 1024*0.1)
    yellow = (1024*0.8, 1024*0.8, 1024*0.1)
    green = (1024*0.2, 1024*0.6, 1024*0.2)
    blue = (1024*0.2, 1024*0.2, 1024*0.7)
    purple = (1024*0.6, 1024*0.1, 1024*0.6)

    while True:
      pix = [(0.0,0.0,0.0)]*24
      if counter ==0:
        pix[0] = purple
        pix[1] = purple
        pix[2] = purple
        pix[3] = purple

        pix[4] = blue
        pix[5] = blue
        pix[6] = blue
        pix[7] = blue

        pix[8] = green
        pix[9] = green
        pix[10] = green
        pix[11] = green

        pix[12] = yellow
        pix[13] = yellow
        pix[14] = yellow
        pix[15] = yellow

        pix[16] = orange
        pix[17] = orange
        pix[18] = orange
        pix[19] = orange

        pix[20] = red
        pix[21] = red
        pix[22] = red
        pix[23] = red
        counter += 1
      elif counter ==1:
        pix[4] = purple
        pix[5] = purple
        pix[6] = purple
        pix[7] = purple

        pix[8] = blue
        pix[9] = blue
        pix[10] = blue
        pix[11] = blue

        pix[12] = green
        pix[13] = green
        pix[14] = green
        pix[15] = green

        pix[16] = yellow
        pix[17] = yellow
        pix[18] = yellow
        pix[19] = yellow

        pix[20] = orange
        pix[21] = orange
        pix[22] = orange
        pix[23] = orange

        pix[0] = red
        pix[1] = red
        pix[2] = red
        pix[3] = red
        counter += 1
      elif counter ==2:
        pix[8] = purple
        pix[9] = purple
        pix[10] = purple
        pix[11] = purple

        pix[12] = blue
        pix[13] = blue
        pix[14] = blue
        pix[15] = blue

        pix[16] = green
        pix[17] = green
        pix[18] = green
        pix[19] = green

        pix[20] = yellow
        pix[21] = yellow
        pix[22] = yellow
        pix[23] = yellow

        pix[0] = orange
        pix[1] = orange
        pix[2] = orange
        pix[3] = orange

        pix[4] = red
        pix[5] = red
        pix[6] = red
        pix[7] = red
        counter += 1
      elif counter ==3:
        pix[12] = purple
        pix[13] = purple
        pix[14] = purple
        pix[15] = purple

        pix[16] = blue
        pix[17] = blue
        pix[18] = blue
        pix[19] = blue

        pix[20] = green
        pix[21] = green
        pix[22] = green
        pix[23] = green

        pix[0] = yellow
        pix[1] = yellow
        pix[2] = yellow
        pix[3] = yellow

        pix[4] = orange
        pix[5] = orange
        pix[6] = orange
        pix[7] = orange

        pix[8] = red
        pix[9] = red
        pix[10] = red
        pix[11] = red
        counter += 1
      elif counter ==4:
        pix[16] = purple
        pix[17] = purple
        pix[18] = purple
        pix[19] = purple

        pix[20] = blue
        pix[21] = blue
        pix[22] = blue
        pix[23] = blue

        pix[0] = green
        pix[1] = green
        pix[2] = green
        pix[3] = green

        pix[4] = yellow
        pix[5] = yellow
        pix[6] = yellow
        pix[7] = yellow

        pix[8] = orange
        pix[9] = orange
        pix[10] = orange
        pix[11] = orange

        pix[12] = red
        pix[13] = red
        pix[14] = red
        pix[15] = red
        counter += 1
      elif counter ==5:
        pix[20] = purple
        pix[21] = purple
        pix[22] = purple
        pix[23] = purple

        pix[0] = blue
        pix[1] = blue
        pix[2] = blue
        pix[3] = blue

        pix[4] = green
        pix[5] = green
        pix[6] = green
        pix[7] = green

        pix[8] = yellow
        pix[9] = yellow
        pix[10] = yellow
        pix[11] = yellow

        pix[12] = orange
        pix[13] = orange
        pix[14] = orange
        pix[15] = orange

        pix[16] = red
        pix[17] = red
        pix[18] = red
        pix[19] = red
        counter =0
      out.write(pix)
      time.sleep(1.0/speed)
