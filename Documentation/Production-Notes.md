Production Notes
================

Chroma is currently running on `siebl-1104-06` and the code is in `/opt/chroma`.

Restarting the server
=====================
To restart the server, do the following on the machine.

```
sudo su
cd /opt/chroma/chroma-scripts
source activate
cd osc
screen python oscapi.py
# Check for errors. If the screen stays blank, then do Ctrl-a d to detach from the screen.
exit
```

Running an animation
====================
If the server is running, run an animation with:
```
cd /opt/chroma/chroma-scripts
source activate
screen python run.py [animation name] # pass -h to see possible animations
# if no error, then Ctrl-a d to detach screen
exit
```

Troubleshooting
===============

  * Try restarting the power supply (by pulling the plug).
  * Tey unplugging and plugging the USB cords (on the hub) back in.
  * Verify that all of the devices in `osc/devices.txt` actually exist. If they do not then try the above regarding USB ports.