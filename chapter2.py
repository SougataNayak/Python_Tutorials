# Variables and data types, operators, typecasting and input

# A variable is a name given to a memory location in a program
# Primary data types in python are Integers, Floating point numbers, Strings, Booleans and None.
a = 5
b = 3.14
c = 'Leo'
d = True
e = None

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))

# Types of operators in python are Arithmetic, Assignment, Comparison and Logical operators

print("\nArithmetic operators")
print("3+2 =", 3+2, "\t 3-2 =", 3-2, "\t 3*2 =", 3*2, "\t 3/2 =", 3/2, "\t 3**2 =", 3**2, "\t 3%2 =", 3 % 2)

print("\nAssignment operators")
print("These include '=', '+=', '-=', '*=' '/=' and more")
a = 5   # Assign 5 to a
a += 2   # Add 2 to a
a -= 3   # Subtract 3 to b

print("\nComparison operators")
x = 14
y = 7
print("x==y =", x == y, "\t x>=y =", x >= y, "\t x<=y =", x <= y, "\t x<y =", x < y, "\t x>y =", x > y, "\t x!=y =", x != y)

print("\nLogical operators")
bool1 = True
bool2 = False
print("bool1 and bool2 =", (bool1 and bool2), "\tbool1 or bool2 =", (bool1 or bool2), "\tnot bool2 =", (not bool2))


# Typecasting: The way to converting one data type to another
# typecasting functions try to convert data types, but there is no guarantee as data types might not be compatible
print("\nTypecasting")
s = "123"
print(s, type(s))
s = int(s)       # converts string to int
print(s, type(s))
s = float(s)       # converts int to float
print(s, type(s))

r = 10.5
print("Directly converting float to int omits the float part:", r, "changes to", int(r))


print("\nInput function")  # Used to take inputs
n = input("Enter anything: ")
print("The entered text and its type is:", n, type(n))
# IMPORTANT NOTE: Anything you receive as an input will always be of string class
