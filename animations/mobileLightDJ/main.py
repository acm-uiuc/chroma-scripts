import sys, random, pickle
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
    out = ColorsOut()
    pix = [(0.0,0.0,0.0)] * 24
    
    serv = socket( AF_INET,SOCK_STREAM)    

    serv.bind((ADDR))    
    serv.listen(5)  

    serv = socket( AF_INET,SOCK_STREAM)    
    
    serv.bind((ADDR))
    serv.listen(5)   
    print 'listening...'

    conn,addr = serv.accept()
    print '...connected!'
    
    while True:
        conn.send(pickle.dumps(pix))
        time.sleep(1.0)

        data = conn.recv(BUFSIZE)
        if not data: break
        # pixels = pickle.loads(data)
        pixelBefore = data.split("//")
        pixelAfter = [x.split() for x in pixelBefore]
        for i in xrange(24):
            pix[i] = (float(pixelAfter[i][0]),float(pixelAfter[i][1]), float(pixelAfter[i][2]))
        
        #pixel = [tuple(s.split()) for s in data.split("//")]
        
#print pix
        #for i in xrange(24):
        #pix[i] = pixel
        out.write(pix)
    
    conn.close()