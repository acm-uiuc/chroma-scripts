import pyaudio
import numpy
import audioop
import sys
import math
import struct
from oscapi import ColorsOut
from animations import FadeAnimation

'''
Sources

http://www.swharden.com/blog/2010-03-05-realtime-fft-graph-of-audio-wav-file-or-microphone-input-with-python-scipy-and-wckgraph/
http://macdevcenter.com/pub/a/python/2001/01/31/numerically.html?page=2

'''

chunk      = 2**11 # Change if too fast/slow, never less than 2**11
scale      = 21    # Change if too dim/bright
exponent   = 9     # Change if too little/too much difference between loud and quiet sounds
samplerate = 44100 
cutoff = 0

MAX = 48
out = FadeAnimation()
out.FADEINRATE = 2.0 #optional
out.FADEOUTRATE = 8.0 #optional, makes things 'trail off'
out.start()

def list_devices():
    # List all audio input devices
    p = pyaudio.PyAudio()
    i = 0
    n = p.get_device_count()
    while i < n:
        dev = p.get_device_info_by_index(i)
        if dev['maxInputChannels'] > 0:
            print str(i)+'. '+dev['name']
        i += 1

def music_visuals(): 
    # CHANGE THIS TO CORRECT INPUT DEVICE
    # Enable stereo mixing in your sound card
    # to make you sound output an input
    # Use list_devices() to list all your input devices
    device   = 4  
    
    p = pyaudio.PyAudio()
    stream = p.open(format = pyaudio.paInt16,
                    channels = 1,
                    rate = 44100,
                    input = True,
                    frames_per_buffer = chunk,
                    input_device_index = device)

    hue = 0.0
    
    try:
        while True:
            try:
                data = stream.read(chunk)
            except IOError, e:
                if e.args[1] == pyaudio.paInputOverflowed:
                    data = '\x00'*chunk
                else:
                    raise

            # Do FFT
            levels = calculate_levels(data, chunk, samplerate)

            for i in range(0,len(levels)):
                levels[i] = max(min(levels[i] / scale, 1.0), 0.0)
                levels[i] = levels[i]**exponent 
                levels[i] = int(levels[i] * 255)
                if levels[i] < cutoff:
                    levels[i] = 0

            cols = (1.0, 1.0, 1.0)
            c = 1.0
            x = c * (1.0 - abs(hue % 2.0 - 1.0))
            if hue > 6.0:
                hue = 0.0
            if hue < 1.0:
                cols = (1.0 * c, 1.0 * x, 0.0)
            elif hue < 2.0:
                cols = (1.0 * x, 1.0 * c, 0.0)
            elif hue < 3.0:
                cols = (0.0, 1.0 * c, 1.0 * x)
            elif hue < 4.0:
                cols = (0.0, 1.0 * x, 1.0 * c)
            elif hue < 5.0:
                cols = (1.0 * x, 0.0, 1.0 * c)
            elif hue < 6.0:
                cols = (1.0 * c, 0.0, 1.0 * x)

            # s = ser.read(6)
            r = 4.0 * cols[0]
            g = 4.0 * cols[1]
            b = 4.0 * cols[2]
            pix = [(level * r, level * g, level * b) for level in levels]
            hue += 0.02
            out.write(pix)

    except KeyboardInterrupt:
        print "\nStopping"
        stream.close()
        p.terminate()
        quit()

def calculate_levels(data, chunk, samplerate):
    # Use FFT to calculate volume for each frequency
    global MAX

    fmt = "%dH"%(len(data)/2)
    data2 = struct.unpack(fmt, data)
    data2 = numpy.array(data2, dtype='h')
    # Convert raw sound data to Numpy array
    # Apply FFT
    fourier = numpy.fft.fft(data2)
    ffty = numpy.abs(fourier[0:len(fourier)/2])/1000
    ffty1=ffty[:len(ffty)/2]
    ffty2=ffty[len(ffty)/2::]+2
    ffty2=ffty2[::-1]
    ffty=ffty1+ffty2
    ffty=numpy.log(ffty)-2
    
    fourier = list(ffty)[4:-4]
    fourier = fourier[:len(fourier)/2]
    
    size = max(MAX,len(fourier))

    # Add up for MAX lights
    levels = [sum(fourier[i:(i+size/MAX)]) for i in xrange(0, size, size/MAX)][:MAX]
    
    return levels

if __name__ == '__main__':
    #list_devices()
    music_visuals()
