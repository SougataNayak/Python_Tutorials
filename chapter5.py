# Dictionary and Sets
myDict = {
    "key": "value",
    "name": "sougata",
    5: "numeric key",
    False: "boolean key",
    "age": 21,
    "marks": [95, 86, 90],
    "nestedDict": {
        "nickName": "leo",
        "single": False
    }
}
print("Dictionary\n", myDict)
'''PROPERTIES OF DICTIONARY
    1. Unordered
    2. Mutable (Can be changed)
    3. Indexed (Can fetch items in log(n) time)
    4. Cannot contain duplicate keys (if one key is defined more than once, it is overwritten)'''

print("Getting values by keys")
print("Value corresponding to key name is:", myDict["name"])
print("Value corresponding to key 5 is:", myDict[5])
print("Value corresponding to key False is:", myDict[False])
print("Value corresponding to key marks is:", myDict["marks"])
print("Value corresponding to key nestedDict is:", myDict["nestedDict"])

myDict["age"] = 22
print("After changing value of key age:", myDict["age"])

print("\nDictionary methods")
print("Keys methods gets the list of keys:", myDict.keys())
print("Values methods gets the list of values:", myDict.values())
print("Items methods gets the list of (keys, value) tuples:", myDict.items())
print("Keys methods gets the list of keys:", myDict.keys())
updatedDict = {
    "college": "KIIT",
    "branch": "CSE"
}
myDict.update(updatedDict)   # It overwrites if any old key is updated
print("Update method updates the dictionary with the new dictionary:", myDict)
print("Get method gets the value for a key:", myDict.get("name"))

'''NOTE
The difference between [] and .get() method is that if the key passed is not present the [] raise an error
whereas the .get() method does not'''
print("For key not present in the dictionary:", myDict.get("KeyNotPresent"))
# But myDict["KeyNotPresent"] gives an exception


# Sets: Collection of non-repetitive elements
print("\nSets")
st = {1, 2, 3, 4, 5, 2, 1}
print(st)  # Does not print 2, 1 from the last
'''PROPERTIES OF SETS
    1. Unordered
    2. Un-indexed
    3. As they are unordered, there is no way to change items in set
    4. Cannot contain duplicate values'''

# Empty set cannon be created using empty_set = {}, this will create empty dictionary
empty_set = set()  # This creates an empty set
print(type(empty_set))

print("\nSet methods")
mySet = empty_set.copy()
'''IMPORTANT NOTE: 
    Writing mySet = empty_set will just make mySet create a reference to emptySet 
    (changes to empty_set will be reflected to mySet)
    Whereas the .copy() method creates a different copy for mySet
    (It is still a shallow copy but not the direct reference)'''

mySet.add(4)
mySet.add(4)
mySet.add(5)
mySet.add((1, 2, 3))
print("Adding values to a set:", mySet)
# Lists and dictionaries cannot be added to sets as they are un-hashable, but tuples can be added

print("Length of a set is given by len method:", len(mySet))
mySet.remove(4)
print("Remove method removes from the set:", mySet)

print("pop methods returns an arbitrary element from the the set and removes it:", mySet.pop())
print(mySet)

mySet.clear()
print("Clear method empties the whole set:", mySet)

# Union and Intersection
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))

# Items of different data types
ss = {20, 20.0, "20"}
print("\nSame data type set:", ss)
'''NOTE: Here 20 and 20.0, though different data types, have the same value, so they are not repeated'''
