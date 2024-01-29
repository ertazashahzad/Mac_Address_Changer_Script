#!/usr/bin/env python

import subprocess
import optparse


subprocess.call(["ifconfig"])
interface = input("Which Interface You Want To Read : ")


ifconfig_result = subprocess.check_output(["ifconfig", interface])
print(ifconfig_result)

