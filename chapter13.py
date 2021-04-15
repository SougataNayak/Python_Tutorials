# Miscellaneous in Python

"""if __name__ == '__main__' in Python
    The __name__ evaluates the name of the module where the program is being executed
    If it is directly being executed by itself, it is set to '__main__'
    This comes handy when checking if the module is being run directly or imported in another file"""

'''So if we directly import the file and start using it, it will run it's code as well, to stop that we put a entry 
point to the program and now even if the file is imported, it will not start executing and then only the functions 
called will be executed. import basically picks up all the content of the file and puts it in its place.

********** This is the content of the main.py file ********************

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')'''

import main
main.print_hi("Sougata")


# Global keyword

a = 8
def printNum():
    global a
    a = a+1
    # Here this can be done because of the global keyword, which says that here we must use the global
    # variable rather than creating a new local variable
    print(a)

printNum()


# Enumerate function: It adds counter to an iterable and returns it

list1 = [1, 54, 3.14, False, "leo"]

for index, item in enumerate(list1):
    print(f"{index}:{item}", end=", ")


# List comprehension: It is the way to create sublist of lists based on a certain condition

list2 = [3, 52, 66, 9, 41, 65, 90, 123, 88, 46, 55]

# Creating a list which has only the even numbers of list2
sub = [i for i in list2 if i % 2 == 0]

print("\nEven numbers of the list: ", sub)


# Set comprehension: It is a way to remove repeated items from a list by converting them to sets
list3 = [1, 2, 3, 2, 7, 5, 3, 4, 5]
subset = {i for i in list3}
print(subset)

















