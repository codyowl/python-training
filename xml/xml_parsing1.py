import xml.etree.ElementTree as ET
tree = ET.parse('xml_parsing1.xml')
root = tree.getroot()

# print root

#printing tag and attribute
# print root.tag

# print root.attrib

# for childrennode in root:
#  	print childrennode.tag

# for childrennode in root:
#     print childrennode.attrib

# for neighbor in root.iter('neighbor'):
#     print neighbor.attrib
    	
for country in root.findall('country'):
	rank = country.find('year').text
	print rank
 	