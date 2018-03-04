# try:
# 	file_opener = open("somefile", "r")
# except IOError, e:
#     print "We can't do any operations because %s is raised" % (e)

#Second approach
try:
	file_opener = open("somefile", "r")
except IOError as e:
    print "We can't do any operations because %s is raised" % (e)    