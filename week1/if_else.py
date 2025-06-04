#if
a = 33
b = 200
if b > a:
  print("b is greater than a")

#if...elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#if...elif...else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#if...else
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")



### TERNARY OPERATORS OR CONDITIONAL EXPRESSIONS

#Shorthand if
if a > b: print("a is greater than b")

#Shorthand if...else
a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# and Keyword
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# or Keyword
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

# not Keyword
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# Nested if
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# pass Statement
a = 33
b = 200
if b > a:
  pass