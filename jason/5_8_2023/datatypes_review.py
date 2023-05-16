import os


# Back to strings!!!
# "" -> '' -> """""""" anything in quotes basically
# A string is a list of `valid characters` so basically anything on your keyboard

# x = 'asdlnjksdf'
# y = ' 112'
# String Concatenation -- Basically you can append new characters / strings to end of strings!

# z = x + y

# print(z)
# This can be really useful for some string construction magic!

# room_description = "The corridors around you give off an creepy vibe. There is a stench of death in the air and you hear the squeking of rats."
# room_options = """
#     You may go the following directions:
#         1) North
#         2) South
#         3) Give up and Die
# """
# character_display_name = "Isaac the Grey Alien"


# Let's say we are in a game loop
# This is a zork project preview! Your project will be much harder
#while True:
#    # Clear console and display input
#    os.system('cls' if os.name == 'nt' else 'clear')
#    full_room_to_display = character_display_name + "\n" + room_description + "\n" + room_options
#    print(full_room_to_display)
#
#    # Ask for user_input
#    user_input = input("\nSubmit a direction to go: ")
#    clean_user_input = str(user_input.strip()).upper() # WIP
#    if clean_user_input[0] == "N" or clean_user_input[0] == "1":
#        room_description = "You enter a dusty library there is nothing around you"
#    elif clean_user_input[0] == "S" or clean_user_input[0] == "2":
#        room_description = "You leave the castle. There is a howling in the wind."
#    elif clean_user_input[0] == "G" or clean_user_input[0] == "3":
#        print("You give up and die!")
#        break
#    else:
#        print("You gave an invalid direction please try again (Press Enter to try again).")
#        input()
#print("Game Over")


# String can be interacted with in many ways! Another common/useful way is through string interopolation. (Basically putting variables dynamically into a string)

#while True:
#    # Clear console and display input
#    os.system('cls' if os.name == 'nt' else 'clear')
#
#    # String interopolation is a clever and easier way to construct strings
#    # This can be done on any string type you are constructing
#    full_room_to_display = f"""
#    {character_display_name}
#    {room_description}
#    {room_options}
#    """
#    print(full_room_to_display)
#
#    # Ask for user_input
#    user_input = input("\nSubmit a direction to go: ")
#    clean_user_input = str(user_input.strip()).upper() # WIP
#    if clean_user_input[0] == "N" or clean_user_input[0] == "1":
#        room_description = "You enter a dusty library there is nothing around you"
#    elif clean_user_input[0] == "S" or clean_user_input[0] == "2":
#        room_description = "You leave the castle. There is a howling in the wind."
#    elif clean_user_input[0] == "G" or clean_user_input[0] == "3":
#        print("You give up and die!")
#        break
#    else:
#        print("You gave an invalid direction please try again (Press Enter to try again).")
#        input()
#print("Game Over")#


# A couple of extra string functions
# Upper function
# x = 'a'.upper()
# print(x)
# Lower function
# print(x.lower())
# Strip function. This removes all whitespace or instances of whatever character you pass into a string.
# x = '      a      '
# print(x.strip())
# Split takes a string and turns it into a list of strings depending on the character you "split" it on



# Dictionaries part 2 zork boogaloo
#character = {
#    "name": "Isaac the Grey Alien",
#    "level": 99,
#}
#
#rooms = {
#    "corridor": {
#        "description": "The corridors around you give off an creepy vibe. There is a stench of death in the air and you hear the squeking of rats.",
#        "options_string": """
#            You may go the following directions:
#                1) North
#                2) South
#                G) Give up and Die
#        """,
#        "option_select": {
#            "1": "library",
#            "N": "library",
#            "2": "outside",
#            "S": "outside"
#        }
#    },
#    "library": {
#        "description": "You enter a dusty library there is nothing around you",
#        "options_string": """
#            You may go the following directions:
#                1) South
#                2) East
#                G) Give up and Die
#        """,
#        "option_select": {
#            "1": "corridor",
#            "S": "corridor",
#            "2": "pool",
#            "E": "pool"
#        }
#    },
#    "pool": {
#        "description": "You head to pool. There is a nice bath here or something.",
#        "options_string": """
#            You may go the following directions:
#                1) West
#                G) Give up and Die
#        """,
#        "option_select": {
#            "1": "library",
#            "W": "library"
#        }
#    },
#    "outside": {
#        "description": "You are outside of the castle. There is a howling in the wind.",
#        "options_string": """
#            You may go the following directions:
#                1) North
#                G) Give up and Die
#        """,
#        "option_select": {
#            "1": "corridor",
#            "N": "corridor",
#        }
#    }
#}
#
## Current room is always the key of the rooms dictionary that is used in reference to the users current position.
#current_room = "outside"
#
#while True:
#    # Clear console and display input
#    os.system('cls' if os.name == 'nt' else 'clear')
#
#    # String interopolation is a clever and easier way to construct strings
#    # This can be done on any string type you are constructing
#    full_display = f"""
#        {character["name"]}: Level {character["level"]}
#        --------------------------------------------------
#        {rooms[current_room]["description"]}
#        {rooms[current_room]["options_string"]}
#    """
#    print(full_display)
#
#    # Ask for user_input
#    user_input = input("\nSubmit a direction to go: ")
#    clean_user_input = str(user_input.strip()).upper()
#
#    if clean_user_input == '':
#        print("You gave an invalid direction please try again (Press Enter to try again).")
#        input()
#    
#    # The 'in' operator asks if something is inside of a datastructure like a list of dictionary keys
#    if clean_user_input[0] in rooms[current_room]["option_select"]:
#        # The user gave a valid option! Do the room change
#        current_room = rooms[current_room]["option_select"][clean_user_input[0]]
#    elif clean_user_input[0] == "G":
#        print("You give up and die!")
#        break
#    else:
#        print("You gave an invalid direction please try again (Press Enter to try again).")
#        input()
#print("Game Over")


