Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = 42
>>> if a < 10:
	print 'chotri'
	else
	
SyntaxError: invalid syntax
>>> if a < 10:
	print ' chotri'
else:
	print 'tricho'

	
tricho
>>>  a = 6
 
  File "<pyshell#9>", line 2
    a = 6
    ^
IndentationError: unexpected indent
>>> a
42
>>> a = 6
>>> b = -2
>>> if a + b == 4
SyntaxError: invalid syntax
>>> if a + b == 4:
	print " troi oi bang 4 that kia"
print " eo phai 4"
SyntaxError: invalid syntax
>>> 
>>> 
>>> if a + b == 4:
	print " troi oi bang 4 that kia"

	
 troi oi bang 4 that kia
>>> if a + b == 4
SyntaxError: invalid syntax
>>> if a+b==4:
	print ' troi oi bang 4 that kia '
print ' huhm'
SyntaxError: invalid syntax
>>> if a+b==4:
	print ' troi oi bang 4 that kia '

 troi oi bang 4 that kia 
>>> if a+b==4:
	print ' troi oi bang 4 that kia 'print ' huhm'
	
SyntaxError: invalid syntax
>>> if a+b==4:
	print ' troi oi bang 4 that kia '
	print ' huhm '

	
 troi oi bang 4 that kia 
 huhm 
>>> f= open('input.txt', 'r')

Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    f= open('input.txt', 'r')
IOError: [Errno 2] No such file or directory: 'input.txt'
>>> getcwd()

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    getcwd()
NameError: name 'getcwd' is not defined
>>> os.getcwd()

Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    os.getcwd()
NameError: name 'os' is not defined
>>>  os.getcwd()
 
  File "<pyshell#33>", line 2
    os.getcwd()
    ^
IndentationError: unexpected indent
>>> import os
>>> os.getcwd()
'C:\\Python27'
>>> greetings = 1
>>> while greetings <= 3
SyntaxError: invalid syntax
>>> while greeting <=3
SyntaxError: invalid syntax
>>> while greeting <=3:
	print 'hello' *greetings
	greetings = greetings + 1

	

Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    while greeting <=3:
NameError: name 'greeting' is not defined
>>> while greetings <=3:
	print 'hello' *greetings
	greetings = greetings + 1

	
hello
hellohello
hellohellohello
>>> names = ['Alice', 'Bob', 'Charley']
>>> for name in names:
	print 'hello, ' + name

	
hello, Alice
hello, Bob
hello, Charley
>>> leaves = [ 'la 1', 'la 2', 'la 3']
>>> for leaf in leaves :
	print 'dem' + leaf

	
demla 1
demla 2
demla 3
>>> names = ['Alice', 'Bob', 'Charley']
>>> for 1 in names:
	print '22'+ name
	
SyntaxError: can't assign to literal
>>> n=10
>>> for i in range (n):
	print i

	
0
1
2
3
4
5
6
7
8
9
>>> print range(5,12)
[5, 6, 7, 8, 9, 10, 11]
>>> while a < b < 10000:
	for i in range (a, b):
		if i % 2 = 1:
			
SyntaxError: invalid syntax
>>> 
>>> while a < b < 10000:
	for i in range (a, b) and i % 2 = 1
	
SyntaxError: invalid syntax
>>> while a < b < 10000:
	or i in range (a, b) and i % 2 = 1:
		
SyntaxError: invalid syntax
>>> while a < b < 10000:
	for i in range (a, b) and i % 2 = 1:
		
SyntaxError: invalid syntax
>>> 
>>> 
>>> while a < b < 10000:
	for i in range (a,b)
	
SyntaxError: invalid syntax
>>> while a < b < 10000:
	for i in range (a,b):
		a=100
		b=200

		
>>> 
>>> print (i)
9
>>> while a < b < 10000:
	for i in range (100,200):
		print i

		
>>> 
>>> print range (i)
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> for i in range ( 100,200 )
SyntaxError: invalid syntax
>>> for i in range ( 100,200 ):
	print i

	
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
>>> if i % 2 =1 :
	
SyntaxError: invalid syntax
>>> if r = i % 2 == 1:
	print sum(r)
	
SyntaxError: invalid syntax
>>> 
>>> if i % 2 == 1:
	print i

	
199
>>> 
>>> if i % 2 == 1:
	for i in range (100,200)
	
SyntaxError: invalid syntax
>>> 
>>> if i % 2 == 1:
	for i in range (100,200):
		print i

		
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
>>> if i % 2 == 1:
	for i in range (100,200):
		print sum(i+1)

		

Traceback (most recent call last):
  File "<pyshell#111>", line 3, in <module>
    print sum(i+1)
TypeError: 'int' object is not iterable
>>> for i in range (100,200):
	if i % 2 ==1 :
		print i

		
101
103
105
107
109
111
113
115
117
119
121
123
125
127
129
131
133
135
137
139
141
143
145
147
149
151
153
155
157
159
161
163
165
167
169
171
173
175
177
179
181
183
185
187
189
191
193
195
197
199
>>> for i in range (100,200):
	if i % 2 ==1 :
		print sum (i)

		

Traceback (most recent call last):
  File "<pyshell#120>", line 3, in <module>
    print sum (i)
TypeError: 'int' object is not iterable
>>> print (i)
101
>>> for i in range (100,200):
	if i % 2 ==1 :
		print sum (i)

		

Traceback (most recent call last):
  File "<pyshell#123>", line 3, in <module>
    print sum (i)
TypeError: 'int' object is not iterable
>>> for i in range (100,200):
	if i % 2 ==1 :
		print i

		
101
103
105
107
109
111
113
115
117
119
121
123
125
127
129
131
133
135
137
139
141
143
145
147
149
151
153
155
157
159
161
163
165
167
169
171
173
175
177
179
181
183
185
187
189
191
193
195
197
199
>>> for i in range (100,200):
	if i % 2 ==1 :
		print sum (i)

		

Traceback (most recent call last):
  File "<pyshell#128>", line 3, in <module>
    print sum (i)
TypeError: 'int' object is not iterable
>>> for i in range (100,200):
	if i % 2 ==1 :
		print sum (int(i))

		

Traceback (most recent call last):
  File "<pyshell#130>", line 3, in <module>
    print sum (int(i))
TypeError: 'int' object is not iterable
>>> i = data

Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    i = data
NameError: name 'data' is not defined
>>> for i in range (100,200):
	if i % 2 ==1 :
		i = data
		print i

		

Traceback (most recent call last):
  File "<pyshell#134>", line 3, in <module>
    i = data
NameError: name 'data' is not defined
>>> for i in range (100,200):
	if i % 2 ==1 :
		i = data
		print data

		

Traceback (most recent call last):
  File "<pyshell#137>", line 3, in <module>
    i = data
NameError: name 'data' is not defined
>>> 
