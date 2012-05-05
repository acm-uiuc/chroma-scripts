#!/usr/bin/python
from osc import OSCServer, OSCClient, OSCMessage
import sys
import time
import itertools
# funny python's way to add a method to an instance of a class
import types
# for some awesome hacking to get the name of the script
import os

def handle_timeout(self):
    self.timed_out = True

CLEAR_TIME = 5 #5 seconds before it clears stuff
STAGING = False #don't do the actual writing. also print shit out.
DEBUG = False 

def clampv(low,x,high):
    return max(low, min(x, high))

def clamp(x):
    return max(0.0, min(x, 1023.0))

def clampColor(color):
    return (clamp(color[0]), clamp(color[1]), clamp(color[2]))

def sum(c1, c2):
    #print "mult %s,%s"%(str(c1),str(c2))
    return (c1[0]+c2[0], c1[1]+c2[1], c1[2]+c2[2])

def mult(c1, val):
    #print "mult %s, val: %s"%(str(c1),str(val))
    return (c1[0]*val, c1[1]*val, c1[2]*val)

class ColorsIn:
    #measured in seconds to fade in 100%
    fadeoutrate = 4.0
    fadeinrate = 4.0
    bootthreshold = 0.01
    maxlayers = 3

    def set_colors(self,path, tags, args, source):
        try:
            chroma = ChromaMessage.fromOSC(tags,args)

            #if we have no records of any streams:
            #if we have a record of a current stream, and no record of this stream:
            if not self.activepid or chroma.pid not in self.layers:
                self.activepid = chroma.pid
                #mark all other layers as fading out
                for pid in self.layers:
                    self.layers[pid].state = Layer.FADEOUT
                self.layers[chroma.pid] = Layer(chroma, 0, Layer.FADEIN)
                self.lastwriteany = time.time() - 1/30.0 #force this frame to fade in at the target framerate: 30fps

            self.layers[chroma.pid].chroma = chroma

            #in any case, we slowly fade out every stream remaining
            #this also writes to the device
            self.updateStream()
            #mark the last time we got a packet
            self.lastwrite=time.time()
        except:
            import traceback
            traceback.print_exc()

    """
        applies fadeout rules to any stream not the main one
        and writes to the device
    """
    def updateStream(self):
        for layer in self.layers.values():
            self.applyFadingRules(layer)
        if len(self.layers) > ColorsIn.maxlayers:
            self.layers = dict( (k, v) for k,v in self.layers.iteritems() if self.shouldWeKeepLayer(v) )
        #apply our opacity rules
        pixels = self.applyOpacity(self.layers.values())
        if not STAGING:
            self.streamer.pixels = pixels
	    self.streamer.metadata = self.layers[self.activepid].chroma
            #pixels = self.crazyMofoingReorderingOfLights(pixels)
            octoapi.write(pixels)
        if DEBUG:
            for layer in self.layers.values():
                print "PID: %d, OPACITY: %f"%(layer.chroma.pid, layer.opacity)
        self.lastwriteany=time.time()

    def shouldWeKeepLayer(self,layer):
        if layer.state == Layer.FADEOUT and layer.opacity < self.bootthreshold:
            return False
        return True

    def applyFadingRules(self,layer):
        diff = time.time() - self.lastwriteany
        print diff
        fadein = (1.0/ColorsIn.fadeinrate) * diff
        fadeout = (1.0/ColorsIn.fadeoutrate) * diff
        if layer.state == Layer.FADEIN:
            layer.opacity += fadein 
        if layer.state == Layer.FADEOUT:
            layer.opacity -= fadeout 
        layer.opacity = clampv(0,layer.opacity,1)
        return layer

    """
        compresses down the entire list and gives us the final result
    """
    def applyOpacity(self,layers):
        data = [(0.0,0.0,0.0)] * len(layers[0].chroma.data)
        for layer in layers:
            data = [sum(currentvalue,mult(value,layer.opacity)) for currentvalue,value in itertools.izip(data,layer.chroma.data)]
        data = [clampColor(value) for value in data]
        return data

    def handleClearing(self):
        if time.time() - self.lastwrite > CLEAR_TIME and time.time() - self.lastclear > 1/30.0:
            #print "CLEARING! %f"%time.time()
            self.activepid = 0
            for layer in self.layers.values(): layer.state = Layer.FADEOUT
            shouldweupdate = False
            #don't bother updating if we're below the threshold. not often anyway.
            for layer in self.layers.values():
                if layer.opacity > self.bootthreshold:
                    shouldweupdate = True
            if shouldweupdate: 
                self.updateStream()
            else:
                if not STAGING: 
                    octoapi.write([(0,0,0)]*24)
                if DEBUG:
                    print "CLEARED! %f"%time.time()
            self.lastclear = time.time()

    def each_frame(self):
        self.server.timed_out = False
        while not self.server.timed_out:
            self.handleClearing()
            self.server.handle_request()


    def crazyMofoingReorderingOfLights(self, pixels):
        pixels2 = pixels[:] #make a copy so we don't kerplode someone's work
        """
        what are we expecting? we want the back left (by the couches) of the room to be pixel 0, 
        and by the front is the last row
        whereas in reality, it's the opposite.
        here is the order it'd be nice to have them in:
        
        0  1  2  3
        4  5  6  7
        8  9  10 11
        12 13 14 15
        16 17 18 19
        20 21 22 23

        this is the actual order:   
        23 22 21 20
        19 16 17 18
        15 14 13 12
        11 10 9  8
        3  2  5  4
        6 *0**1**7*   *=not there
        """

        actualorder = [23,22,21,20,19,16,17,18,15,14,13,12,11,10,9,8,3,2,5,4,6,0,1,7]
        badcolors = [] #3,2,5,4,6,0,1,7]
        for i in range(len(actualorder)):
            (r,g,b) = pixels[i]
            r = max(0.0, min(r, 1023.0))
            g = max(0.0, min(g, 1023.0))
            b = max(0.0, min(b, 1023.0))
            pixels2[actualorder[i]] = (r,g,b)
        for i in range(len(badcolors)):
            pixels2[badcolors[i]] = (0.0,0.0,0.0)
        return pixels2


    def start(self):
        #server = OSCServer( ("128.174.251.39", 11661) )
        self.server = OSCServer( ("localhost", 11661) )
        self.server.timeout = 0
        self.lastwrite = time.time()        
        self.server.handle_timeout = types.MethodType(handle_timeout, self.server)
        self.server.lastpixels = [(0,0,0)]*24

        self.layers = {}
        self.activepid = 0
        self.lastclear = time.time()
        self.lastwriteany = 0

        self.streamer = StreamPoster()
        self.streamer.start()

        self.server.addMsgHandler( "/setcolors", self.set_colors)
        while True:
            self.each_frame()

        self.server.close()


