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








	

	