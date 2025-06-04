# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable (change, add or remove items) and do not allow duplicates.
# Dictionaries are ordered from 3.7 onwards and in earlier versions, it was unordered
# Dictionaries are written with curly brackets
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])

# Dictionaries cannot have two items with the same key and if they do, the latest one gets considered
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# To determine how many items a dictionary has, use the len() function
print(len(thisdict))

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(type(thisdict))


# Creation of dictionary using dict() constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)