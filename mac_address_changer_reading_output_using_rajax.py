#!/usr/bin/env python

import subprocess
import optparse
import re

subprocess.call(["ifconfig"])
interface = input("Which Interface You Want To Read : ")

ifconfig_result = subprocess.check_output(["ifconfig", interface])

ifconfig_result = ifconfig_result.decode("utf-8")
print(str(ifconfig_result))

mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)
print("Your MAC Address is : ", str(mac_address_search_result.group(0)))
