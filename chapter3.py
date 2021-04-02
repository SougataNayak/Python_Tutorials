# Strings: sequence of characters enclosed by single, double or triple quotes

name = "abcdefgh"
greet = 'Hello, '

print("Concatenating: ", greet+name)

print(f"Python supports formatted strings as {name} and {greet}are printed here")

print("\nString slicing")
print("Element 1 is:", name[1])
# This works only to access individual elements, but not assign them
# name[2] = "k" (does not work)

print("Element 0 to 3 are:", name[0:3])
print("Element 1 to 5 are:", name[1:5])
'''The basic syntax is 'str[start:end]' 
    Here if start is not defined it is by default 0
    And if end is not defined it is by default the last index'''
print("Elements '3rd to end' are:", name[3:])
print("Elements 'start to 5th' are:", name[:5])

# To fetch the last parts of the string, we use negative indexes
print("\nLast element of the string is:", name[-1])
# In negative indexing, the last element is -1, and the subsequent elements are -2, -3, -4...
print("Fetch range in negative index -4 to -1:", name[-4:-1])
'''To convert negative indexes to positive: 'str[-x:-y] is same as str[len-x:len-y]', len is the length of string'''

print("Slicing with skip value of 2:", name[1:6:2])


print("\nString Functions")
print("Length:", len(name))
print("Check if the string ends with a certain string:", name.endswith("gh"))
print("Count the total number of occurrence of a character:", name.count("a"))
print("Capitalize the first character of the string:", name.capitalize())
print("Find if a certain string is present or not and give its index:", name.find("cd"))
# Find just gives back the index of first occurrence of the substring not all
print("Replace one part of the string with another:", name.replace("cd", "xy"))
# Replace function replaces all the occurrences of the given string with the new string
print("The strip function is used to remove all initial and trailing spaces from a string:", "    Hello   leo".strip())

# IMPORTANT NOTE: Functions like find and replace do not change the original string, they just return a new string


'''Python also has many escape sequences, majorly consisting
    1. \n for new line within a string
    2. \t for tab or multiple spaces within a string
    3. \\ for printing a backslash in the string as by default backslash will be considered as a escape sequence
    4. \' for printing single quote within a string which starts and ends with single quote'''
