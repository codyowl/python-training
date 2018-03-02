# -*- coding: utf-8 -*-

import re

unicode1 = re.search(r"\w+", u"♥αβγ!", re.U)
unicode2 = re.search(r"\w+", u"♥αβγ!")

if unicode1:
    print unicode1.group().encode("utf8") # → 「αβγ」
else:
    print "no match"

print unicode2   