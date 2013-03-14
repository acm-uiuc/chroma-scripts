from __future__ import with_statement #dgrrrr
import serial
import config

#ser = serial.Serial('/dev/tty.usbserial-A9007Q5M', 115200)
#ser = serial.Serial('/dev/ttyUSB0', 115200)

arduinos=[]
FILENAME = "devices.txt"
LIGHTS_PER_ARDUINO = 16
NUM_LIGHTS = 16*3

def setup():
    for arduino in arduinos:
        arduino.close()
    ardunos = []
    with open(FILENAME) as f:
        for line in f.readlines():
            line = line.strip()
            try:
                arduinos.append(serial.Serial(line, 115200))
            except Exception as e:
                print "ERROR OPENING ARDUINO "+line
                print e
    NUM_LIGHTS = LIGHTS_PER_ARDUINO * len(arduinos) 

setup()




"""
    array is an array of 3 tuples (R, G, B)
"""
def write1(array, ser):
    try:
        towrite = ""
        for LED, (R,G,B) in enumerate(array):
            R = round(R)
            G = round(G)
            B = round(B)
            towrite += "%d %d %d %dn"%(LED, R, G, B)
        towrite += "W"
        ser.write(towrite)
        #print "writing: "+towrite
    except:
        print "OOPS! error! retrying"
        setup()

def write(array):
    #bounds checking
    array = config.maplights(array)
    if len(array) < NUM_LIGHTS:
        diff = NUM_LIGHTS - len(array)
        array = array + [(0,0,0)]*diff
    if len(array) > NUM_LIGHTS:
        array = array[0:NUM_LIGHTS]
    for arduino,chunk in enumerate(chunks(array, LIGHTS_PER_ARDUINO)):
        write1(chunk, arduinos[arduino])

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


def clear():
    for arduino in arduinos:
        arduino.write('C')


if __name__ == "__main__":
    import sys
    if sys.argv[1] == "clear":
        clear()
