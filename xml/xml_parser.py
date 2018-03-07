import xml.etree.ElementTree as ET

xmlfile = "something.xml"

tree = ET.parse(xmlfile)

root = tree.getroot()

print root

#XML parsing at very basic level


