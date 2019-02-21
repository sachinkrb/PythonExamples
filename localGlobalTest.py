# Function doesn't execute itself. It has to be called. When called though, if
# there is another function called inside a function, that insider widll also be
# and results will be published.

def spam():
    eggs = 'spam local'
    print(eggs)

def bacon():
    eggs = 'bacon local'
    print(eggs)
    spam()
    print(eggs)

eggs='global'
bacon()
print(eggs)

def spam1():
    global eggs1
    eggs1 = 'spam1'

eggs1 = 'global'
spam1()
print(eggs1)

    
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error')

print(spam(2))
print(spam(0))
print(spam(1))
