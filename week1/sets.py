# Sets are used to store multiple items in a single variable.

thisset = {"apple", "banana", "cherry"}
print(thisset)

# Sets are written with curly brackets.
# A set is a collection which is unordered, unchangeable (can't change but add or remove items), and unindexed and don't allow duplicate values.

# Sets cannot have two items with the same value but if it does then latest one is considered.
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#The values True and 1 are considered the same value in sets, and are treated as duplicates
# True gets printed, 1 doesn't
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
# The values False and 0 are considered the same value in sets, and are treated as duplicates
# 0 gets printed, 0 doesn't
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# To determine how many items a set has, use the len() function
thisset = {"apple", "banana", "cherry"}
print(len(thisset))


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
set4 = {"abc", 34, True, 40, "male"}
print(type(set1))
print(type(set2))
print(type(set3))
print(type(set4))


# Creation of set using set() constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)