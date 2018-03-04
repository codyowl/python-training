try:
	file_opener = open("somefile.txt","r")
except IOError:
    print "We can't do any operations"
finally:
    print "anyway this will be printed"    	