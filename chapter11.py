# Inheritance
"""Inheritance is the way of creating a new class from an existing class
    The derived class will have all the attributes of the base class and also its own or the once it has overridden"""


class Employee:
    company = "Google"

    def showDetails(self):
        print(f"This is a employee")

    def getCompany(self):
        print(f"The company is {self.company}")


class Programmer(Employee):
    language = "Python"

    def getLanguage(self):
        print(f"Language is {self.language}")

    def showDetails(self):
        print(f"This is a {self.company} programmer")
        # This is method overriding, as this showDetails method will override the one from Employee class


e = Employee()
p = Programmer()

e.showDetails()
p.showDetails()   # Overridden method will run
p.getCompany()    # Even though Programmer does not have a getCompany method, it gets to use the one from Employee
p.getLanguage()


# Types of inheritance in Python
'''Python has 3 types of inheritance:
    1. Single: When child class derives from only one parent class 
    2. Multiple: When child class derives from more than one parent class
    3. Multilevel: When a child class becomes a parent for another class'''



# SINGLE INHERITANCE
class A:
    name = "Leo"

class B(A):
    name = "Sougata"



# MULTIPLE INHERITANCE
class C1:
    college = "KIIT"

class C2:
    college = "Harvard"

class S(C1, C2):  # Arguments of classes given are in decreasing order of priority
    name = "Ron"


s = S()
print(f"\nCollege name is {s.college}")
'''Here college name is printing kiit as the when declaring class S, C1 was given as first argument, hence will
    have more priority. This is how python resolves the multiple inheritance ambiguity'''



# MULTILEVEL INHERITANCE
class GrandFather:
    generation = 1
    def __init__(self):
        print("Initializing grandfather")

    def showGeneration(self):
        print(f"Generation of grand father is {self.generation}")


class Father(GrandFather):
    generation = 2
    fg = 5
    def __init__(self):
        super().__init__()
        print("Initializing father")

    def showGeneration(self):
        super().showGeneration()
        print(f"Generation of father is {self.generation}")

class Son(Father):
    generation = 3
    def __init__(self):
        super().__init__()
        print("Initializing son")

    def showGeneration(self):
        print("\n---------Inside Son class---------")
        super().showGeneration()
        print(f"Generation of Son is {self.generation}")

        # But here in every case the generation will show 3, as self will be of the Son class


'''Here when we fetch attributes, the checking starts from the class of which the object is given
    But if the attribute is not found, then it moves higher and higher to find the attribute
    Same is with functions'''

print("\nCreating object for GrandFather class")
g = GrandFather()  # This will call just it's own constructor

print("\nCreating object for Father class")
f = Father()       # This will call it's own and GrandFather's constructor

print("\nCreating object for Son class")
s = Son()          # This will call it's own plus Father's and GrandFather's constructor


'''super method: Used to access the methods of super class from the derived class
    It goes on to call it's super classes as the functions have super classes'''
s.showGeneration()


# Class method
'''Class methods are the methods bound to the class, and their main objective is to manipulate class attributes
    It is done by the @classmethod decorator'''

class College:
    name = "KIIT"

    def changeCollege(self, newCollege):
        self.name = newCollege
        '''But here if we use this function to change the college name, it will not actually change the class attribute
        Rather it will create a new instance attribute called name 
        To change this, we use class methods, which takes the class as attribute as cls'''

    @classmethod
    def modifyCollege(cls, newName):
        cls.name = newName


clg = College()
clg.changeCollege("Harvard")
print("\nWhen changeCollege() was called: ", College.name)
clg.modifyCollege("Harvard")
print("When modifyCollege() was called: ", College.name)



# Property decorators
'''1. Property (Getter): Using the property decorator, we can use any function in a class as a property
                When we don't want to use a hardcoded property, we can use this and return the value we want to keep
    2. Setter : To set a property made by getter'''

class Salary:
    base = 100
    bonus = 10
    # total = base + bonus
    # Here we cannot make a property for total, as later even if we change
    # any of the properties it's value will not change. This is also called a getter method

    @property
    def total(self):
        return self.base + self.bonus

    # Now if we want to set change the value of total, we use setter method

    @total.setter
    def total(self, val):
        self.bonus = val - self.base


sal = Salary()
sal.bonus = 20
print(f"\nThe total salary is {sal.total}")
sal.total = 150
print(f"Base: {sal.base} \tBonus: {sal.bonus} \tTotal: {sal.total}\n")


# Operator Overloading
'''In python operators can be overloaded using dunder/magic methods
    Dunder methods are the ones which start and end with __
    Apart from __add__ and __mul__ there are many other methods which can be used for different uses
    __str__  It is used if we directly print the object and want to see its details. Ex: print(objectName)
    __len__ It is used to print the length of the object. Ex: print(len(objectName))'''

class Number:
    def __init__(self, n):
        self.num = n

    def __add__(self, other):
        print("Inside add")
        return self.num + other.num

    def __mul__(self, other):
        print("Inside multiply")
        return self.num * other.num

    def __str__(self):
        return f"The number is {self.num}"


n1 = Number(4)
n2 = Number(6)
print("n1 + n2 = ", n1 + n2)
print("n1 * n2 = ", n1 * n2)
print(n1)
