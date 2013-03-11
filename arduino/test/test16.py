
import api 
import time

lights = [(0,0,0)]*16
pos = 0

while True:
    lights = [(1023,1023,1023)]*16
    lights[pos] = (0,0,1023)
    pos += 1
    pos = pos % len(lights)
    api.write(lights)
    time.sleep(0.500)
    print 'turning on light %d'%pos


