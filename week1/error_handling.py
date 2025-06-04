# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# try block
try:
  print(x)
except:
  print("An exception occurred")

# NameError special block
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# else keyword
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# finally block
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# Try to open and write to a file that is not writable
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

# To throw (or raise) an exception, use the raise keyword
# x = -1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

# Raise a TypeError if x is not an integer
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")