# Lists review part 2 Zork more boogaloo
#character = {
#    "name": "Isaac the Grey Alien",
#    "level": 99,
#    # This is going to be a list of items. An item can have a description. It's a string
#    "inventory": []
#}
#
#default_actions_string = """
#        L) Look for an item!
#        G) Give up and Die
#"""
#
#rooms = {
#    "corridor": {
#        "description": "The corridors around you give off a creepy vibe. There is a stench of death in the air and you hear the squeking of rats.",
#        "options_string": """
#            You may go the following directions:
#                1) North
#                2) South
#        """,
#        "direction_select": {
#            "1": "library",
#            "N": "library",
#            "2": "outside",
#            "S": "outside"
#        },
#        "items": []
#    },
#    "library": {
#        "description": "You enter a dusty library there is nothing around you",
#        "options_string": """
#            You may go the following directions:
#                1) South
#                2) East
#                G) Give up and Die
#        """,
#        "direction_select": {
#            "1": "corridor",
#            "S": "corridor",
#            "2": "pool",
#            "E": "pool"
#        },
#        "items": ["Secret Key", "A Book"]
#    },
#    "pool": {
#        "description": "You head to pool. There is a nice bath here or something.",
#        "options_string": """
#            You may go the following directions:
#                1) West
#                G) Give up and Die
#        """,
#        "direction_select": {
#            "1": "library",
#            "W": "library"
#        },
#        "items": ["A Floatie"]
#    },
#    "outside": {
#        "description": "You are outside of the castle. There is a howling in the wind.",
#        "options_string": """
#            You may go the following directions:
#                1) North
#                G) Give up and Die
#        """,
#        "direction_select": {
#            "1": "corridor",
#            "N": "corridor",
#        },
#        "items": []
#    }
#}
#
## Current room is always the key of the rooms dictionary that is used in reference to the users current position.
#current_room = "outside"
#
#while True:
#    # Clear console and display input
#    os.system('cls' if os.name == 'nt' else 'clear')
#
#    # String interopolation is a clever and easier way to construct strings
#    # This can be done on any string type you are constructing
#    # the ternary operator is if shorthand which lets you do conditional logic on a single line of code
#    # Because inventory is a list we need to do some work before we pass it into our string constructor
#    inventory_string = ""
#    for item in character["inventory"]:
#        inventory_string += f"{item}, "
#    inventory_string = inventory_string.rstrip(", ")
#    full_display = f"""
#        {character["name"]}: Level {character["level"]}
#        {"Inventory is Empty!" if len(character["inventory"]) == 0 else f'Inventory: {inventory_string}'}
#        --------------------------------------------------
#        {rooms[current_room]["description"]}
#        {rooms[current_room]["options_string"]}{default_actions_string}
#    """
#    print(full_display)
#
#    # Ask for user_input
#    user_input = input("\nSubmit a direction to go: ")
#    clean_user_input = str(user_input.strip()).upper()
#
#    if clean_user_input == '':
#        print("You gave an invalid direction please try again (Press Enter to try again).")
#        input()
#    
#    # The 'in' operator asks if something is inside of a datastructure like a list of dictionary keys
#    if clean_user_input[0] in rooms[current_room]["direction_select"]:
#        # The user gave a valid option! Do the room change
#        current_room = rooms[current_room]["direction_select"][clean_user_input[0]]
#    elif clean_user_input[0] == "L":
#        # The player is searching for an item. If they find one add it to their inventory
#        if len(rooms[current_room]["items"]) > 0:
#            print(f"Wow! How lucky! You found a {rooms[current_room]['items'][0]}")
#            # Use the pop method on index 0 to remove the first index and then return it to the invetory
#            item = rooms[current_room]["items"].pop(0)
#            character["inventory"].append(item)
#        else:
#            print("You searched and searched but there was no items to be found.")
#        input("(Press Enter to continue)")
#    elif clean_user_input[0] == "G":
#        print("You give up and die!")
#        break
#    else:
#        print("You gave an invalid direction please try again (Press Enter to try again).")
#        input()
#print("Game Over")
# 
# 
# list1 = [1, 2, 3, 4, 5]
# list2 = ["one", "two", "three"]
# list3 = ["problem", "time", "uhoh", "hi"]
# 
# for i in list1:
#     for x in list2:
#         for y in list3:
#             print(f"{y} -- {x}: {i}")