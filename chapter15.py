# Lambda functions
"""These are the functions created by the lambda keyword. They are used for functions which has only one line or
    can be brought down to one line (one return statement).

    SYNTAX: lambda arguments: expression"""

square = lambda x: x * x  # This is a lambda function to square
sum3 = lambda a, b, c: a + b + c  # Lambda function with multiple arguments

print(f"Square of 5 is: {square(5)}")


# Join method (strings): Creates a string from iterable objects with given joining elements between items
l = ["macbook", "iphone", "ipad", "apple watch", "airpods"]

sentence = " and ".join(l)  # This takes the list l and puts " and " between items and return a string
print(f"Sentence is: {sentence}")


# Format method: used before f strings were created
name = "Sougata"
college = "KIIT"

s1 = f"{name} studies in {college} college"  # Using f strings
s2 = "{} studies in {} college".format(name, college)  # Using format method
s3 = "{1} studies in {0} college".format(name, college)  # Format method with specified indices

print(f"{s1}\n{s2}\n{s3}")


# Map, filler and reduce
'''1. Map applies the passed function to all the items in a given list, returns a map object which needs to be 
      typecasted to a list
   2. The filter function applies the function passed to it to the items of the list, and filters the list based
       on the given condition
   3. Reduce applies a rolling computation to a sequential pair of elements'''


l1 = [1, 2, 3, 4, 5]
print("The list returned by map function is: ", list(map(square, l1)))
# Using the lambda function map to square all the elements, normal functions will work too


greaterThanThree = lambda x: x > 3
print("The list returned by filter function is: ", list(filter(greaterThanThree, l1)))


from functools import reduce

sum2 = lambda a, b: a + b
print("The list returned by reduce function is: ", reduce(sum2, l1))
# It essentially takes the first two elements and passes it to the sum2 func, then passes their sum again with the 3rd
# element and so on, thus getting the sum of the list. Useful when finding the max or min in a list
# To find max in a list
print("Max in the list is: ", reduce(max, l1))
