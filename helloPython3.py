print('100 + 200 = ', 100 + 200)
#name = input('please enter your name:')
#print('hello,',name)

a = 100
if a >= 0:
    print(a)
else:
    print(-a)	

print('I\'m \"OK\"!')

print('I\'m learning\nPython.')
print('\\\t\\')
print(r'\\\t\\')
print(r'''line1
line2
line3''')

age = 19

if age >= 18:
	print('adult')
else:
	print('teenager')	
	
	
a = 123
print(a)	
a = 'abc'
print(a)

print(10 /  3)
print(10 // 3)
print(10 % 3)
	
print('------------')	
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello,\'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello, Lisa!'''

print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)

print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))

print('\u4e2d\u6587')


x = b'ABC'
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
#print('中文'.encode('ascii'))

print(b'ABC'.decode('ascii'))
print( b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))


print(len('ABC'))
print(len('中文'))



print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))


print('Hello, %s' % 'world')


print('Hi, %s, you have $%d.' % ('Michael', 100000))


print('%2d-%02d' %  (3, 1))
print('%.2f' % 3.14324)


print('Age: %s. Gender: %s' % (25, True))

print('growth rae: %d %%' % 7)



classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)


print(len(classmates))

print(classmates[-1])
print(classmates[-2])
print(classmates[-3])
#print(classmates[-4])

classmates.append('Adam')
print(classmates)


classmates.insert(1, 'Jack')
print(classmates)


classmates.pop()
print(classmates)

a = classmates.pop(1)
print(a)
print(classmates)


classmates[1] = 'Sarah'
print(classmates)
L = ['Apple',123, True]
print(L)



s = ['python','java',['asp','php','scheme']]
print(len(s))


L = []
print(len(L))

classmates = ('Michael','Bob','Tracy')
print(classmates)


t = ()
print(t)
t= (1)
print(t)
t = (1,)
print(t)



t = ('a','b',['A','B'])


t[2][0] = 'X'
t[2][1] = 'Y'
print(t)




age = 20
if age >= 18:
	print('your age is',age)
	print('adult')
	
	
age = 3
if age >= 18:
	print('your age is',age)	
	print('adult')
else:
	print('your age is',age)	
	print('teenager')
	
	



age = 3
if age >= 18:
	print('adylt')
elif age >=	6:
	print('teenager')
else:
    print('kid')	

#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
if x:
	print('True')
	
	
#s = input('birth: ')	
#birth = int(s)
#if birth < 2000:
#	print('00前')
#else:
#	print('00后')
	
	
	
	
names = ['Michale','Bob','Tracy']	
for name in names:
	print(name)
	
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
	sum = sum + x
print(sum)


print(list(range(5)))

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print(sum)

L = ['Bart','Lisa','Adam']

for x in L:
	print(x)
	
n = 1
while n <= 100:
	if n > 10:
		break
	print(n)
	n = n + 1
print('END')


n = 0
while n < 10:
	n = n + 1
	print(n)

	
n = 0
while n < 10:
	n = n + 1
	if n % 2 == 0:
		continue
	print(n)

		
d = {'Michael': 95, 'Bob': 75,'Tracy': 85}
print(d['Michael'])

d['Adam'] = 67
print(d['Adam'])

d['Jack'] = 90
print(d['Jack'])
d['Jack'] = 88
print(d['Jack'])

print('Thomas' in d)


print(d.get('Thomas'))
print(d.get('Thomas', -1))

d.pop('Bob')
print(d)

#key = [1,2,3]
#d[key] = 'a list'

s = set([1,2,3])
print(s)



s = set([1,1,2,2,3,3])
print(s)
s.add(4)
print(s)
s.add(4)
print(s)


s.remove(4)
print(s)



s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)
print(s1 | s2)


a = ['c','b','a']
a.sort()


print(a)

a = 'abc'
b = a.replace('a', 'A')
print(b)
print(a)

print(abs(100))
print(abs(-20))
print(abs(12.34))


print(max(1, 2))
print(max(2, 3, 1, -5))


print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(''))

a = abs
print(a(-1))

def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x
		
		
		
def nop():
	pass
	
if age >= 18:
	pass
	
def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else: 
		return -x
		
import math

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny
	
	
x,y = move(100, 100, 60, math.pi / 6)
print(x, y)


r = move(100, 100, 60, math.pi / 6)
print(r)

def power(x):
	return x * x
	
def power(x, n):
	s = 1
	while n > 0:
		n = n -1
		s = s * x
	return s
	
	
print(power(5,2))
print(power(5,3))

