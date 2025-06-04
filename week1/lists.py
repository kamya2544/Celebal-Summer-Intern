# Lists are used to store multiple items in a single variable.

# 4 built-in data types in Python are: Lists, Tuples, Set and Dictionary

thislist = ["apple", "banana", "cherry"]
print(thislist)

# List items are ordered, changeable (add or remove items), and allow duplicate values. The order can't be changed i.e. new items are added to end of list.
# List items are indexed, the first item has index [0]

# To determine how many items a list has, use the len() function
print(len(thislist))

#List items can be of any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(type(list1))
print(type(list2))
print(type(list3))
print(type(list4))

# Creationn of list using list() constructor
thislist = list(("apple", "banana", "cherry")) #double round brackets are needed here
print(thislist)