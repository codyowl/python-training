import re


pattern1 = re.compile(r"""\d +  # the integral part
                   \.    # the decimal point
                   \d *  # some fractional digits""", re.X)

pattern2 = re.compile(r"\d+\.\d*")    # pattern p2 is same as p1

myregex1 = re.findall(pattern1, u"a3.45")
myregex2 = re.findall(pattern2, u"a3.45")

print myregex1[0].encode("utf8")      # 3.45
print myregex2[0].encode("utf8")      # 3.45