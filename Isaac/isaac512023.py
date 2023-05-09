print("Hello World")
name = "Isaac"
print(name)
#string
name = "John"
print("My name is" , name)
#list
print(["apple","banana","Fruit", "3", name, 7])

fruit = ["apple","banana","Fruit", "3",]
print(fruit)

fruit.append("i am at the end")

print(fruit)

print(fruit[3])

person = {"name": "John", "age": "30", "city":"Palm Beach", "age20": "20"}
print(person["name"])
print(person["age"])
print(person["city"])
print(person["age20"])









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

# With a list there are really only 3 major ways to work with it.
# You can add to the list programatically.
fruits.append("I Will Be Added to the End of the list")
print(fruits)

# I can access the things in the list. This works via something called index accessing.
# That is like counting up the list but starting at 0 --> index notation uses []

print(fruits[6])