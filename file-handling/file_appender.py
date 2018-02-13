file_opener = open("newfile2.txt", 'a')

file_opener.write("This is the new content and this wont overwrite")
file_opener.write("extra contents in new line" + "\n")
file_opener.write("some more extra contents" + "\n")
file_opener.close()