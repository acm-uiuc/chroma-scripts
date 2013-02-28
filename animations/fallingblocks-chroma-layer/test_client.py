from simpleOSC import initOSCClient, sendOSCMsg

ip = "127.0.0.1"
port = 9125

def test():
	initOSCClient(ip, port)

	sendOSCMsg("/collision", [444, "stuff"])

test()