class Layer:
    FADEIN = 1
    FADEOUT = -1

    def __init__(self, chroma, opacity, state):
        self.chroma = chroma
        self.opacity = opacity
        self.state = state


"""
The Chroma OSC Message structure:
    HEADER
        header length (1 int, in number of messages, not bytes)
        pid (int)
        name of animation (string)
        class of stream (string)
        framenumber (int)
        timestamp
        ---reserved for future use---
    DATA
        72 Floats
"""
class ChromaMessage:
    def __init__(self, data, title, streamclass, framenumber, creator, description, timestamp=0, pid=0):
        self.data = data
        self.title = title
        self.streamclass = streamclass
        self.framenumber = framenumber
        self.timestamp = timestamp
        self.pid = pid
	self.creator = creator
	self.description = description

    def toOSC(self, messagename):
        message = OSCMessage(messagename)
        message.append(8)
        message.append(os.getpid())
        message.append(self.title)
        message.append(self.streamclass)
        message.append(self.framenumber)
        message.append(time.time())
	message.append(self.creator)
	message.append(self.description)
        message.append(self.data)
        return message

    @staticmethod
    def fromOSC(tags, args):
        headerlength = args[0]
        pid = args[1]
        name = args[2]
        streamclass = args[3]
        framenumber = args[4]
        timestamp = args[5]
	creator = args[6]
	description = args[7]
        pixels = []
        for i in range(0,(len(args)-headerlength)/3):
            pixel = (clamp(args[i*3+headerlength]), clamp(args[i*3+1+headerlength]), clamp(args[i*3+2+headerlength]))
            pixels.append( pixel )
        return ChromaMessage(pixels,name,streamclass,framenumber,creator,description, timestamp, pid)
    



import threading
import urllib2
import simplejson
import time
streamurl = "http://lab2.acm.uiuc.edu:8009/sendstream"
class StreamPoster( threading.Thread):
    
    def run(self):
        self.pixels = []
        self.keepRunning = True
	self.metadata = None
	while self.keepRunning:
	   if self.metadata:
	       jsondata = simplejson.dumps({"colors":self.pixels, "title":self.metadata.title, "creator": self.metadata.creator})
	       #print "Sending to server: %s data: %s"%(streamurl, jsondata)
	       try:
		urllib2.urlopen(streamurl, "data="+jsondata)
	       except:
		pass
           time.sleep(1.0/12.0)
 


import os
import sys

class ColorsOut:
    def __init__(self, streamclass="something"):
        self.client = OSCClient()
        self.client.connect( ("localhost",11661) )
	self.title = "Something went wrong"
	try:
	  print "argv[0] "+sys.argv[0]
	  print "getcwd "+os.getcwd()
	  path = os.getcwd()+"/"+sys.argv[0]
	  path = path.replace("main.py","")
	  manifest = open(path+"manifest.json")
	  data = simplejson.load(manifest)
	  self.title = data["name"]
	  self.creator = data["creator"]
	  self.description = data["description"]
	  manifest.close()
	except:
	  print "Hey we died"

        self.framenumber = 0
        self.streamclass = streamclass

    def write(self, pixels):
        #pixels = self.crazyMofoingReorderingOfLights(pixels)
        chroma = ChromaMessage(pixels, self.title, self.streamclass, self.framenumber, self.creator, self.description)
        message = chroma.toOSC("/setcolors")
        self.client.send( message )
        self.framenumber += 1





















if __name__ == "__main__":
    import signal
    import sys
    if not STAGING:
        import octoapi
    colors = ColorsIn()
    def signal_handler(signal, frame):
        colors.streamer.keepRunning=False
        sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)
    colors.start()
