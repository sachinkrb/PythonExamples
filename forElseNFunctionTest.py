Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
==== RESTART: C:/Users/sachi/Documents/GitHub/PythonExamples/primeNum.py ====
2 is a prime number
4 equals 2 * 2
6 equals 2 * 3
8 equals 2 * 4
>>> 
==== RESTART: C:/Users/sachi/Documents/GitHub/PythonExamples/primeNum.py ====
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
>>> 
==== RESTART: C:/Users/sachi/Documents/GitHub/PythonExamples/primeNum.py ====
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
>>> range(2,2)
range(2, 2)
>>> list(range(2,2))
[]
>>> list(range(3,3)
	 )
[]
>>> list(range(2,3))
[2]
>>> for number in range(2,10)
SyntaxError: invalid syntax
>>> for  num in range(2,10):
	for x in range(2,num):
		print(num)
		print(x)

		
3
2
4
2
4
3
5
2
5
3
5
4
6
2
6
3
6
4
6
5
7
2
7
3
7
4
7
5
7
6
8
2
8
3
8
4
8
5
8
6
8
7
9
2
9
3
9
4
9
5
9
6
9
7
9
8
>>> for  num in range(2,10):
	for x in range(2,num):
		print('num=' + num)
		print('x=' + x)

		
Traceback (most recent call last):
  File "<pyshell#12>", line 3, in <module>
    print('num=' + num)
TypeError: can only concatenate str (not "int") to str
>>> for  num in range(2,10):
	for x in range(2,num):
		print('num=' + str(num))
		print('x=' + str(x))

		
num=3
x=2
num=4
x=2
num=4
x=3
num=5
x=2
num=5
x=3
num=5
x=4
num=6
x=2
num=6
x=3
num=6
x=4
num=6
x=5
num=7
x=2
num=7
x=3
num=7
x=4
num=7
x=5
num=7
x=6
num=8
x=2
num=8
x=3
num=8
x=4
num=8
x=5
num=8
x=6
num=8
x=7
num=9
x=2
num=9
x=3
num=9
x=4
num=9
x=5
num=9
x=6
num=9
x=7
num=9
x=8
>>> 
======= RESTART: C:/Users/sachi/Documents/GitHub/PythonExamples/abc.py =======
Traceback (most recent call last):
  File "C:/Users/sachi/Documents/GitHub/PythonExamples/abc.py", line 6, in <module>
    print(num + 'prime')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
======= RESTART: C:/Users/sachi/Documents/GitHub/PythonExamples/abc.py =======
3prime
4not prime
4prime
5prime
5prime
5prime
6not prime
6not prime
6prime
6prime
7prime
7prime
7prime
7prime
7prime
8not prime
8prime
8not prime
8prime
8prime
8prime
9prime
9not prime
9prime
9prime
9prime
9prime
9prime
>>> 
======= RESTART: C:/Users/sachi/Documents/GitHub/PythonExamples/abc.py =======
3prime
4not prime
5prime
5prime
5prime
6not prime
7prime
7prime
7prime
7prime
7prime
8not prime
9prime
9not prime
>>> list(range(2,3))
[2]
>>> 
======= RESTART: C:/Users/sachi/Documents/GitHub/PythonExamples/abc.py =======
2prime
3prime
4not prime
5prime
6not prime
7prime
8not prime
9not prime
>>> 
======= RESTART: C:/Users/sachi/Documents/GitHub/PythonExamples/abc.py =======
2prime
3prime
4not prime
4prime
5prime
6not prime
6not prime
6prime
7prime
8not prime
8not prime
8prime
9not prime
9prime
>>> 
======= RESTART: C:/Users/sachi/Documents/GitHub/PythonExamples/abc.py =======
2prime
3prime
4not prime
5prime
6not prime
7prime
8not prime
9not prime
>>> 
======= RESTART: C:/Users/sachi/Documents/GitHub/PythonExamples/abc.py =======
2prime
3prime
4not prime
5prime
6not prime
7prime
8not prime
9not prime
10not prime
11prime
12not prime
13prime
14not prime
15not prime
16not prime
17prime
18not prime
19prime
>>> 
======= RESTART: C:/Users/sachi/Documents/GitHub/PythonExamples/abc.py =======
2prime
3prime
4not prime
5prime
6not prime
7prime
8not prime
9not prime
10not prime
11prime
12not prime
13prime
14not prime
15not prime
16not prime
17prime
18not prime
19prime
20not prime
21not prime
22not prime
23prime
24not prime
25not prime
26not prime
27not prime
28not prime
29prime
30not prime
31prime
32not prime
33not prime
34not prime
35not prime
36not prime
37prime
38not prime
39not prime
40not prime
41prime
42not prime
43prime
44not prime
45not prime
46not prime
47prime
48not prime
49not prime
>>> def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

    
>>> parrot(1000)
-- This parrot wouldn't voom if you put 1000 volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's a stiff !
>>> parrot(voltage=1000)
-- This parrot wouldn't voom if you put 1000 volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's a stiff !
>>> parrot('a million', 'bereft of life','jump')
-- This parrot wouldn't jump if you put a million volts through it.
-- Lovely plumage, the Norwegian Blue
-- It's bereft of life !
>>> 
