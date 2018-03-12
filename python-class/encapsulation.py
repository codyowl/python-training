class College(object):
    def __init__(self):
        self.course_name = "computer science first"    # OK to access directly
        self._course_name = "computer science second"   # should be considered private
        self.__course_name = "computer science third" 


c = College()


print c.course_name

print c._course_name

# print c.__course_name    

print c._College__course_name   

