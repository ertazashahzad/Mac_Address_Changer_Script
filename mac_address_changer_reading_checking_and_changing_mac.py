#!/usr/bin/env python

import os
import subprocess
import re

os.system("clear")


def getting_mac_address(interface):
    subprocess.call(["ifconfig", interface])
    search_result = subprocess.check_output(["ifconfig", interface])
    search_result = search_result.decode("utf-8")

    mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", search_result)

    if mac_address:
        return str(mac_address.group(0))
    else:
        print("\nThe Interface is Invalid, Please Chose a different one\n\n")
        input("Press Any Key To Continue . . .")
        os.system("clear")
        getting_mac_address(interface)


def validating_and_changing_mac(mac_address, interface):
    os.system("clear")

    subprocess.call(["ifconfig", interface])
    new_mac = input("\n Please Enter New 12 Digit MAC : ")

    if mac_address != new_mac:

        subprocess.call(["ifconfig",interface,"down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
        os.system("clear")
        subprocess.call(["ifconfig", interface])

        print("\nSuccessfully Changed MAc Address".center(50))
        subprocess.call(["ifconfig",interface,"up"])
        input("\n\n Press Any Key To Exit . . .")
        return

    else:
        print("\n Your OLD MAC IS :  ", str(mac_address), "\n Your NEW MAC IS : ", str(new_mac),
              "\n Please Chose Different MAC From OLD MAC \n")
        input("Press Any Key To Continue . . .")
        os.system("clear")
        validating_and_changing_mac(mac_address, interface)


subprocess.call(["ifconfig"])
interface = input("Please Chose Interface : ")
mac_address = getting_mac_address(interface)
validating_and_changing_mac(mac_address,interface)
