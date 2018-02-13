file_reader = open("newfile2.txt", 'r')
#contents = file_reader.read()
#print contents

#======================================
contents_line = file_reader.readlines()

for data in contents_line:
	print "The data is : %s" % (data)