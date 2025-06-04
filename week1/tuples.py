mytuple = ("apple", "banana", "cherry")
print(mytuple)

#Tuples are used to store multiple items in a single variable.
#Tuple items are ordered, unchangeable (can't add, remove or change items), and allow duplicate values. Tuple items are indexed, the first item has index [0]
#Tuples are written with round brackets

#To determine how many items a tuple has, use the len() function
print(len(mytuple))

#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))
print(type(tuple4))


#Creation of tuple using tuple() constructor
thistuple = tuple(("apple", "banana", "cherry")) #double round-brackets are needed
print(thistuple)