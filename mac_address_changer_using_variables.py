#!/usr/bin/env python

import subprocess
import optparse


subprocess.call("ifconfig", shell=True)

interface = input("Which Mac You Want To Change : ")

subprocess.call("ifconfig " + interface + " down", shell=True)

print("\nChanging Mac Address For " + interface)

new_mac = input("Enter 12 Digit New Mac Address For " + interface + ": ")

subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)
subprocess.call("ifconfig", shell=True)
