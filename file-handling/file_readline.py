file_opener = open("demofile.txt", 'r')
contents = file_opener.readline()

while contents:
	print contents
	contents = file_opener.readline()