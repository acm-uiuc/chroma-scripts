import simplejson


def turnOn(pix, currentPixels, index):
    currentPixels[index] = pix[index]
    return currentPixels

def turnOff(currentPixels, index):
    currentPixels[index] = (0.0, 0.0, 0.0)
    return currentPixels

def turnOffAll(currentPixels):
    for i in xrange(24):
        currentPixels[i] = (0.0, 0.0, 0.0)
    return currentPixels

def turnOnAll(pix, currentPixels):
    for i in xrange(24):
        currentPixels[i] = pix[i]
    return currentPixels

def flashAll(currentPixels):
    for i in xrange(24):
        currentPixels[i] = (1023.0, 1023.0, 1023.0)

    return currentPixels

def makeAllPixels(pix, data):
    try:
        pix = simplejson.loads(data)
    except:
        pass
    
    return pix

def makePixel(pix, data):
    print data
    try:
        index = simplejson.loads(data.split("/")[0])
        pix[index] = simplejson.loads(data.split("/")[1])
    except:
        pass

    return pix


def showSuccessfulConnection(pix): 
    for i in xrange(24):
        pix[i] = (0.0, 0.0, 1023.0)

    pix[5] = (0.0, 1023.0, 0.0)
    pix[6] = (0.0, 1023.0, 0.0)
    pix[9] = (0.0, 1023.0, 0.0)
    pix[10] = (0.0, 1023.0, 0.0)

    return pix


def showErrorInConnection(pix):
    for i in xrange(24):
        pix[i] = (0.0, 0.0, 1023.0)
        
    pix[5] = (1023.0, 0.0, 0.0)
    pix[6] = (1023.0, 0.0, 0.0)
    pix[9] = (1023.0, 0.0, 0.0)
    pix[10] = (1023.0, 0.0, 0.0)

    return pix