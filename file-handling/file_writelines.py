file_opener = open("demofile.txt", 'w')

mysequence = ['hai', 'hello', 'bye']

file_opener.writelines(mysequence)
file_opener.close()