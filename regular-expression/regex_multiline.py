import re

mytext = """stevejobs
billgates
markzuckerberg"""

myregex1 = re.findall(r"^\w", mytext)
myregex2 = re.findall(r"^\w", mytext, flags = re.MULTILINE)

print myregex1                        
print myregex2                        