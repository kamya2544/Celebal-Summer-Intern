# Module is a file containing a set of functions we want to include in our application

# To create a module we need to save the code we want in a file with file extension .py and then use it using import statement
# def greeting(name):
#   print("Hello, " + name)

import mymodule

mymodule.greeting("Jonathan")

a = mymodule.person1["age"]
print(a)

# RENAMING A MODULE
import mymodule as mx

a = mx.person1["age"]
print(a)



# BUILT-IN MODULES
import platform

x = platform.system()
print(x)


# dir() function
# It is a built-in function to list all the function names (or variable names) in a module.
import platform

x = dir(platform)
print(x)

y = dir(mymodule.person1)
print(y)

z = dir(mymodule)
print(z)


# IMPORT FROM MODULES USING from KEYWORD
from mymodule import person1

print (person1["age"])
