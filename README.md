Chroma-Lights
=============

Chroma lights is a frame work for running annimations for led lights over OSC.

Running
-------
To run an animation run `./run.py [animation name]`


Contributing
------------
To contribute add a new folder in the animation directory. 
This folder should be have a unique name for the animation.
The folder must contain the following two files:

main.py:

```python
import sys
sys.path.append("./osc")
from osc import ColorsOut
...
```

manifest.json:

```json
{
	"name":"Random Colors",
	"description":"Random colors on 3 second intervals",
	"creator","RJ and Reed"
}
```

Each light recieves an input that is a touple (r,g,b) where each of r, g, b can be 0-1023.

Construct an array of touples and send them to the OSC server with 

```python
pix = [(0.0,0.0,0.0)]*24
out = ColorsOut()
out.write(pix)
```


To run the light emulator:

```bash
$ emulator/lights_emulator 
```
