import myprogram
import unittest

class TestMyprogram(unittest.TestCase):
	def test_integer_value_getter(self):
		data_type = myprogram.integer_value_getter(5)
		self.assertEqual(type(data_type), int)

	def test_integer_value_getter(self):
		data_type = myprogram.integer_value_getter("something")
		self.assertNotEqual(type(data_type), int)

	
if __name__ == '__main__':
    unittest.main()		
