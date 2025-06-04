# while loop
i = 1
while i < 6:
  print(i)
  i += 1 #remember to increment i, or else the loop will continue forever.

# break statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break #stop execution at i=3
  i += 1

# continue statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue #skips i=3 and proceeds forward with next iteration
  print(i)

# else statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")