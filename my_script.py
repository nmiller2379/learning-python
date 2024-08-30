# print("Hello, World!")

# Declaring variables in python
name = "Nate" # string
last_name = 'Miller' # also a string
age = 25 # integer
gpa = 3.5 # float
is_ture = True # boolean

# Printing variables
# print(name)
# print(last_name)
# print(age)
# print(gpa)
# print(is_ture)

# Concatenating strings
full_name = name + " " + last_name
# print(full_name)

my_list = [1, 2, 3, 4, 5]
# print(my_list)

# Accessing elements in a list
# print(my_list[0]) # 1

my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple)

# Accessing elements in a tuple
# print(my_tuple[0]) # 1

my_dict = {
    "name": "Nate",
    "age": 25,
    "gpa": 3.5
}

# Accessing elements in a dictionary
# print(my_dict["name"]) # Nate

# Adding elements to a dictionary
my_dict["is_true"] = True

# print(my_dict, "updated dictionary")

my_range = range(10)
# print(my_range)

# print(my_range[4])

my_set = {1, 2, 3, 4, 5}
#print(my_set)

# Accessing elements in a set
# print(my_set[0]) # TypeError: 'set' object is not subscriptable. Can't really be accessed like a list or tuple because it's unordered. We can iterate throug the set to access the elements. Or we can use the in keyword to check if an element is in the set.

# Using a set to remove duplicates from a list
my_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
my_set = set(my_list)
unique_list = list(my_set)
# print(unique_list) # Items in the unique_list won't necessarily be in the same order as the original list. Sets are unordered.

# Using the in keyword
# print(1 in my_set) # True

# Using the not in keyword
# print(1 not in my_set) # False

# In Python everything is an object. We can use the type() function to check the type of an object. Classes are also objects in Python. They are instances of the class type. When we create a class, we're effectively creating a new type. We can use the type() function to check the type of a class. We can also use the isinstance() function to check if an object is an instance of a class.

#print(type(my_list)) # <class 'list'>
#print(type(my_dict)) # <class 'dict'>
#print(type(my_set)) # <class 'set'>
#print(type(my_range)) # <class 'range'>
#print(type(my_tuple)) # <class 'tuple'>

# Creating a class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating an instance of a class
rex = Dog("Rex", 2)
# print(rex.name) # Rex
# print(rex.age) # 2
# rex.bark() # Rex says Woof!

# Scope in Python
# Variables declared inside a function are local variables. They can only be accessed inside the function. Variables declared outside a function are global variables. They can be accessed anywhere in the script. If a local variable has the same name as a global variable, the local variable will take precedence. The global variable will be shadowed by the local variable. We can use the global keyword to access a global variable inside a function. We can use the nonlocal keyword to access a variable from an outer function inside an inner function.

# Global variable
x = 10

def my_function():
    # Local variable
    x = 5
    print(x) # 5

# my_function()
# print(x) # 10

# Using the global keyword
def my_function():
    global x
    x = 5
    print(x)

# my_function()

def outer_function():
    x = "I'm in the outer function."
    def inner_function():
        x = "I'm in the inner function."
        print(x)
    inner_function()
    print(x)

outer_function()