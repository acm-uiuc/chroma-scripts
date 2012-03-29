#!/usr/bin/env python
import sys
import os
import string
import subprocess
import signal
import argparse
import socket
from time import sleep

# Argument handling
parser = argparse.ArgumentParser(description="Run a specific chroma animation script.")
parser.add_argument('animation',
    metavar='animation',
    help='One of these animations: '+string.join(os.listdir('animations/'),', '),
    choices=os.listdir('animations/'))
args = parser.parse_args()
animation = args.animation

# Open emulator if there's no OSC responsive on that port already
try:
    sys.path.append("./osc")
    from osc import OSCClient,OSCMessage
    s=OSCClient()
    s.connect(('localhost',11661))
    # asychronous, so send a bunch to get a potential exception.
    for x in range(10):
        s.send(OSCMessage("poop"))
except Exception,e:
    if '[Errno 61]' in str(e):
        print "Starting emulator, since it doesn't seem to be running yet."
        os.system('emulator/lights_emulator > /dev/null &')
        emu_up = False
        while not emu_up:
            try:
                # asychronous, so send a bunch to get a potential exception.
                for x in range(10):
                    s.send(OSCMessage("poop"))
                emu_up = True
            except Exception,e:
                if not '[Errno 61]' in str(e):
                    emu_up = True
                else:
                    sleep(0.1)

# Start the animation with osc added to the path.
p = subprocess.Popen(['env','PYTHONPATH=./osc:$PYTHONPATH','python','animations/%s/main.py'%animation])

print "Running animation %s"%animation

print "Press enter to end"

i = raw_input()

os.kill(p.pid, signal.SIGTERM)
