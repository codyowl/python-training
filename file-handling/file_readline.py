file_opener = open("newfile2.txt", 'r')
contents = file_opener.readline()

while contents:
	print contents
	contents = file_opener.readline()