def power(x, n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x
	return s
	
print(power(5))
print(power(5,2))
print(power(5, 3))

def enroll(name, gender, age=6,city='Beijing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:',city)

enroll('Sarah', 'F')    
enroll('BOb', 'M', 7)
enroll('Adam', 'M', city='Tianjin')

def add_end(L=None):
	if L is None:
		L = []
		L.append('END')
		return L
		
print(add_end())
print(add_end())


def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
	
calc(1,2)	
calc()
nums = [1,2,3]
calc(*nums)

def person(name, age, **kw):
	print('name:',name,'age:',age,'other:',kw)
	
person('Michael', 30)	
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')


extra = {'city':'Beijing','job':'Engineer'}
#person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)

def person(name, age, *, city, job):
	print(name, age, city, job)
	
person('Jack', 24, city='Beijing',job='Engineer')


def person(name,age,*args, city, job):
	print(name, age, args, city, job)

def person(name,age, *, city='Beijing',job):
	print(name, age, city, job)
	
	
person('Jack', 24, job='Engineer')	

def f1(a, b, c=0, *args, **kw):
	print('a =', a,'b = ',b,'c = ',c,'args = ',args,'kw =',kw)
	
def f2(a, b, c=0, *,d ,**kw):
	print('a =',a, 'b =',b,'c = ',c,'d = ',d,'kw = ',kw)	
	
	
f1(1,2)	
f1(1,2, c=3)
f1(1,2,3,'a','b')
f1(1,2,3, 'a','b',x=99)
f2(1,2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d':99,'x':'#'}
f1(*args, **kw)

args = (1,2,3)
kw = {'d': 88,'x':'#'}
f2(*args, **kw)

def fact(n):
	if n==1:
		return 1
	return n * fact(n - 1)	
print(fact(1))
print(fact(5))
print(fact(100))



def fact(n):
	return fact_iter(n,1)
	
	
def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)
	
	
print(fact(5))

L = []
n = 1
while n <= 99:
	L.append(n)
	n = n + 2
	
L = ['Michael','Sarah','Tracy','Bob','Jack']	
print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[-2:])
print(L[-2:-1])


L = list(range(100))
print(L)
print(L[:10])

print(L[-10:])
print(L[10:20])

print(L[:10:2])

print(L[::5])

print(L[:])


print((0,1,2,3,4,5)[:3])



print('ABCDEFG'[:3])
print('ABCDEFG'[::2])

d = {'a':1,'b':2,'c':3}
for key in d:
	print(key)
	
for value in d.values():
    print(value)

for k, v in d.items():
   print(k,v)


for ch in 'ABC':
	print(ch)
	
	
	
from collections import Iterable
    
print( isinstance('abc', Iterable))
print(isinstance([123], Iterable))
print(isinstance(123, Iterable))

for i , value in enumerate(['A','B','c']):
	print(i, value)
	
	
for x, y in [(1, 1),(2,4),(3,9)]:	
     print(x,y)



print(list(range(1,11)))

print([x * x for x in range(1, 11)])
   
print([x * x for x in range(1, 11) if x % 2 == 0])

mn = [m + n for m in 'ABC' for n in 'XYZ']
print(mn)


import os
dd = [d for d  in os.listdir('.')]
print(dd)
	

d = {'x':'A','y':'B','z':'C'}
for k, v in d.items():
	print(k,'=',v)
print([k + '=' + v for k, v in d.items()])	

L = ['Hello','World','IBM','Apple']
print([s.lower() for s in L])

x = 'abc'
y = 123
print(isinstance(x,str))
print(isinstance(y,str))


g = (x * x for x in range(10))
for n in g:
	print(n)


def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a + b
		n = n + 1
	return 'done'
	

print(fib(6))


def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a+b
		n = n + 1
	return 'done'
		

for n in fib(6):
    print(n)
g = fib(6)
while True:
	try:
		x = next(g)
		print('g:',x)
	except StopIteration as e:
		print('Generator return value:', e.value)	
		break
	
from collections import Iterable
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))


from collections import Iterator
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc',Iterator))


print(isinstance(iter([]), Iterator ))
print(isinstance(iter('abc'), Iterator))


# 首先获得Iterator对象
it = iter([1,2,3,4,5])
# 循环
while True:
	try:
		# 获得下一个值：
		x = next(it)
	except StopIteration:
		# 遇到StopIteration就退出循环
		break
		


f = abs
print(f(-10))


def add(x, y, f):
	return f(x) + f(y)
	
print(add(-5, 6, abs))

def f(x):
	return x * x
	
r = map(f, [1,2,3,4,5,6,7,8,9])

print(list(r))


print(list(map(str, [1,2,3,4,5,6,7,8,9])))

from functools import reduce

def add(x, y):
	return x + y
print(reduce(add,[1,3,5,7,9]))


def fn(x, y):
	return x * 10 + y
print(reduce(fn, [1,3,5,7,9]))


