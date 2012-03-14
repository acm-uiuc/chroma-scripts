#!/usr/bin/python
import sys
import os
import subprocess
import signal

animation = sys.argv[1]

p = subprocess.Popen(['python','animations/%s/main.py'%animation])

print "Running animation %s"%animation

print "Press any key to end"

i = raw_input()

os.kill(p.pid, signal.SIGTERM)
