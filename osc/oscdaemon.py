#!/usr/bin/python
import daemon

import osc

with daemon.DaemonContext():
	osc.start()

