class Dict(dict):
	def __init__(self, **kw):
		super.__init__(**kw)
		
	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
	def __setattr__(self, key, value):
		self[key] = value

import unittest
from mydict import Dict
class TestDict(uuittest.TestCase):
	
	def test_init(self):
		d = Dict(a=1, b='test')
		self.assertEqual(d.a, 1)
		self.assertEqual(d.b, 'test')
		self.assertEqual(isinstance(d, dict))
	
	def test_key(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'], 'value')
	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.aseertEqual(d.key, 'value')
	
	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']
	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty
			
			
			
class TestDict(unittest.TestCase):
	def seUp(self):
		print('setup...')
	def tearDown(self):
		print('tearDown...')
		
def abs(n):
	'''
	Function to get absolute value of number.
	
	Example:
		
	>>> abs(1)
	1
	>>> abs(-1)
	1
	>>> abs(0)
	0
	'''
	