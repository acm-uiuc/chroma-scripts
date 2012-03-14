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
`import sys
sys.path.append("./")
from osc import ColorsOut`


manifest.json:
`{
	"name":"Random Colors",
	"description":"Random colors on 3 second intervals",
	"creator","RJ and Reed"
}`
