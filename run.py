#!/usr/bin/python
import sys
import os
import subprocess
import signal
import argparse

parser = argparse.ArgumentParser(description="Run a specific chrome animation script.")
parser.add_argument('animation_name',
    metavar='animation', 
    type=str,
    help='Name of the animation, specifically name of the folder in animations/.')
args = parser.parse_args()
animation = args.animation_name

p = subprocess.Popen(['python','animations/%s/main.py'%animation])

print "Running animation %s"%animation

print "Press any key to end"

i = raw_input()

os.kill(p.pid, signal.SIGTERM)
