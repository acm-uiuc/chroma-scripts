import json


def turnOn(pix, currentPixels, index):
    currentPixels[index] = pix[index]
    return currentPixels

def turnOff(currentPixels, index):
    currentPixels[index] = (0.0, 0.0, 0.0)
    return currentPixels


def makeAllPixels(pix, data):
    pix = json.loads(data)
    return pix