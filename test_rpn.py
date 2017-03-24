import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
	def test_subtract(self):
		result = rpn.calculate('5 3 -')
		self.assertEqual(2, result)
	def test_exponential(self):
		result = rpn.calculate('3 2 ^')
		self.assertEqual(9,result)
	def test_extra(self):
		result = rpn.calculate('6 6 &')
		self.asserEqual(9,result)
