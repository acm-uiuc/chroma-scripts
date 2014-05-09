import sys
import urllib2
import simplejson
from animations import FadeAnimation

URL = "http://sitesquares.herokuapp.com/colors?tail=24"
if __name__ == "__main__":
    import time
    out = FadeAnimation()
    out.FADERATE = 8.0
    out.start()

    while True:
        f = urllib2.urlopen(URL)
        data = f.read()
        data = data[1:-2]
        data = simplejson.loads(data)
        pix = [(0.0,0.0,0.0)]*24
        for i in range(24):
            item = data[i]
            color = item["color"]
            r = int('0x'+color[0:2],16)
            g = int('0x'+color[2:4],16)
            b = int('0x'+color[4:6],16)
            pix[i]=(r*4.0,g*4.0,b*4.0)
        out.write(pix)
        time.sleep(2.7)
