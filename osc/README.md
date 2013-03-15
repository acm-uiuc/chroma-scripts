# Chroma Lights Library
This is the dark side of chroma, the library that's both the server code and client libraries. A quick runthrough:

##Client code:
* `oscapi.py` - the bulk of our code. contains the library to send out chroma messages, wraps them in pretty OSC messages, and sends them to the server.
* `animations.py` - all sorts (ok just one class) of handy classes to do smooth animations and stuff. Automatically included in the path when run.py is used.

##Server code:
* `oscapi.py` - the bulk of our code. In addition to housing the core client code, it also contains the server, which deserializes the messages, potentially doing some fancy magic to avoid conflicts, and sends them to the arduino module.
* `octoapy.py` - the code that actually interfaces with the arduinos. It supports multiplexing to multiple arduinos, and reorders them based on the config (see below). It's a bit rough, but attempts to retry if an arduino gets knocked out.
* `config.py` - a simple module that rearranges the lights however you see fit.
* `devices.txt` - another simple file that lists the full paths of all arduinos that should be communicated with
* `sendcommands.py' - a handy script to send config OSC messages to the server.
* `osc.py` - a library. ignore it.
* `oscdaemon.py` - ignore it as well.
* `daemon/` - some code do daemonize `oscapi.py`.

### Running the Chroma server
In general, running `python oscapi.py` will run the server in the foreground just fine. Be careful about dependencies (see the main page for virtualenv help).
However, if you want to daemonize it, enter the `daemon/` folder and run `./startserver.sh`.

While running, you can use `./sendcommands.py MESSAGE` to send various messages to it. run it without a parameter to see what's available.
