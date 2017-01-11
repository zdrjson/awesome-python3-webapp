#class FooError(ValueError):
#	pass
#
#def foo(s):
#	n = int(s)
#	if n==0:
#		raise FooError('invalid value: %s' % s)
#	return 10 / n
#	
#foo('0')

import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)


#s = '0'
#n = int(s)
#print(10 / n)


