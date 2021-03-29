# Lists and Tuples

# Creating a list using []
a = [1, 2, 3, 4, 5, 6, 7, 8]  # Lists are ordered
print("Lists\nList a is:", a)
print("Individual elements in a list can be accessed using []:", a[1])

a[3] = 10
print("Lists items can also be changed using []:", a)

# List items need not be of the same type, they can be of any data type
b = [1, "Leo", True, 3.14, None]
print("List of different data types:", b)

# Lists can be sliced the same way as strings
print("Sliced list a:", a[1:5])

print("\nList methods")
l1 = [1, 8, 7, 2, 21, 15]
l1.sort()
print("The updated list after sorting is:", l1)
l1.reverse()
print("The updated list after reversing is:", l1)
l1.append(84)
print("List after appending (adding item to the end of list) is:", l1)
l1.insert(1, 90)
print("List after insert (inserting item at a given position and pushing the later elements) is:", l1)
l1.pop(2)
print("List after pop (removing item at a given index) is:", l1)
l1.remove(7)
print("List after remove (removing the given item) is:", l1)
print("To get sum of numeric lists sum method is used:", sum(l1))


print("\nTuples")
tup = (1, 2, 3, 4, 5, 1, 2)
print("Tuple tup is:", tup)
print("Tuples can also be sliced the same way as strings and lists", tup[1:4])

'''tup[1] = 5 WILL NOT WORK
    NOTE: Major difference between list and tuple is that tuple is immutable and can't be changed'''

empty_tuple = ()
# Above is a empty tuple
# For tuple with single element, we can't write 't = (1)', as it will consider it a single number
tuple_with_single_element = (1, )
print("Empty tuple:", empty_tuple, "\nTuple with single element:", tuple_with_single_element)

print("\nTuple methods")
print("Count method tells number of occurrence of a value:", tup.count(1))
print("Index method tells the index of first occurrence of value", tup.index(5))
