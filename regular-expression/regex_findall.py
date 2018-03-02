import re

pattern_to_find = "hai"

mytext = "hai hello how are you ? and not only hai but also hai too"

myregex = re.findall(pattern_to_find, mytext)
  
print len(myregex)  
print myregex