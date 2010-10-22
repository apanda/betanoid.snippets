#!/usr/bin/env python	
import sys
from StringIO import StringIO
from lxml import etree


def ReadProvisioningCertificate(provisioning_certificate):
    # Global xpath lets you find all sorts of keys in a plist
    xpath = etree.XPath('/plist/dict/key[text() = $key]')
    devices = []
    
    with open(provisioning_certificate) as fil:
        file_text = fil.read()
        xml_begin = file_text.find('<?xml')
        xml_end = file_text.find('</plist>') + len('</plist>')
        # trim to eliminate the random signature stuff
        xml = file_text[xml_begin : xml_end]
        xml_tree = etree.parse(StringIO(xml))
        subtrees = xpath(xml_tree, key = 'ProvisionedDevices')
        for subtree in subtrees:
            array = subtree.getnext()
            for device in array.iterchildren('string'):
                devices.append(device.text)
    
    for device in devices:
        print device

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Supply an argument")
    
    provisioning_certificate = sys.argv[1]
    ReadProvisioningCertificate(provisioning_certificate)
