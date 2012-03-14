import serial

#ser = serial.Serial('/dev/tty.usbserial-A9007Q5M', 115200)
ser = serial.Serial('/dev/ttyUSB0', 115200)



"""
    array is an array of 3 tuples (R, G, B)
"""
def write(array):
    towrite = ""
    for LED, (R,G,B) in enumerate(array):
        R = round(R)
        G = round(G)
        B = round(B)
        towrite += "%d %d %d %dn"%(LED, R, G, B)
    towrite += "W"
    ser.write(towrite)
    #print "writing: "+towrite

def clear():
    ser.write('C')


if __name__ == "__main__":
    import sys
    if sys.argv[1] == "clear":
        clear()
