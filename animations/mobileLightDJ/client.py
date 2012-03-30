from socket import *    
import pickle
import time, random

HOST = 'localhost'
PORT = 29876   
ADDR = (HOST,PORT)
BUFSIZE = 4096

cli = socket( AF_INET,SOCK_STREAM)
cli.connect((ADDR))

while True:
    data = cli.recv(BUFSIZE)
    if not data: break
    pix = pickle.loads(data)
    pix[0] = (0.0, 0.0 + random.randint(0,1023), 0.0)
    
    cli.send(pickle.dumps(pix))
    time.sleep(.5)

cli.close()