class College(object):
    def __init__(self):
        self._name = None

    @property
    def name(self):
        print("getter of x called")
        print self._name

    @name.setter
    def name(self, value):
        print("setter of x called")
        self._name = value

    @name.deleter
    def name(self):
        print("deleter of x called")
        del self._name


c = College()
c.name = 'Anna university'  # setter called

print "setter"
print c.name

name_value = c.name    # getter called

print "getter"
print name_value

del c.name      # deleter called
print c.name