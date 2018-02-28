class Myfirstclass:
	def my_first_function(self, argument1):
		self.argument1 = argument1

#we need an instance to run our class:
myinstance = Myfirstclass()

#now myinstance is capable of accessing all the things Myfirstclass do
myinstance.my_first_function()

#======================================================================

'''
Now when we call myinstance.my_first_function(firstargument)

Python treats the above code like this

Myfirstclass.my_first_function(myinstance, argument1) => This is where self variable comes
'''		