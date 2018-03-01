class Superclass(object):
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class Subclass(Superclass):
    def get_value(self):
        return self.value + 1


s = Subclass()
# s = Superclass()
print s.get_value()        