#Python 3.7.2
#docs.pythdon.org
#Demonstration of Lambda expressions

def make_increments(n):
    return lambda x: x + n  
f = make_increments(96) # assigns function to an object

print(f(4)) #passed an argument to the function, adds the value of n to x 
#Result :100
print(f(9)) #make_increment(96) remains the same 
#Result: 105

pairs = [(1, 'nike'), (2, 'addidas'), (3, 'puma'), (4, 'goldstar'), (5, 'xinsau')]
pairs.sort(key = lambda pair:pair[1])# sorts pair values in alphabetical order
print(pairs)

"""
Results:
100
105
[(2, 'addidas'), (4, 'goldstar'), (1, 'nike'), (3, 'puma'), (5, 'xinsau')]

"""
