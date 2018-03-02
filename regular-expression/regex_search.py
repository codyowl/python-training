import re

pattern_to_find = "good soul"

long_text = "Linus torvalds who is the founder of linux is such a good soul"

myregex = re.search(pattern_to_find, long_text)

if myregex:
	print "Yes the matching pattern found !"
else:
    print "No the mathching pattern is not found"	