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
	
	
s = input('birth: ')	
birth = int(s)
if birth < 2000:
	print('00前')
else:
	print('00后')
	





	