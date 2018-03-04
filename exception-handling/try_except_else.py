# file_opener = open("something", "r")

#====================================

try:
	file_opener = open("something.txt", "r")

except IOError:
    print "We can't open this file"	

else:
	print "we can open this file and do whatever we want"


	