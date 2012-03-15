Chroma-Lights
=============

Chroma lights is a frame work for running annimations for led lights over OSC.

Running
-------

In order to run the animations locally, we provide a lights emulator written in Processing.

To run the light emulator: `$ emulator/lights_emulator`

To run an animation: `$ ./run.py [animation name]`


Contributing
------------
To contribute add a new folder in the animation directory. 
This folder should be have a unique name for the animation.
The folder must contain the following two files:

main.py:

```python
import sys
sys.path.append("./osc")
from oscapi import ColorsOut
...
```

manifest.json:

```json
{
	"name":"Random Colors",
	"description":"Random colors on 3 second intervals",
	"creator":"RJ and Reed"
}
```

Each light recieves an input that is a tuple (r,g,b) where each of r, g, b can be 0-1023.

Construct an array of tuples and send them to the OSC server with 

```python
pix = [(1023.0,0.0,0.0)]*24
out = ColorsOut()
out.write(pix)
```

To add simple effects, such as automatic fade-in and fade-out of pixels, use the animations library in place of ColorsOut

```python
from animations import FadeAnimation
pix = [(1023.0,0.0,0.0)]*24
out = FadeAnimation()
out.FADERATE = 8.0 #optional
out.start()
out.write(pix)
```


