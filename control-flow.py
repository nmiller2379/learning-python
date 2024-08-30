# If statements are the same in Python as they are in JavaScript, except for the syntax. The syntax for an if statement in Python is:
if True:
    print("This will print.")

# The syntax for an if-else statement in Python is:
if False:
    print("This will not print.")
else:
    print("This will print.")

# The syntax for an elif statement in Python is:
if False:
    print("This will not print.")
elif True:
    print("This will print.")

#Loops in Python

# The syntax for a for loop in Python is:
for i in range(5):
    print(i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# The syntax for a while loop in Python is:
i = 0
while i < 5:
    print(i)
    i+=1

# Using len to access the index of an item in a list
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"Index: {i}, Value: {fruits[i]}")

