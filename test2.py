Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for nepal in [2018, 2019, 2020]:
	print(nepal)

	
2018
2019
2020
>>> year = [2018, 2019, 2020, 2021]
>>> for nepal in range(len(year)):
	print(nepal)

	
0
1
2
3
>>> print(nepal)
3
>>> 
>>> print(nepal)
3
>>> 'tamatar' in ['cauli', 'pyaj', 'lasun','tamatar']
True
>>> tarkari = ['cauli', 'pyaj', 'lasun','tamatar']
>>> 'biralo' in tarkari
False
>>> 'biralo' not in tarkari
True
>>> maanxe = ['romas', 'suraj', 'bikku']
>>> fyaure = maanxe[0]
>>> chyaure = maanxw[1]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    chyaure = maanxw[1]
NameError: name 'maanxw' is not defined
>>> chhaure = maanxe[2]
>>> # we can type above code like this
>>> maanxe =['romas', 'suraj', 'bikku']
>>> fyaure, chyaure, chhaure = maanxe
>>> print(fyaure)
romas
>>> #Assignment trick can be used to swap variables
>>> a, b, c = 'raame', 'syamme', 'chyame'
>>> a, b, c = c, a, b
]
>>> print(a, b, c)
chyame raame syamme
>>> name = 'Suraj a Chyaure'
>>> newName = name[0:7]+ 'the' + name[9:16]
>>> newName
'Suraj athehyaure'
>>> newName = name[0:6] + 'the' + name[7:15]
>>> newName
'Suraj the Chyaure'
>>> tuple(['red','blue,'green'])
	   
SyntaxError: invalid syntax
>>> tuple(['red','blue','green'])
	   
('red', 'blue', 'green')
>>> list(('red','blue','green'))
	   
['red', 'blue', 'green']
>>> list('hello')
	   
['h', 'e', 'l', 'l', 'o']
>>> list('hello','goodbye')
	   
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    list('hello','goodbye')
TypeError: list expected at most 1 arguments, got 2
>>> type(('hello',))
	   
<class 'tuple'>
>>> type((hello))
	   
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    type((hello))
NameError: name 'hello' is not defined
>>> type(('hello'))
	   
<class 'str'>
>>> numbers(1,2,3,4)
	   
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    numbers(1,2,3,4)
NameError: name 'numbers' is not defined
>>> numbers[1,2,3,4]
	   
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    numbers[1,2,3,4]
NameError: name 'numbers' is not defined
>>> tuple[1,2,3,4]
	   
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    tuple[1,2,3,4]
TypeError: 'type' object is not subscriptable
>>> numbers([1,2,3,4])
	   
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    numbers([1,2,3,4])
NameError: name 'numbers' is not defined
>>> #Use tuple or lost to convert
	   
>>> tuple((1,2,3,4))
	   
(1, 2, 3, 4)
>>> list([1,2,3,4)]
	   
SyntaxError: invalid syntax
>>> list([1,2,3,4])
	   
[1, 2, 3, 4]
>>> list((1,2,3,4))
	   
[1, 2, 3, 4]
>>> tuple['hello']
	   
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    tuple['hello']
TypeError: 'type' object is not subscriptable
>>> spam = [0,1,2,3,4,5]
	   
>>> cheese = spam
	   
>>> cheese[1] = 'no num'
	   
>>> spam
	   
[0, 'no num', 2, 3, 4, 5]
>>> cheese
	   
[0, 'no num', 2, 3, 4, 5]
>>> # A reference was assigned to spam but its pointing to the same list. Cheese has the same reference as spam but pointing to the same list. When values for list/array changes the reference is gonna be the same so pointing to the same changed list or array.
