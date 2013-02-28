import sys
from animations import FadeAnimation
from simpleOSC import initOSCServer, startOSCServer, closeOSC, setOSCHandler
import OSC

ip = "127.0.0.1"
port = 9125
NUMBER_OF_LIGHTS = 48
DEFAULT_COLOR = [25, 25, 25]
canvas = DEFAULT_COLOR * NUMBER_OF_LIGHT

def setup():
	import time
	initOSCServer(ip, port)
	
	# OSC HANDLERS #
	setOSCHandler('/collision', collision)

	# SERVER START #
	startOSCServer()
	print "server is running, listening at " + str(ip) + ":" + str(port)

	try:
		while(1):
			time.sleep(1000)
	except KeyboardInterrupt:
		print "closing all OSC connections... and exit"
		closeOSC() # finally close the connection before exiting or program.

def collision(addr, tags, data, source):
	print "HEY I GOT A THING!!!"
	print "addr = " + str(addr) # /collision
	print "tags = " + str(tags) # is
	print "data = " + str(data) # [444, 'stuff']
	print "sour = " + str(source) # (network info)
	
if __name__ == "__main__":
	setup()

	# import time
    # out = FadeAnimation()
    # out.FADERATE = 8.0
    # out.start()

    # while True:
        # for i in range(24):
            # pix = [(0.0,0.0,0.0)]*24
            # if i%8 == 0:
                # pix[i] = (1023.0,0.0,0.0)
            # else:
                # pix[i] = (0.0,1023.0,1023.0)
            # out.write(pix)
            # time.sleep(0.7)
            # time.sleep(0.2)
