# Functions and recursion

def greet(name):
    print(f'Good day, {name}')


greet('leo')


def getPercentage(marks):
    return sum(marks) / 4


marks1 = [87, 90, 68, 76]
print(f'Percentage for marks 1 is: {getPercentage(marks1)}%')

marks2 = [44, 80, 69, 72]
print(f'Percentage for marks 2 is: {getPercentage(marks2)}%')

'''Python has 2 types of functions
    1. built-in functions (Functions like len(), range(), print(), etc)
    2. user-defined functions'''


# Default argument
def printName(name='Stranger'):
    print(f'Default argument: {name}')


printName('Sougata')
printName()

print('\nRecursion')


def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)


'''Every recursive function has some base condition which is used to stop the recursion eventually without the base
    condition the recursion will never stop, the rest of the code includes calling of the function again'''
n = 0
print(f'The factorial of {n} is {factorial(n)}')
