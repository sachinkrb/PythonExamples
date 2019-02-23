Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> list(range(10,0,2)
	 )
[]
>>> list(range(20,0,-2))
[20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
>>> listNum(range(9,2,-1)
	    )
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    listNum(range(9,2,-1)
NameError: name 'listNum' is not defined
>>> list(range(9,2,-1)
	 )
	    
[9, 8, 7, 6, 5, 4, 3]
>>> words = ['cat', 'dog','mouse']
	    
>>> for w in words:
	    print(w,len(w))

	    
cat 3
dog 3
mouse 5
>>> for w in words[:]:
	    if len(w) > 5:
		    words.insert(0, w)

	    
>>> words
	    
['cat', 'dog', 'mouse']
>>> for w in words[:]:
	    if len(w) > 3:
		    words.insert(0,w)

	    
>>> words
	    
['mouse', 'cat', 'dog', 'mouse']
>>> # Looping over slice copy of the entire list, without the silce included, the iteration will be infinite , will add mouse over and over again.
	    
>>> 
