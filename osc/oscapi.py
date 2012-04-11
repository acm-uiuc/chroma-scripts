#!/usr/bin/python
from osc import OSCServer, OSCClient, OSCMessage
import sys
import time
# funny python's way to add a method to an instance of a class
import types
# for some awesome hacking to get the name of the script
import os

def handle_timeout(self):
    self.timed_out = True

CLEAR_TIME = 5 #5 seconds before it clears stuff

def clamp(x):
    return max(0.0, min(x, 1023.0))

class ColorsIn:
# this method of reporting timeouts only works by convention
# that before calling handle_request() field .timed_out is 
# set to False


    def set_colors(self,path, tags, args, source):
        chroma = ChromaMessage.fromOSC(tags,args)
        pixels = chroma.data
        #print "Pixels: %s"%str(pixels)
        #print "Time: "+str((time.time()*1000) % 10000)
        octoapi.write(pixels)
        self.lastwrite=time.time()
        self.server.lastpixels = pixels

    def diff_colors(self, path, tags, args, source):
        # which user will be determined by path:
        # we just throw away all slashes and join together what's left
        #print "Here's what we got : path:%s tags:%s args:%s source:%s"%(str(path),str(tags),str(args),str(source))
        pixels = server.lastpixels
        for i in range(0,len(args)/3):
            pp = (args[i*3],args[i*3+1],args[i*3+2])
            p = pixels[i]
            pixels[i] = (clamp(p[0]+pp[0]), clamp(p[1]+pp[1]), clamp(p[2]+pp[2]))
        #print "Pixels: %s"%str(pixels)
        #print "Time: "+str((time.time()*1000) % 10000)
        octoapi.write(pixels)
        self.lastwrite=time.time()
        self.server.lastpixels = pixels

    def each_frame(self):
        self.server.timed_out = False
        while not self.server.timed_out:
            if time.time() - self.lastwrite > CLEAR_TIME:
                self.lastwrite = time.time()
                octoapi.write([(0,0,0)]*24)
                print "Clearing"
            self.server.handle_request()

    def start(self):
        #server = OSCServer( ("128.174.251.39", 11661) )
        self.server = OSCServer( ("localhost", 11661) )
        self.server.timeout = 0
        self.lastwrite = time.time()        
        self.server.handle_timeout = types.MethodType(handle_timeout, self.server)
        self.server.lastpixels = [(0,0,0)]*24

        self.server.addMsgHandler( "/setcolors", self.set_colors)
        self.server.addMsgHandler( "/diffcolors", self.diff_colors)
        while True:
            self.each_frame()

        self.server.close()


if __name__ == "__main__":
    import octoapi
    ColorsIn().start()


"""
The Chroma OSC Message structure:
    HEADER
        header length (1 int, in number of messages, not bytes)
        pid (int)
        name of animation (string)
        class of stream (string)
        framenumber (int)
        ---reserved for future use---
    DATA
        72 Floats
"""
class ChromaMessage:
    def __init__(self, data, title, streamclass, framenumber):
        self.data = data
        self.title = title
        self.streamclass = streamclass
        self.framenumber = framenumber

    def toOSC(self, messagename):
        message = OSCMessage(messagename)
        message.append(5)
        message.append(os.getpid())
        message.append(self.title)
        message.append(self.streamclass)
        message.append(self.framenumber)
        message.append(self.data)
        return message

    @staticmethod
    def fromOSC(tags, args):
        headerlength = args[0]
        pid = args[1]
        name = args[2]
        streamclass = args[3]
        framenumber = args[4]
        pixels = []
        for i in range(0,len(args)/3):
            pixel = (clamp(args[i*3+headerlength]), clamp(args[i*3+1+headerlength]), clamp(args[i*3+2+headerlength]))
            pixels.append( pixel )
        return ChromaMessage(data,name,streamclass,framenumber)
        




class ColorsOut:

    def __init__(self, title="demo", streamclass="something"):
        self.client = OSCClient()
        self.client.connect( ("localhost",11661) )
        self.title = title 
        self.framenumber = 0
        self.streamclass = streamclass

    def write(self, pixels):
        pixels = self.crazyMofoingReorderingOfLights(pixels)
        chroma = ChromaMessage(pixels, self.title, self.streamclass, self.framenumber)
        message = chroma.toOSC("/setcolors")
        self.client.send( message )
        self.framenumber += 1



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
