# Built with Python 3.7.2
# A simple program to guess odd or even seconds and test execution time.
# Measures total duration for execution, start_time and end_time can be resituated if needed.
# When 'continue' statements are used after ending of if, elif statements.....
# ...Pointer will jump back to while loop immediately, hence total duration time can be shortened
import ctypes  # An included library with Python install.

from datetime import datetime
import sys
import os
import html
print(html.unescape("I &hearts; Python &lt;GuessingGame&gt;")) # Use of escape or unescape
print(os.getcwd()) # Prints current working directory using os standard library and module
print(sys.version)
odd = [1,  3,  5,  7,  9, 11, 13, 15, 17, 19,
       21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
       41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

answer =''

while answer != 'exit':
    at_this_moment = datetime.today().second
    print('Enter your guess - odd/even/exit?')
    answer = input()
    start_time = datetime.today() #Starting time for execution
    
    if at_this_moment in odd and answer == 'odd':
        print('Correct answer, you fell in ODD minute. ' + str(at_this_moment) + ' secondth at this moment.')
        def Mbox(title, text, style):
            return ctypes.windll.user32.MessageBoxW(0, text, title, style)
        Mbox('Your title', 'Your text', 1)
        #continue statement can be used here to jump back to while loop to check the while statement
        
    elif at_this_moment not in odd and answer == 'even':
        print('Correct answer, you fell in EVEN minute. ' + str(at_this_moment) + ' secondth at this moment.')
        #continue statement can be used here to jump back to while loop to check the while statement

    elif at_this_moment not in odd and answer == 'odd':
        print("Wrong, you missed it by a second! Better luck next time")
        print('It was ' + str(at_this_moment))
        #continue statement can be used here to jump back to while loop to check the while statement
        
    elif at_this_moment in odd and answer == 'even':
        print("Wrong, you missed it by a second! Better luck next time")
        print('It was ' + str(at_this_moment))
        #continue statement can be used here to jump back to while loop to check the while statement
        
    elif answer == 'exit':
        print('Bye Bye')
        break       #this will break the execution for while loop
        
    else:
        print('uh oh! Could not comprehend your input but the second hand was in ' + str(at_this_moment) + ' .Please try again')
     
    end_time = datetime.today() #End time for execution
    print('Program Execution ' + 'Duration: {}'.format(end_time - start_time) + " after user's input.") # Calculates duration of execution after receiving input
    print('') 
        
"""
TIP OF THE DAY: If you need to import


# Part of above code that is copied or sourced from a book pasted below

"""

   from datetime import datetime
        odds = [ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19,
                21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
                41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")

        """
    
