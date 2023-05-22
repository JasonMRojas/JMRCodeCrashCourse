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


#input your list
input_list= [1, 2, 3, 4, 5, 6]

empty_bucket=[]

x = len(input_list)

for i in range(0, x):
    print(i)
    empty_bucket.append(input_list[x - 1 - i])



#input_list[3]

#empty_bucket.append(input_list[4])
#
#empty_bucket.append(input_list[3])
#
#empty_bucket.append(input_list[2])
#
#empty_bucket.append(input_list[1])
#
##empty_bucket.append(input_list[0])

print(empty_bucket)
#for i in range(len(user_input)):

    

    #print(user_input[i])






#print(user_input)
