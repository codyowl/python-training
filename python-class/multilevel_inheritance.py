class A:
	def first_function(self):
		print "text from first function"

class B(A):
    def second_function(self):
        print "text from second function"

class C(B):
    def third_function(self):
    	print "text from third function"


c = C()

c.first_function()
c.second_function()
c.third_function()    	        		