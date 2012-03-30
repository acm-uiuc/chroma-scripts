def makeAllRed(pix):
    for i in xrange(24):
        pix[i] = (1023.0, 0.0, 0.0)
    
    return pix

def makeAllBlue(pix):
    for i in xrange(24):
        pix[i] = (0.0, 0.0, 1023.0)
    
    return pix

def makeAllGreen(pix):
    for i in xrange(24):
        pix[i] = (0.0, 1023.0, 0.0)
    
    return pix


def turnOn(pix, currentPixels, index):
    currentPixels[index] = pix[index]
    return currentPixels

def turnOff(currentPixels, index):
    currentPixels[index] = (0.0, 0.0, 0.0)
    return currentPixels