#!/usr/bin/env python

import subprocess
import optparse



subprocess.call("ifconfig", shell=True)
subprocess.call("ifconfig eth0 down", shell=True)
subprocess.call("ifconfig eth0 hw ether 50:11:22:33:44:66", shell=True)
subprocess.call("ifconfig eth0 up", shell=True)
subprocess.call("ifconfig", shell=True)
