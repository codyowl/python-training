import re

mytext = """The good part of opensource softwares is,
It is opensource"""

myregex1 = re.findall(r".+", mytext)
myregex2 = re.findall(r".+", mytext, re.DOTALL)

print myregex1                        
print myregex2

print "Length of first regex pattern result"
print len(myregex1)

print "Length of second regex pattern result"
print len(myregex2)                        