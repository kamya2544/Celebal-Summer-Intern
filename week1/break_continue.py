# break and continue are loop control statements executed inside a loop

# BREAK STATEMENT
# terminates the loop immediately and transfers execution to the new statement after the loop
count = 0
while count <= 100:
    print (count)
    count += 1
    if count == 3:
        break

# CONTINUE STATEMENT
# causes the loop to skip its current execution at some point and move on to the next iteration
for i in range(0, 5):
    if i == 3:
        continue
    print(i)