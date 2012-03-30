Chroma-Lights
=============

Chroma lights is a frame work for running annimations for led lights over OSC.

Setup
-----
Install virtualenv (skip if you have it already).

```bash
sudo easy_install virtualenv
```

Move on to running to get the environment activated and dependencies checked.

###Windows users
Scroll down to see instructions since there are a buttload.

Running
-------
There is a simple emulator provided that will start automatically when run.py is executed if it's not running already.
In your chrome-scripts directory, run the activate script. If this is your first time running it, give it a bit to fetch dependencies and setup the environment:

```bash
source activate
```

To run an animation:

```bash
./run.py [animation name]
```

If you're on zsh, tab completion should work too. If there isn't a server or emulator started, it will start the emulator for you automatically.

When you're done hacking, `deactivate` to get exit out of virtualenv.
Contributing
------------
To contribute add a new folder in the animation directory. 
This folder should be have a unique name for the animation.
The folder must contain the following two files:

main.py:

```python
import sys
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
out.FADEINRATE = 2.0 #optional
out.FADEOUTRATE = 8.0 #optional, makes things 'trail off'
out.start()
out.write(pix)
```

Tips and Tricks
---------------

Chroma is bright, and can easily be the predominant lighting in the room.  Fast blinking of the lights can be intense, so be considerate.

* Avoid instantaneous changes in both intensity and color
* Use the provided animation framework to transition between colors

Windows Setup Cont'd
--------------------
###### 0. Install Python 2.x from http://www.python.org/getit/

###### 1. Download and run Processing for Windows from http://processing.org/download/

###### 2. Install the oscP5 library from http://www.sojamo.de/libraries/oscP5/

###### 3. Run chroma-scripts\emulator\source\lights_emulator\lights_emulator.pde in processing

###### 4. Add "C:\Python2x" and "C:\Python2x\Scripts" to your PATH environment variable

###### 5. Install the setup tools as described here: http://pypi.python.org/pypi/setuptools

###### 6. Download and fully extract this file: http://pypi.python.org/pypi/pip#downloads

###### 7. Go to the extracted directory and run 
```bash
python setup.py install
```
```bash
pip install virtualenv
```

###### 8. Change directory to chroma-scripts and run
```bash
virtualenv env
```
```bash
env\Scripts\activate
```
```bash
pip install -r dependencies.txt
```
```bash
python run.py random
```
Note: be sure (env) is displayed at the beginning of every command line when running scripts, or else it will not work!

###### 9. Check your emulator. It should be displaying random colors.