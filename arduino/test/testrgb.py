import colorsys
import api 
import time

lights = [(0,0,0)]*16
hue = 0

while True:
    col = colorsys.hsv_to_rgb(hue, 1, 1)
    lights = [(col[0]*1023, col[1]* 1023, col[2]*1023)]*16
    api.write(lights)
    hue += 0.01
    time.sleep(0.03)
    print 'turning on light %d'%hue


