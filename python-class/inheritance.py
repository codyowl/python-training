class Firstclass:
	def first_function(self):
		print "text from first function"

class Subclass(Firstclass):
    def second_function(self):
    	print "text from second function"

S = Subclass()

S.first_function()

S.second_function()
