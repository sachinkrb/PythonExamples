from datetime import datetime
odd = [1,  3,  5,  7,  9, 11, 13, 15, 17, 19,
       21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
       41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

at_this_moment = datetime.today().minute

if at_this_moment in odd:
    print("you fell in odd minute.")
else:
    print("you fell in even minute.")
    
