class Myclass:
	def my_function(self, myargument=None):
		self.myargument = myargument
	def get_value(self):
	    return self.myargument

M = Myclass()

M.my_function()
print M.get_value()

print "now method over loading"

M = Myclass()

M.my_function("something")
print M.get_value()


