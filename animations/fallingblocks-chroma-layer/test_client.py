from simpleOSC import initOSCClient, sendOSCMsg

ip = "127.0.0.1"
port = 9125

NUMBER_OF_LIGHTS = 24 # currently 24, EOH 48
DEFAULT_COLOR = [(25.0, 25.0, 25.0)] # dim white light
canvas = DEFAULT_COLOR * NUMBER_OF_LIGHTS

def test():
	initOSCClient(ip, port)
	#sendOSCMsg("/collision", [444, "stuff"]))
	canvas[0] = (1.0,2.0,3.0)
	print canvas

test()
