# Conditional statements

# If else and elif statements
age = int(input("Enter your age: "))
gender = "F"

'''In the problem, people 24 to 60 are working
    Males between 18 and 23 are studying
    Males between 13 to 17 and females between 13 to 23, plus all people above 60 get support
    Below 13 get child support'''

if 24 <= age <= 60:
    print("Working")
elif 18 <= age <= 23 and gender == "M":
    print("Studying")
elif age >= 13 or gender == "F":
    print("Support")
else:
    print("Child support")
# Apart from and and or, we can also use not operator as 'if not condition:'
'''The if else elif ladder just executes one statement from the whole ladder
    Once a condition is satisfied in the ladder, the remaining conditions are not checked'''


print("\nis and in")
# in and is keywords
a = 5
b = a
c = 5
if b is a:
    print("b is a")
if c is a:
    print("c is a")

lis = [1, 2, 3, 4, 5]
if 3 in lis:
    print("3 is present in the list")

comment = "Buy from our site, we have a great deal"
if "buy" in comment.lower():
    print("Spam comment")
else:
    print("Not spam")
