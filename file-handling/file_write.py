# file_opener = ("demofile.txt", 'w')
# file_opener.write("some text as a content")
# file_opener.close()

#this will add the contents and 
#overwrite if the file have some existing data

file_opener = open("demofile.txt", "w")
file_opener.write("some new contents")
file_opener.close()