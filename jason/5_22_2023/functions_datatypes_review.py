########################################### FUNCTIONS ############################################################

print("Hello World!")

len([1, 2, 3])
len("sdfnjasq")

some_list = []
some_list.append(1)

range_result = range(10)
print(range_result)


# What is a function?
# Our Guess -- Builtin things in python that will do some operation of code that you don't have to write out again.
# A Function is a Wrapper around some "Block" of code that we want to call without explicitly rewriting the code.

# Let's talk about the internals of a function
# The builtin python len() function finds the length of a list or string that is passed into it!
# But we could also just do that manually with code right?

some_string = "apple"
length_of_the_string = 0
for char in some_string:
    length_of_the_string += 1

print(f"The length of the string: \"{some_string}\"")
print(length_of_the_string)

"""
This block of code is the internals of the len() function
length_of_the_string = 0
for char in some_string:
    length_of_the_string += 1
"""

def my_len(some_string):
    length_of_the_string = 0
    for char in some_string:
        length_of_the_string += 1
    return length_of_the_string


print(my_len("Some String I Pass In"))


# The anatomy of a function
# A Function has the following parts:
# 1.) It has some name and a definition -- `def <some_snake_cased_name>`
# 2.) The argument definition. What variables can be passed to the function -- This is anything in the () on function definition.
# 3.) All function definitions end with a :
# 4.) All functions have some defined Block of code which will execute when the function is invoked/called
# 5.) Functions return some value

# Let's create a function that checks if an integer value is smaller than 10
# first what block of code does this?

some_integer = 11
if some_integer < 10:
    print(f"{some_integer} is smaller than 10")
else:
    print(f"{some_integer} is greater than 10")

def smaller_than_ten__bad_func_do_not_use():
    some_integer = 11
    if some_integer < 10:
        print(f"{some_integer} is smaller than 10")
    else:
        print(f"{some_integer} is greater than 10")

def smaller_than_ten(some_integer):
    if some_integer < 10:
        print(f"{some_integer} is smaller than 10")
    else:
        print(f"{some_integer} is greater than 10")


smaller_than_ten(22)
smaller_than_ten(3)

# Now Functions can have multiple arguments! In fact they can have essential as many as you want!
# These arguments are ordered.
# The names of them are scoped only to the function!

def func_that_prints_four_numbers(number1, number2, number3, number4):
    print(number1)
    print(number2)
    print(number3)
    print(number4)

number4 = 10

func_that_prints_four_numbers(number4, 22, 33, -1120)

# The final part of a function is a return operation

def my_len_again(some_string):
    length_of_the_string = 0
    for char in some_string:
        length_of_the_string += 1
    return length_of_the_string

print("\n")
print(my_len_again("Some String I Pass In"))

length_of_string = my_len_again("Hello")
print(length_of_string)

def add_two_numbers(x, y):
    jason = "Jason"
    return x - y

x = 10
summation = add_two_numbers(15, x)

print(summation)

# Scoping! Now is relevant because of functions.
# Python is a functionally scoped language. This is different than most other languages which are block scoped.

# A block scoped language loses the memory of any variables which were defined in the block of code when it goes up in the block.
# IE when you transition from a tab in one level higher
"""
    var_always_in_scope = 10
    if True:
        var_only_in_scope_in_if = 55
        print(var_always_in_scope + var_only_in_scope_in_if)
    # var_only_in_scope_in_if is now not accessessible.
    
    print(var_always_in_scope)
"""

# Python is kind of functionally scoped. This means that a variables is accessible so long as you are in the same function.
# If a variable of conflicting names is defined within some function and you assign a value to it it will override and knock the other 
# Variable out of scope


print("\n\n\n\n")
x = 10

def some_function():
    # We can access x within the function because it is in the function definition scope
    y = 55
    print(y)
    x = 100
    print(x)

some_function()
print(x)
# print(y) this will error out



############################################ DATATYPES AGAIN! ###############################################

# One of the biggest hurdles with learning python is that it is a dynamically typed language and this can cause you to think of datatypes as magic.


# How does a computer store data?
# Our Guess -- It stores in binary everything is machine code, whether it is an integer, string, list whatever.
# And computers really only have a couple of operations they can do: Write, Read, and Go To


# When a computer gets some number
# 10 <-- The number 2 in binary -- A binary representation of the integer 2
# '2' <-- This is a string of 2 this is like a million times more binary bits to represent this. `0x000000B2` in utf-32

if 2 == '2':
    print("Yes 2 is 2")
else:
    print("Yes 2 is never '2'")

# In a dynamically typed language variables can store any datatypes they really don't care
# But! The computer still does care if you have to do work with it. Meaning if you are doing work across 2 different variabels of two different datatypes you need to make sure they match with each other.
my_var = 2
my_var = "2"

# You can do this via casting.
# Casting is turning one datatype into another datatype

string_variable = "55"
number_variable = 55

print(string_variable + str(number_variable))
print(int(string_variable) + number_variable)
print("\n\n")

############################################ LOOPS AGAIN ############################################

# some_list = [2, 3, "hello"]

# print(some_list)
for num in range(4):
    for _ in range(4):
        for tomtime in range(4):
            print("Tom")

# High level stuff if you are interested in algs
# Big O notation which is a way of defining the "speed" of some algorithms.
# Basically nested loops are defined as O(n^2)
# A single loop is O(n)
# A single execution is O(1)