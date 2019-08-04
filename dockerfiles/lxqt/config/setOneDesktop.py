#!/usr/bin/env python3
from xml.etree import ElementTree as ET

ET.register_namespace('', 'http://openbox.org/3.4/rc')
namespaces = {'rc': 'http://openbox.org/3.4/rc'}
filePath = "/etc/xdg/openbox/lxqt-rc.xml"

tree = ET.parse(filePath)
tree.find('rc:desktops/rc:number', namespaces).text = '1'
tree.write(filePath)