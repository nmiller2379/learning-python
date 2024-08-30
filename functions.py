# Basic syntax of a function
def my_function():
    print("This is a function.")

# Calling a function
my_function()

# Functions with parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Nate")

# Functions with default parameters
def greet(name="World"):
    print(f"Hello, {name}!")

greet()
greet("Todd")

# Functions with return values
def add(a, b):
    return a + b

result = add(5, 10)
print(result)

# Functions with multiple return values
def add_sub(a, b):
    return (a + b, a - b)

multi_result = add_sub(5, 10)
print(multi_result)
print(multi_result[0])

# Unpacking multiple return values
addition, subtraction = add_sub(5, 10)
print(addition)
print(subtraction)

# Unpacking multiple return values without a tuple
def add_sub(a, b):
    return a + b, a - b

addition, subtraction = add_sub(5, 10)
print(addition)
print(subtraction)

# Functions with keyword arguments
def add_nums(a, b, c):
    print(a, b, c)
    return a + b + c

result = add_nums(b=5, a=10, c=15)
print(result)

# Functions with variable-length arguments 
def add(*args):
    return sum(args)

result = add(1, 2, 3, 4, 5)
print(result)