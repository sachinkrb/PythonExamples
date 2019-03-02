Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tel = {'apple': 123, 'ball':456, 'cat':789}
>>> tel['dog'] = 234
>>> tel
{'apple': 123, 'ball': 456, 'cat': 789, 'dog': 234}
>>> del tel['ball']
>>> tel
{'apple': 123, 'cat': 789, 'dog': 234}
>>> tel['egg'] = 896
>>> tel
{'apple': 123, 'cat': 789, 'dog': 234, 'egg': 896}
>>> list(tel)
['apple', 'cat', 'dog', 'egg']
>>> sorted(tel)
['apple', 'cat', 'dog', 'egg']
>>> 'apple' in tel
True
>>> dict([('abc', 123),('cde', 456)])
{'abc': 123, 'cde': 456}
>>> for k, v in tel.items():
	print(k, v)

	
apple 123
cat 789
dog 234
egg 896
>>> question = ['name', 'address', 'job']
>>> answers = ['dave','austin,tx', 'pythoning']
>>> for q,a in zip(question, answers)
SyntaxError: invalid syntax
>>> for q, a in zip(question, answers):
	print('what is your {0}? It is {1}.'.format(q,a))

	
what is your name? It is dave.
what is your address? It is austin,tx.
what is your job? It is pythoning.
>>> 
>>> q
'job'
>>> a
'pythoning'
>>> basket =['apple', 'ball', 'cat', 'dog']
>>> for f in sorted(basket):
	print(f)

	
apple
ball
cat
dog
>>> basket2 = ['finance', 'hr', 'ceo', 'dev']
>>> for f in sorted(basket2):
	print(f)

	
ceo
dev
finance
hr
>>> # can also be used set as sorted(set(basket2)) to avoid duplicates
>>> 

>>> s1, s2 , s3, s4 = 'abc', 'def', 'ghi', 'jkl'
>>> ans = s1 or s2 or s3 or s4
>>> ans
'abc'
>>> ans1 = s1 and s2 and s3 and s4
>>> ans1
'jkl'
>>> ans2 = s1 not s2 not s3 not s4
SyntaxError: invalid syntax
>>> s5 = 'mno'
>>> ans3 = s1 and s2 and s3 and s4 and s5
>>> ans3
'mno'
>>> s6 =''
>>> ans4 = s1 and s6 and s3
>>> ans4
''
>>> #when a module is imported, the interpreter searches for built-in modile, if not found, searches for module.py
>>> #in directories given under sys.path variable
>>> import sys
>>> sys.ps1
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    sys.ps1
AttributeError: module 'sys' has no attribute 'ps1'
>>> sys.ps2
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    sys.ps2
AttributeError: module 'sys' has no attribute 'ps2'
>>> 
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> import sys
>>> dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_git', '_home', '_xoptions', 'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_coroutine_wrapper', 'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_coroutine_wrapper', 'setcheckinterval', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'version', 'version_info', 'warnoptions', 'winver']
>>> import builtins
>>> dir(builtins)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> software = {}
>>> software['pinger'] = 100
>>> software
{'pinger': 100}
>>> software[100]
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    software[100]
KeyError: 100
>>> software['pinger'}
SyntaxError: invalid syntax
>>> software['pinger']
100
>>> for key in software.keys()
SyntaxError: invalid syntax
>>> for key in software.keys():
	print(key)

	
pinger
>>> for value in software.values():
	print(value)

	
100
>>> for key_value in software.items():
	print(key_value)

	
('pinger', 100)
>>> my_file = open('testfile.txt', 'wt')
>>> my_file.write('This is a test file\n')
20
>>> my_file.write('How to read,write,delete and open files
		  
SyntaxError: EOL while scanning string literal
>>> my_file.write('How to read, write,delete and open files')
		  
40
>>> my_file.close()
		  
>>> my_file2.read()
		  
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    my_file2.read()
NameError: name 'my_file2' is not defined
>>> my_file
		  
<_io.TextIOWrapper name='testfile.txt' mode='wt' encoding='cp1252'>
>>> my_file =open('testfile.txt','rt')
		  
>>> contents = my_file.read()
		  
>>> print(contents)
		  
This is a test file
How to read, write,delete and open files
>>> my_file.close()
		  
>>> my_file = open('testfile','rt')
		  
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    my_file = open('testfile','rt')
FileNotFoundError: [Errno 2] No such file or directory: 'testfile'
>>> my_file= open('testfile.txt','rt')
		  
>>> for line in my_file:
		  print('line is: ', line)

		  
line is:  This is a test file

line is:  How to read, write,delete and open files
>>> 
