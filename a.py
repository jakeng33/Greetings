Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=324
>>> b=2
>>> c=a-b
>>> c
322
>>> print'a-b is', c
a-b is 322
>>> 2+3=5
SyntaxError: can't assign to operator
>>> 2+3==5
True
>>> 2+3
5
>>> 18%5
3
>>> 4%2
0
>>> 2**2
4
>>> 18/5
3
>>> float(18)/5
3.6
>>> A='hihi'
>>> A*2
'hihihihi'
>>> A+2

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    A+2
TypeError: cannot concatenate 'str' and 'int' objects
>>> A**(-1)

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    A**(-1)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> A**-1

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    A**-1
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
>>> 3**2 + 4**2
25
>>> 25**-1
0.04
>>> 25**-2
0.0016
>>> 25**1/2
12
>>> 25**(-2)
0.0016
>>> 3**2+5**2
34
>>> 912**2 + 947**2
1728553
>>> hihi=[0:10]
SyntaxError: invalid syntax
>>> hihi=[1:30]
SyntaxError: invalid syntax
>>> hihi=[a,b,c,d,f]

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    hihi=[a,b,c,d,f]
NameError: name 'd' is not defined
>>> hihi=['a','b','c','d','f']
>>> hihi
['a', 'b', 'c', 'd', 'f']
>>> print hihi
['a', 'b', 'c', 'd', 'f']
>>> a='HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain'
>>> a[0:22]
'HumptyDumptysatonawall'
>>> a[22:27]
'Humpt'
>>> a[27:97]
'yDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumpty'
>>> a[97:102]
'Dumpt'
>>> s=a[0:22]
>>> b=a[22:27]
>>> c=a[27:97]
>>> d=a[97:102]
>>> s+b
'HumptyDumptysatonawallHumpt'
>>> s-b

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    s-b
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> s - b

Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    s - b
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> a[:27]
'HumptyDumptysatonawallHumpt'
>>> a[:22]
'HumptyDumptysatonawall'
>>> a[22:27]
'Humpt'
>>> a.append['y']

Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.append['y']
AttributeError: 'str' object has no attribute 'append'
>>> a[22:27].append['y']

Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a[22:27].append['y']
AttributeError: 'str' object has no attribute 'append'
>>> b.append=('y')

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    b.append=('y')
AttributeError: 'str' object has no attribute 'append'
>>> b
'Humpt'
>>> b.append('y)
	 
SyntaxError: EOL while scanning string literal
>>> b.append9'y')
SyntaxError: invalid syntax
>>> b.append('y')

Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    b.append('y')
AttributeError: 'str' object has no attribute 'append'
>>> a[22:27]
'Humpt'
>>> [22:28]
SyntaxError: invalid syntax
>>> a[22:28]
'Humpty'
>>> d
'Dumpt'
>>> a[97:107]
'Dumptyinhi'
>>> a[97:103]
'Dumpty'
>>> a[22:28]+a[97:103]
'HumptyDumpty'
>>> a[22:28]+ ' '+ a[97:103]
'Humpty Dumpty'
>>> a='cxw6jwCMelanocoryhpaSw3LdKVoqDFus6li28pdsHAsx35ff8WiCUTzcbgaMUOGgDdkMkbgalericulataZZlZuSCV2O4TPdOucvUjt9UsK5VcxFiKGtlm6WDu1oVew5Iyfr7nr4nbznpsHNbUh0Y7B7QGV6Hdg8ZXGS5vHh'
>>> a[7:19]
'Melanocoryhp'
>>> a[7:20] +' '+ a[71:83]
'Melanocoryhpa galericulata'
>>> a = 42
if a < 10:
	
>>> print 'the number is less than 10'
else:
  print 'the number is greater or equal to 10'
  
the number is less than 10
>>> 5
5
>>> a = 42
if a < 10:
	
>>> a = 42
if a < 10:
print 'the number is less than 10'
else:
  print 'the number is greater or equal to 10'
  
>>> 3
3
>>> a==4
False
>>> a=4
>>> a
4
>>> a = 42
if a < 10:
  print 'the number is less than 10'
else:
  print 'the number is greater or equal to 10'
  
>>> a=2
>>> a = 42
if a < 10:
  print 'the number is less than 10'
else:
  print 'the number is greater or equal to 10'
  
>>> a
42
>>> a==2
False
>>> a==42
True
>>> print a=3
SyntaxError: invalid syntax
>>> print a
42
>>> n = 10
for i in range(n):
  print i
  
>>> i

Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    i
NameError: name 'i' is not defined
>>> print i

Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    print i
NameError: name 'i' is not defined
>>> f = open('input.txt', 'r')

Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    f = open('input.txt', 'r')
IOError: [Errno 2] No such file or directory: 'input.txt'
>>> os.chdir('C:\Users\Wicked\Desktop\CODET')

Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    os.chdir('C:\Users\Wicked\Desktop\CODET')
NameError: name 'os' is not defined
>>> os.getcwd

Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    os.getcwd
NameError: name 'os' is not defined
>>> os.getcwd()

Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    os.getcwd()
NameError: name 'os' is not defined
>>> chdir(C:\Users\Wicked\Desktop\CODET)
SyntaxError: invalid syntax
>>> chdir('C:\Users\Wicked\Desktop\CODET')

Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    chdir('C:\Users\Wicked\Desktop\CODET')
NameError: name 'chdir' is not defined
>>> import os
chdir('C:\Users\Wicked\Desktop\CODET')

>>> getcwd()

Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    getcwd()
NameError: name 'getcwd' is not defined
>>> os.getcwd()
'C:\\Python27'
>>> os.chdir('C:\Users\Wicked\Desktop\CODET')
>>> os.getcwd()
'C:\\Users\\Wicked\\Desktop\\CODET'
>>> f = open('input.txt', 'r')

Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    f = open('input.txt', 'r')
IOError: [Errno 2] No such file or directory: 'input.txt'
>>> 
