from math import sqrt
from animations import FadeAnimation
import requests
from PIL import Image
from StringIO import StringIO
from time import sleep
from collections import namedtuple
Color = namedtuple("Color", ["r","g", "b"])
# author: Harsh Singh
light_count = 48
rows = 8
cols = 6
out = FadeAnimation()
out.FADEINRATE = 2  # optional
out.FADEOUTRATE = 8  # optional, makes things 'trail off'
out.start()

pix = [(1023.0, 0.0, 0.0)] * light_count


class ImagePoint(object):

    """docstring for Point"""

    def __init__(t, size, rows, cols, x=0, y=0):
        super(ImagePoint, t).__init__()
        t.x = x
        t.y = y
        t.rows = rows
        t.cols = cols
        t.size_x, t.size_y = size
        t.done = False
        t.direction = "right"

    def move_down(t):
        print "called down"
        t.direction = "down"
        t.down_count = 0
        t.move()

    def move(t):
        if t.direction is "right":
            if t.x == t.size_x - t.cols - 1:
                t.next_direction = "left"
                t.move_down()
            else:
                t.x += 1
        elif t.direction is "left":
            if t.x - 1 < 0:
                t.next_direction = "right"
                t.move_down()
            else:
                t.x -= 1
        elif t.direction is "down":
            if t.y is t.size_y:
                if t.last_row:
                    t.done = True
                t.last_row = True
                t.direction = t.next_direction
            elif t.down_count + 1 is t.rows:
                # change rows to 2 condition for less jumpy
                t.direction = t.next_direction
            else:
                t.down_count += 1
                t.y += 1

    def similar_frame(t, img_data):
        # http://stackoverflow.com/questions/8863810/python-find-similar-colors-best-way
        a = Color(*img_data[t.x, t.y])
        b = Color(*img_data[t.x + t.cols-1, t.y])
        rm = 0.5*(a.r+b.r)
        return abs(((2+rm) * (a.r-b.r)**2) + 4*(a.g-b.g)**2 + ((3-rm) * (a.b-b.b)**2))**.5 < 10

    def write_frame(t, out, img_data):
        """
        Given a frame larger than grid size, select only values starting from top left to fit grid
        """
        result = [rgb_to_lights(img_data[t.x + i, t.y + j]) for i in xrange(t.cols) for j in xrange(t.rows)]
        out.write(result)


def longest_side():
    return max(rows, cols)


def get_image():
    url = "https://api.flickr.com/services/rest/?method=flickr.photos.getRecent&api_key=88a7df8d4b7696c5de97f5fc97c75c91&format=json&nojsoncallback=1"
    recent_image = requests.get(url).json()["photos"]["photo"][0]
    picture_url = "http://farm{farm_id}.staticflickr.com/{server_id}/{id}_{secret}.jpg".format(
        farm_id=recent_image["farm"], server_id=recent_image["server"], id=recent_image["id"], secret=recent_image["secret"])
    img = Image.open(StringIO(requests.get(picture_url).content))
    return img

def rgb_to_lights(rgb):
    return [i * 4.0 for i in rgb]

def animation_picture_slider():
    img = get_image()
    size = img.size
    img_data = img.load()
    speed = .15
    point = ImagePoint(size, rows, cols)
    while (not point.done):
        point.write_frame(out, img_data)
        point.move()
        if point.similar_frame(img_data):
            if speed > .01:
                speed *= .9
        elif speed < .16:
            speed *=1.04
        sleep(speed)


if __name__ == "__main__":
    while True:
        animation_picture_slider()
