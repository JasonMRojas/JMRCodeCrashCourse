print("hw")

user_input = input("Make a list of items separated by spaces: ").split()
user_output = {}

for word in user_input:
    if len(word) == 0:
        print("nothing there nerd")
        continue
    user_output[word] = len(word)

print(user_output)
    

