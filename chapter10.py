# Object Oriented Programming

"""Class is the blueprint of how object will be created
    Object is the real life entity for the given class"""

'''There are 2 types of attributes associated to python classes
    1. class attributes
    2. instance attributes'''


class Employee:
    company = "Google"

    def __init__(self, name):
        print("\nConstructor run -> Employee created\n")
        self.name = name

    def getSalary(self, signature):
        print(f"\nSalary is ${self.salary} for leo working at company {self.company}, not in {Employee.company}"
              f"\n{signature}")
        # Here self.salary is not defined yet so there might be a runtime error if not defined later
        # In any function, 'self' can be changed to any other valid identifier and will work fine, bu writing self is
        # a best practice

    @staticmethod
    def greet():
        print("Good morning from leo")
    # Here self is not required as @staticmethod makes this method static, hence not related to an object but the class
    # @staticmethod is a decorator which modifies a function


leo = Employee("leo")
leo.company = "Facebook"
leo.salary = 5000

print("Name is: ", leo.name)
print("Company is: ", leo.company)  # This is an instance attribute as it has preference over class attribute
print("Salary is: ", leo.salary)  # This is an instance attribute
print("Employee company is: ", Employee.company)  # This is a class attribute
'''Whenever object.attribute is called, the attribute is searched as an instance attribute, if it is not present
    then it is searched as a class attribute. Instance attribute takes preference over class attribute during 
    assignment and retrieval'''


# 'self' parameter
'''self refers to the instance of the class which is automatically passed with a function call from an object

    Internally, leo.getSalary() is converted to Employee.getSalary(leo)
    Hence the self parameter is always passed and it will receive the object through which it is called'''

leo.getSalary("Cheers!")
leo.greet()


# Constructor (__init__())

'''__init__() is the first method which runs as soon as an object is created.
    It takes self as an argument and can also take other arguments'''
