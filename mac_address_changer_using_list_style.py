#!/usr/bin/env python

import subprocess
import optparse


subprocess.call(["ifconfig"])
interface = input("Which Mac You Want To Change : ")
subprocess.call(["ifconfig", interface, "down"])

new_mac = input("Enter 12 Digit New Mac Address For " + interface + ": ")
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
subprocess.call(["ifconfig"])