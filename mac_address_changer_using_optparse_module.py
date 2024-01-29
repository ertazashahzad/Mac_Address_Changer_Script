#!/usr/bin/env python

import subprocess
import optparse


parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Name of Interface to change MAC Address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")

(options, arguments) = parser.parse_args()

subprocess.call(["ifconfig"])
interface = options.interface
subprocess.call(["ifconfig", interface, "down"])

new_mac = options.new_mac
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
subprocess.call(["ifconfig"])