def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'0':0,'8':8,'9':9}[s]
print(reduce(fn, map(char2num, '13579')))




def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'0':0,'8':8,'9':9}[s]
	return reduce(fn, map(char2num, s))
	
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'0':0,'8':8,'9':9}[s]
def str2int(s):
	return reduce(lambda x, y: x * 10 + y, map(char2num, s))
	

def is_odd(n):
	return n % 2 == 1
	
	
	
print(list(filter(is_odd, [1,2,4,5,6,9,10,15])))


def not_empty(s):
	return s and s.strip()
l = list(filter(not_empty, ['A','','B',None,'C','  ']))
print(l)


print(sorted([36,5,-12,9,-21]))
print(sorted([36,5,-12,9,-21],key=abs))
print(sorted(['Bob','about','Zoo','Credit']))
print(sorted(['bob','about','Zoo','Credit'], key=str.lower, reverse=True))


def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax
	
	
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum
f = lazy_sum(1,3,5,7,9)

print(f)
print(f())

f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
print(f1==f2)


def count():
	def f(j):
		def g():
			return j*j
		return g
	fs = []
	for i in range(1,4):
	    fs.append(f(i))
	return fs
	
f1 ,f2 ,f3 = count()
print(f1(), f2(),f3())

l = list(map(lambda x: x * x, [1,2,3,4,5,6,7,8,9]))
print(l)


def f(x):
	return x * x
	
f = lambda x: x * x
print(f(5))
def build(x, y):
	return lambda: x * x + y * y
	
	
def now():
	print('2015-3-25')
f = now()
print(now.__name__)

	
def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper
    

@log
def now():
	print('2015-3-25')
now()


def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator


@log('execute')
def now():
	print('2015-3-25')
	
now()
	
now = log('execute')(now)
print(now.__name__)


import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*arg, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper
	
def log(text):
	def decorator(func):
	    @functools.wraps(func)
	    def wrapper(*args, **kw):
		    print('%s %s():'  % (text, func.__name__))
		    return func(*args, **kw)
	    return wrapper
	return decorator
    

def int2(x, base=2):
	return int(x, base)	
print(int2('1000000'))
print(int2('1010101'))


import functools
int2 = functools.partial(int, base=2)

max2 = functools.partial(max, 10)
print(max2(5,6,7))


class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score
		
	def print_score(self):
		print('%s: %s' % (self.name, self.score))
		
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

bart.print_score()
lisa.print_score()
print(bart.get_grade())

bart.age = 8
print(bart.age)
#print(lisa.age)


class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__scrore = score
	def print_score(self):
		print('%s: %s' % (self.__name,self.__scrore))
		
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__scrore

#    def set_score(self, score):		
#
#	    if 0 <= score <= 100:
#	    self.__scrore = score
#	    else:
#		     raise ValueError('bad score')

	
bart = Student('Bart Simpson', 59)
print(bart._Student__name)
bart = Student('Bart Simpson', 98)
print(bart.get_name())
bart.__name = 'New Name'
print(bart.__name)


print(bart.get_name())


	
class Animal(object):
	def run(self):
		print('Animal is running')
class Dog(Animal):
	def run(self):
		print('Dog is running')
	def eat(self):
		print('Eating meat...')
	
class Cat(Animal):
    def run(self):
	    print('Cat is running...')
    

dog = Dog()
dog.run()


cat = Cat()
cat.run()

		
a = list()
b = Animal()
c = Dog()
print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Animal))

def run_twice(animal):
	animal.run()
	animal.run()
run_twice(Animal())

run_twice(Dog())
run_twice(Cat())

class Tortoies(Animal):
    def run(self):
	    print('Tortoise is running slowly...')
	
		
run_twice(Tortoies())


class Timer(object):
    def run(self):
	    print('Start...')
	
	
print(type(123))
print(type('str'))
print(type(None))

print(type(abs))
print(type(a))



print(type(123)==int)
print(type('abc'==str))

import types
def fn():
	pass
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)


a = Animal()
d = Dog()

print(isinstance(d, Dog) and isinstance(d, Animal))

print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))


print(isinstance([1,2,3],(list, tuple)))		
print(isinstance((1,2,3),(list, tuple)))

print(dir('ABC'))

print(len('ABC'))
print('ABC'.__len__())

class MyDog(object):
	def __len__(self):
		return 100

dog = MyDog()
print(len(dog))




class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x
		
obj = MyObject()
print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
setattr(obj, 'y', 10)
print(hasattr(obj, 'y'))
print(obj.y)

print(getattr(obj, 'z',404))

print(hasattr(obj, 'power'))
print(getattr(obj, 'power'))
fn = getattr(obj, 'power')

print(fn())

def readImage(fp):
	if hasattr(fp, 'read'):
		return readData(fp)
	return None



		
	