#!/usr/bin/env python3

import xml.etree.ElementTree as ET
import csv

def parseXml():
    tree = ET.parse('./sample.xml')
    root = tree.getroot()
    outStr = ''
    depth=0
    with open('sample.csv', mode='w') as f:
        for child1 in root:
            count = 0
            for child2 in child1:
                outStr = outStr + str(root[depth][count].text) + ","
                count += 1
            outStr = outStr + "\n"
            f.write(outStr)
            depth += 1


if __name__ == '__main__':
    parseXml()


