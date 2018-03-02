import re

mystring = "steve jobs Billgates Mark zuckerberg"

mypattern = '(s\w+)'

myregex = re.match(mypattern, mystring)

#print myregex.groups(0)

if myregex:
	print myregex.groups(0)
else:
    print "It is not at starting or not such a thing"	