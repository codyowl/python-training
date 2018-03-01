class College:
    def __init__(self, name):    # Constructor of the class
        self.name = name
    def certificate(self):              # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

class Undergraduate(College):
    def certificate(self):
        return 'Will get a ug certificate'

class Postgraduate(College):
    def certificate(self):
        return 'Will get a pg certificate'

colleges = [Undergraduate('IIT'),
           Undergraduate('MIT'),
           Postgraduate('Anna university')]

for college in colleges:
    print college.name + ': ' + college.certificate()

