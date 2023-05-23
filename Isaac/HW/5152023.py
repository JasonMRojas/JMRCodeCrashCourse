print("Reverse List Hw")
#Problem
#Write a Python program that takes a list of numbers as input and returns a new list with the same numbers in reverse order. Your program should do the following:
#Ask the user to enter a list of numbers separated by spaces.
#Use the input to create a list of numbers.
#Reverse the order of the numbers in the list.
#Requirements
#Your program should meet the following requirements:
#Use at least one if/else statement to handle an error or edge case.
#Use at least one loop to iterate over the list.
#Use at least one list method to manipulate the list.
#Use at least one string method to convert the input string to a list of numbers
user_input = input("please enter a series of numbers separated by spaces: ")
cleaned_user_input = user_input.strip()
user_input_list = cleaned_user_input.split()

reversed_list = []

length_of_list = len(user_input_list)

for i in range(length_of_list):
    print(i)
    reversed_list.append(user_input_list[length_of_list - 1 - i])

for int in user_input:
    if user_input == ' ':
        print("please enter a series of numbers")

    else:
        continue


print(reversed_list)


