file_opener = open("newfile2.txt", 'r')
contents = file_opener.readlines()

print contents
for data in contents:
	print "data is %s" % (data)