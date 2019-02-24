##Python 3.7.2
##docs.python.org
##EXAMPLE WHEN for CLAUSE IS USED WITH else CLAUSE.
##Important: The break statement, like in C, breaks out of the innermost enclosing
##for or while loop. Loop statements may have an else clause; it is
##executed when the loop terminates through exhaustion of the list (with
##for) or when the condition becomes false (with while), but not when the
##loop is terminated by a break statement. This is exemplified by the
##following loop, which searches for prime numbers.
##Try indenting else: statement and assign it to 'if' first and with 'for' next.
##When used with a loop, the else clause has more in common with the else clause
##of a try statement than it does that of if statements: a try statement’s
##else clause runs when no exception occurs, and a loop’s else clause
##runs when no break occurs.
##Check the results
##In summary break is used with to break out of for and while loop
##else helps exhaust the list in for clause and execute the statement after else
for num in range(2,10):
    for x in range(2, num):
        if num % x == 0:
            print(num, 'equals', x, '*', num//x)
            break  #breaks the innermost for loop and jumps to outermost for loop
    else:
            #Exits out of loop unable to get factored
            print(num, 'is a prime number')


"""
SHORT CODE:
for num in range(2,10):
    for x in range(2,num):
        if num % x == 0:
            print(str(num)+ 'not prime')
            break 
    else: #else will exhaust the list x above first before jumping down to next line
            print(str(num) + 'prime')
   """         
"""
In python shell >>>list(range(2,2) will result empty list []
Results when else is indented for 'if' statement: Incorrect Result

3 is a prime number
4 equals 2 * 2
5 is a prime number
5 is a prime number
5 is a prime number
6 equals 2 * 3
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
7 is a prime number
8 equals 2 * 4
9 is a prime number
9 equals 3 * 3

"""

"""
Results when else is indented for 'for' statement: Correct Result

2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3

"""
