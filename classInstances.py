"""
class Employee:
    pass
emp_1 = Employee()      #Instance of class i.e its an employee object, a sample that belongs to the class
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'romeo'       #romeo, julius, 50000 instance variables
emp_1.last = 'julius'           # first, last, pay are attributes of the object
emp_1.pay =  50000

emp_2.first = 'juliet'
emp_2.last = 'romeus'
emp_2.pay =  60000

print(emp_1.pay)
print(emp_2.pay)

#Benefit of using class and constructor  using __init__(which initializes instance variables)

class Student:
    def __init__(self, first, last, pay):   #Similar to constructor in other language, self is compared to 'this'
        self.first = first                      #Can also be self.fname = first
        self.last = last
        self.pay = pay

    def fullname(self):         # self takes the instance here
        return '{} {}'.format(self.first, self.last)
    
stu_1 =  Student('romeo', 'juliuss', 70000)      #stu_1 is the self here
stu_2 =  Student('juliet', 'romeuss', 80000)

print(stu_1.pay)
print(stu_2.pay)
print(stu_1.fullname())     # Method called here for stu_1 instance of the class Student i.e an object
print(Student.fullname(stu_2)) #Method called here on class itself and stu_2 was passed as instance

"""

class Muggle:
    def __init__(self, age, name, liking_person):
        self.age = age
        self.name = name
        self.likes = liking_person
        
Vermont = Muggle(52, "Vermont", None)
Paris =  Muggle(50, "Paris", Vermont)
Vermont.likes = Paris

print(Vermont.likes)
print(Paris.likes)
print(Vermont.age)
print(Vermont.name)






