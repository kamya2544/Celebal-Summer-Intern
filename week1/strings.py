# Strings in python are surrounded by either single quotation marks, or double quotation marks.

print("Hello")
print('Hello')

#You can use quotes inside a string, as long as they don't match the quotes surrounding the string
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Assigning string to a variable
a = "Hello"
print(a)

# Multi-line Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# OR
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


# Strings as ARRAYS
# Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string
a = "Hello, World!"
print(a[1])


# Looping in string
for x in "banana":
  print(x) #prints each character in a different line



# The len() function returns the length of a string
a = "Hello, World!"
print(len(a))

# String Membership
# We can use in keyword to check if a certain phrase or character appears in the string
# returns True or False
txt = "The best things in life are free!"
print(" " in txt)
print("free" in txt)
print("!" in txt)
print(" ! " in txt)
print("free!" in txt)
print("s" in txt)


txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# not in keyword
txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")