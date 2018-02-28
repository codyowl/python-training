import gc


i = 0

def cyclic_function():
	some_dict = {}
	some_dict[i+1] = some_dict
	print some_dict

collected = gc.collect()

print "Garbage collector collected %s" % collected

for i in range(10):
	cyclic_function()

collected = gc.collect()

print "Garbage collector: collected %s" % collected
	