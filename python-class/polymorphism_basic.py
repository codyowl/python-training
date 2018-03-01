class Teacher(object):
    def Assignment(self):
        raise NotImplementedError

class Student(Teacher):
    def Assignment(self):
        print "Assignment of student1"

class GradStudent(Teacher):
    def Assignment(self):
        print "Assignment of student2"


#First student instance
print "#######first student instance#######"
S = Student()
S.Assignment()

print "====================================" + '\n'

#Second student instance
print "######Grad student instance######"
G = GradStudent()
G.Assignment()