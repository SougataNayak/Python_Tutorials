# Loops

# While loops iterate as long as it's condition is satisfied
print("While loops")
i = 1
while i <= 10:
    print(i, end=" ")
    i = i + 1


# For loops iterates through a sequence of iterables (list, tuple or string)
print("\n\nFor loops")
ls = [1, 2, "leo", 3.14, False]
for item in ls:
    print(item, end="  ")


print("\nRange function")
'''Range function: used to generate a sequence of numbers -> range(start, stop, step_size)
    if start is not defined, by default it is 0, and the end is always passed'''

for i in range(5):
    print("Range ", i)
else:
    print("This is inside else of for")
# For and while loops can also have an else segment, which is executed after the loop is exhausted


print("\nBreak statement")
for i in range(10):
    print("Break:", i)
    if i == 5:
        break
else:
    print("This else will not be executed")
    '''This will not be executed as it will only be printed after the successful termination of the loop
        and as break statement prevents that, it will not be printed, which would not have been the case
        if we just wrote the line after the loop'''


print("\nContinue statement")
# It skips everything below the continue statement just for that particular iteration
for i in range(5):
    if i == 3:
        continue
    print("Continue:", i)


# PASS statement
'''Pass statement is a null statement in python which means do nothing
    It is used when we have to syntactically define anything but don't wanna write anything inside the body
    If we don't use pass these might throw errors
    pass can be used in if statements, loops and functions'''
for i in range(5):
    pass
