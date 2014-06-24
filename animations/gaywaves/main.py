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
      pix = [(0.0,0.0,0.0)]*48
      if counter ==0:
        pix[0] = purple
        pix[6] = purple
        pix[12] = purple
        pix[18] = purple
        pix[24] = purple
        pix[30] = purple
        pix[36] = purple
        pix[42] = purple

        pix[1] = blue
        pix[7] = blue
        pix[13] = blue
        pix[19] = blue
        pix[25] = blue
        pix[31] = blue
        pix[37] = blue
        pix[43] = blue

        pix[2] = green
        pix[8] = green
        pix[14] = green
        pix[20] = green
        pix[26] = green
        pix[32] = green
        pix[38] = green
        pix[44] = green

        pix[3] = yellow
        pix[9] = yellow
        pix[15] = yellow
        pix[21] = yellow
        pix[27] = yellow
        pix[33] = yellow
        pix[39] = yellow
        pix[45] = yellow

        pix[4] = orange
        pix[10] = orange
        pix[16] = orange
        pix[22] = orange
        pix[28] = orange
        pix[34] = orange
        pix[40] = orange
        pix[46] = orange

        pix[5] = red
        pix[11] = red
        pix[17] = red
        pix[23] = red
        pix[29] = red
        pix[35] = red
        pix[41] = red
        pix[47] = red
        counter += 1
      elif counter ==1:
        pix[1] = purple
        pix[7] = purple
        pix[13] = purple
        pix[19] = purple
        pix[25] = purple
        pix[31] = purple
        pix[37] = purple
        pix[43] = purple

        pix[2] = blue
        pix[8] = blue
        pix[14] = blue
        pix[20] = blue
        pix[26] = blue
        pix[32] = blue
        pix[38] = blue
        pix[44] = blue

        pix[3] = green
        pix[9] = green
        pix[15] = green
        pix[21] = green
        pix[27] = green
        pix[33] = green
        pix[39] = green
        pix[45] = green

        pix[4] = yellow
        pix[10] = yellow
        pix[16] = yellow
        pix[22] = yellow
        pix[28] = yellow
        pix[34] = yellow
        pix[40] = yellow
        pix[46] = yellow

        pix[5] = orange
        pix[11] = orange
        pix[17] = orange
        pix[23] = orange
        pix[29] = orange
        pix[35] = orange
        pix[41] = orange
        pix[47] = orange

        pix[0] = red
        pix[6] = red
        pix[12] = red
        pix[18] = red
        pix[24] = red
        pix[30] = red
        pix[36] = red
        pix[42] = red
        counter += 1
      elif counter ==2:
        pix[2] = purple
        pix[8] = purple
        pix[14] = purple
        pix[20] = purple
        pix[26] = purple
        pix[32] = purple
        pix[38] = purple
        pix[44] = purple

        pix[3] = blue
        pix[9] = blue
        pix[15] = blue
        pix[21] = blue
        pix[27] = blue
        pix[33] = blue
        pix[39] = blue
        pix[45] = blue

        pix[4] = green
        pix[10] = green
        pix[16] = green
        pix[22] = green
        pix[28] = green
        pix[34] = green
        pix[40] = green
        pix[46] = green

        pix[5] = yellow
        pix[11] = yellow
        pix[17] = yellow
        pix[23] = yellow
        pix[29] = yellow
        pix[35] = yellow
        pix[41] = yellow
        pix[47] = yellow

        pix[0] = orange
        pix[6] = orange
        pix[12] = orange
        pix[18] = orange
        pix[24] = orange
        pix[30] = orange
        pix[36] = orange
        pix[42] = orange

        pix[1] = red
        pix[7] = red
        pix[13] = red
        pix[19] = red
        pix[25] = red
        pix[31] = red
        pix[37] = red
        pix[43] = red
        counter += 1
      elif counter ==3:
        pix[3] = purple
        pix[9] = purple
        pix[15] = purple
        pix[21] = purple
        pix[27] = purple
        pix[33] = purple
        pix[39] = purple
        pix[45] = purple

        pix[4] = blue
        pix[10] = blue
        pix[16] = blue
        pix[22] = blue
        pix[28] = blue
        pix[34] = blue
        pix[40] = blue
        pix[46] = blue

        pix[5] = green
        pix[11] = green
        pix[17] = green
        pix[23] = green
        pix[29] = green
        pix[35] = green
        pix[41] = green
        pix[47] = green

        pix[0] = yellow
        pix[6] = yellow
        pix[12] = yellow
        pix[18] = yellow
        pix[24] = yellow
        pix[30] = yellow
        pix[36] = yellow
        pix[42] = yellow

        pix[1] = orange
        pix[7] = orange
        pix[13] = orange
        pix[19] = orange
        pix[25] = orange
        pix[31] = orange
        pix[37] = orange
        pix[43] = orange

        pix[2] = red
        pix[8] = red
        pix[14] = red
        pix[20] = red
        pix[26] = red
        pix[32] = red
        pix[38] = red
        pix[44] = red
        counter += 1
      elif counter ==4:
        pix[4] = purple
        pix[10] = purple
        pix[16] = purple
        pix[22] = purple
        pix[28] = purple
        pix[34] = purple
        pix[40] = purple
        pix[46] = purple

        pix[5] = blue
        pix[11] = blue
        pix[17] = blue
        pix[23] = blue
        pix[29] = blue
        pix[35] = blue
        pix[41] = blue
        pix[47] = blue

        pix[0] = green
        pix[6] = green
        pix[12] = green
        pix[18] = green
        pix[24] = green
        pix[30] = green
        pix[36] = green
        pix[42] = green

        pix[1] = yellow
        pix[7] = yellow
        pix[13] = yellow
        pix[19] = yellow
        pix[25] = yellow
        pix[31] = yellow
        pix[37] = yellow
        pix[43] = yellow

        pix[2] = orange
        pix[8] = orange
        pix[14] = orange
        pix[20] = orange
        pix[26] = orange
        pix[32] = orange
        pix[38] = orange
        pix[44] = orange

        pix[3] = red
        pix[9] = red
        pix[15] = red
        pix[21] = red
        pix[27] = red
        pix[33] = red
        pix[39] = red
        pix[45] = red
        counter += 1
      elif counter ==5:
        pix[5] = purple
        pix[11] = purple
        pix[17] = purple
        pix[23] = purple
        pix[29] = purple
        pix[35] = purple
        pix[41] = purple
        pix[47] = purple

        pix[0] = blue
        pix[6] = blue
        pix[12] = blue
        pix[18] = blue
        pix[24] = blue
        pix[30] = blue
        pix[36] = blue
        pix[42] = blue

        pix[1] = green
        pix[7] = green
        pix[13] = green
        pix[19] = green
        pix[25] = green
        pix[31] = green
        pix[37] = green
        pix[43] = green

        pix[2] = yellow
        pix[8] = yellow
        pix[14] = yellow
        pix[20] = yellow
        pix[26] = yellow
        pix[32] = yellow
        pix[38] = yellow
        pix[44] = yellow

        pix[3] = orange
        pix[9] = orange
        pix[15] = orange
        pix[21] = orange
        pix[27] = orange
        pix[33] = orange
        pix[39] = orange
        pix[45] = orange

        pix[4] = red
        pix[10] = red
        pix[16] = red
        pix[22] = red
        pix[28] = red
        pix[34] = red
        pix[40] = red
        pix[46] = red
        counter =0
      out.write(pix)
      time.sleep(1.0/speed)
