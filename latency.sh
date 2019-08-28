#!/usr/bin/env python3

import subprocess
from xml.etree import ElementTree

outLine = subprocess.check_output(
    ["curl", "-w", "%{time_connect}\\n", "-o", "/dev/null", "-s", "https://dynamodb.eu-west-1.amazonaws.com/"],
).decode("utf-8")

ms = float(outLine.splitlines()[0]) * 1000
print("curl: {:.2f} ms".format(ms))




xmlStr = subprocess.check_output(
    ["nmap", "-p80", "--oX", "-", "dynamodb.eu-west-1.amazonaws.com"],
).decode("utf-8")

tree = ElementTree.fromstring(xmlStr)
ms = int(tree.find('host/times').attrib["srtt"]) / 1000
print("nmap: {:.2f} ms".format(ms))
