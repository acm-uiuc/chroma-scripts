#!/usr/bin/python
from osc import OSCServer, OSCClient, OSCMessage
import sys








if __name__ == "__main__":
    if len(sys.argv) < 2:
        print """
sendcommand.py: sends commands to the running oscapi.py daemon.
usage: ./sendcommand.py command
available commands:
    reloadconfig - reloads config.py in the octoapi - usually reordering the lights
"""
        sys.exit(-1)
    messagename = sys.argv[1] 
    client = OSCClient()
    client.connect( ("localhost",11661) )
    message = OSCMessage('/'+messagename)
    for param in sys.argv[2:]:
        message.append(param)
    client.send( message )
