import serial

#ser = serial.Serial('/dev/tty.usbserial-A9007Q5M', 115200)
#ser = serial.Serial('/dev/ttyUSB0', 115200)

arduinos=[]


def setup():
    for arduino in arduinos:
        arduino.close()
    ardunos = []
    arduinos.append(serial.Serial('/dev/tty.usbmodem1d114441', 115200))
    arduinos.append(serial.Serial('/dev/tty.usbserial-A9007OSa88', 115200))
    arduinos.append(serial.Serial('/dev/tty.usbserial-A9007Q5M', 115200))

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
        print "OOPS! error!"
        setup()

def write(array):
    write1(array[0:16], arduinos[0])
    write1(array[16:32], arduinos[1])
    write1(array[32:48], arduinos[2])


def clear():
    ser.write('C')


if __name__ == "__main__":
    import sys
    if sys.argv[1] == "clear":
        clear()
