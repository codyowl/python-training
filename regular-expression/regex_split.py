import re

pattern_to_split = "h"

mytext = "hai hello how are you ? and not only hai but also hai too"

myregex = re.split(pattern_to_split, mytext)
  
print myregex  