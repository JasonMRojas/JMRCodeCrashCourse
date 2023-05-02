# Variables
three_five_string = 3
always_five = 5

print(three_five_string + always_five)

three_five_string = 5

print(three_five_string + always_five)

three_five_string = "I am now this"

variable = "I am a variable"
print(variable)

# Casting
print(str(three_five_string) + str(always_five))


# Strings
# A string is anything in "" or '' or """ (block strings)
# It can contain a very varied amount of data usually alphanumerical information.
# Behind this scenes it is known as an "Array" of Characters

j_char = 'J'
name = "\"John"
print("My name is", name)

# Lists
# This is not exactly/technically true, however, Lists are Arrays
# Anything at all that is stored as data can go in a list. A list is very flexible
fruits = ["apple", "banana", "cherry", "anotherthing", 3, "", ["itemnestedlist", variable]]

# With a list there are really only 5 major ways to work with it.
# You can add to the list programatically.
fruits.append("I Will Be Added to the End of the list")
fruits.append("Oh no! Another item!")
print(fruits)

# I can access the things in the list. This works via something called index accessing.
# That is like counting up the list but starting at 0 --> index notation uses []

print(fruits[0])

# You can ask the list how long it is!

print(len(fruits))

fruits.append(10)
# This will ALWAYS return the end of the list
# Yes in python you can also use list[-1] loser nerd
print(fruits[len(fruits) - 1])

# You can change a value at an index

fruits[0] = "strawberry"

# Next way to do work is to remove from a list. This is less common than you think
# List remove(value)
fruits.remove("cherry")

print(fruits)

# Next way and final / main way to interact with a list is to
# Iterate (loop) through the list which we will get into more details soon!

# Dictionaries
# A dictionary is a datastructure created using KVP (key value pairs) which allow quick reference at a labeled key
person = {"name": "John", "age": 30, "city": "New York"}

# We can access a dictionary similarly to a List using [] at a key label.
# All keys inside of a dictionary are unique! They must be unique! Values are not! They can be repeated or be anything at all!
print(person["name"])
print(person["age"])
print(person["city"])

# Like Lists you can access them at a point! You can also change their value (also like lists)

person["name"] = "Sam"

print(person)

print("\n\n\n\n")

# If Statements
x = 7
if x > 10:
    # You can do as much work in an if statement as you want
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but less than or equal to 10")
else:
    print("x is less than or equal to 5")
print("I am going to run always!!!")

# Else statements are not required
if x > 1:
    print("x is greater than 1")
print("I am also always going to run!")



#################
# Looops
#################

# While loop means do a thing over and over while some condition remains true. Loop keywords like 'break' and 'continue' apply
# In more techincal terms repeat a block of code indefinitely until some condition is false or some control flow keyword is invoked.
count = 1
while True:
    # There is a concept in loops called Control flow.
    # Control flow keywords are 'break' and 'continue'
    if count > 5: 
        break

    print("Count is:", count)
    # If count is an even number
    if count % 2 == 0:
        # Add three instead of 1 and 'continue' the loop to make sure we don't add another += 1
        count += 3
        continue
    print("I did not continue")
    count += 1
print("Done!")



print("\n\n")


# For Loops the ones I use nonstop
# For loop means loop through a range of things until it is empty
# This is most commonly used to "iterate" through a list of items
for i in range(1, 6):
    print(i)

# The final way to interact with a list is to loop through it!
# All the key words that work in a while loop also work in a for loop
for fruit in fruits:
    print(fruit)

idx = 0
while idx < len(fruits):
    print(fruits[idx])
    idx += 1



# User input
# In python you can get user input and assign it to a variable using the `input()` function

user_input = input("Please Type Your Name and I will Print It: ")
# User input blocks the 'thread' (the code's thought process and working stack) until a user input is given in the console.

print(user_input)