from myprogram2 import Calculator
import unittest

class TestMyprogram(unittest.TestCase):
    def setUp(self):
        print 'setUp'
        self.instance_variable = Calculator()
        
    def tearDown(self):
        print 'tearDown\n'

	def test_add(self):
		self.assertEqual(self.instance_variable.add(2,3), 5)

	def test_subtract(self):
		self.assertEqual(self.instance_variable.subtract(7,3), 4)
	
if __name__ == '__main__':
    unittest.main()		
