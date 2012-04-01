import sys, random, scripts, select, simplejson
from socket import *
sys.path.append("./osc")
from oscapi import ColorsOut

HOST = ''    
PORT = 8012    
ADDR = (HOST,PORT)    
BUFSIZE = 4096     


#author: Robert Pieta
if __name__ == "__main__":
    import time
    sleepTime = 0.05
    out = ColorsOut()
    pix = [(0.0,0.0,0.0)] * 24
    currentPixels = [(0.0,0.0,0.0)] * 24
    timeout = 1.0
    out.write(pix)
    
    serv = socket( AF_INET,SOCK_STREAM)    
    serv.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    
    
    serv.bind((ADDR))
    serv.listen(5)   
    print 'listening...'
    
    conn,addr = serv.accept()
    print '...connected!'
    
    pix = scripts.showSuccessfulConnection(pix)
    
    for i in xrange(24):
        currentPixels[i] = pix[i]
    
    out.write(pix)
    
    running = True
    while running:
        conn.setblocking(0)
        ready = select.select([conn], [], [], timeout)
        
        if ready[0]: 
            data = conn.recv(BUFSIZE)
            updatePix = False
            message = data.split("//")[0]
            print message
            
            if message == "makeAllPixels":
                pix = scripts.makeAllPixels(pix, data.split("//")[1])
                updatePix = True
            
            if message == "makePixel":
                pix = scripts.makePixel(pix, data.split("//")[1])
                updatePix = True
            
            if updatePix:
                for i in xrange(24):
                    currentPixels[i] = pix[i]
            
            if message == "turnOffAll":
                currentPixels = scripts.turnOffAll(currentPixels)
            
            if message == "turnOnAll":
                currentPixels = scripts.turnOnAll(pix, currentPixels)
            
            if message == "flashAllLights":
                currentPixels = scripts.flashAll(currentPixels)
            
            if message == "turnOn": 
                messageData = data.split("//")[1]
                currentPixels = scripts.turnOn(pix, currentPixels, int(messageData))
            
            if message == "turnOff": 
                messageData = data.split("//")[1]
                currentPixels = scripts.turnOff(currentPixels, int(messageData))
            
            if message == "closeConnection": 
                pix = scripts.showErrorInConnection(pix)
                
                for i in xrange(24):
                    currentPixels[i] = pix[i]
                
                out.write(pix)
                conn.close()
                
                
                serv.listen(5)   
                print 'listening...'
                
                conn,addr = serv.accept()
                print '...connected!'
                
                pix = scripts.showSuccessfulConnection(pix)
                
                for i in xrange(24):
                    currentPixels[i] = pix[i]
                
                out.write(pix)
            
            #time.sleep(sleepTime)
            
            out.write(currentPixels)
        
        
        else: 
            print "Not ready"
            out.write(currentPixels)

#pixel = [tuple(s.split()) for s in data.split("//")]

#print pix
#for i in xrange(24):
#pix[i] = pixel