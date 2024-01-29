#!/usr/bin/env python

import subprocess
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Name of Interface to change MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    return parser.parse_args()


def change_mac(interface, new_mac):
    print("\n -------------------- OLD MAC Address -------------------------\n")
    subprocess.call(["ifconfig"])
    print("\n -------------------- New MAC Address -------------------------\n")

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig"])


(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)
