#Python 3.7.2
#docs.python.org
#Demonstrating how functions,return,and simultaneous calculation operate using Fibonacci series

def fibi(n): #upto certain number
    """ Here goes docstring....what this function is about which is optional """
    a, b = 0, 1  #similar to a = 0, b =1 but have other simulataneous calcualtion usage sometimes
    while a < n:
        print(a, end=' ') #here end prints on the same line followed by space for each print
        a, b = b, a+b # lets u do calculations simultaneously i.e temp = a, a= b, b += temp
    print() # Ends the line and starts another line after 'while' is exhausted
#Use of return statement on same function

def fibi2(n):
    result =[] # empty list created to collect returned values
    a, b =0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

#call the function below

fibi(100)
print(fibi2(100)) # Only results are returned and stored on the list, use 'print' to print it




"""
Notes:
a,b = b,a+b IS NOT same as a=b and b = a+b, one is simulatenous calculation other is not
if fib(0) then return value will be 'None'. In shell prompt, do print(fib(0)) 
Even though without return clause, it is still a function not a procedure only.
n is a parameter, value that will pass or given is an argument.
Results:

0 1 1 2 3 5 8 13 21 34 55 89 
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
"""




