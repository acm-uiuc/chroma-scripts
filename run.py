#!/usr/bin/env python
import sys
import os
import string
import subprocess
import signal
import argparse

parser = argparse.ArgumentParser(description="Run a specific chroma animation script.")
parser.add_argument('animation',
    metavar='animation',
    help='One of these animations: '+string.join(os.listdir('animations/'),', '),
    choices=os.listdir('animations/'))

args = parser.parse_args()

animation = args.animation

p = subprocess.Popen(['python','animations/%s/main.py'%animation])

print "Running animation %s"%animation

print "Press enter to end"

i = raw_input()

os.kill(p.pid, signal.SIGTERM)
