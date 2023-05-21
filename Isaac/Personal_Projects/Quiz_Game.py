print("Hello! My name is Hodge Podge!")

start = input("Would you like to play a game? Yes or No: ")

if start.lower() != "yes":
    quit() 

print("Okay lets play!!!")
score = 0 

#question 1
question = input("Is magic missile a spell? ")
if question == "yes":
    print("Correct")
    score += 1 
else:
    print("Incorrect")

#question 2
question = input("How do you spell aarakocra? ")
if question == "aarakocra":
    print("Correct")
    score += 1 
    
else:
    print("Incorrect")

#question 3
question = input("Three houses occupy a lonely village in the wilderness. One house is red, one is yellow, and the other blue. The houses are occupied by three beings: a dwarf, an orc, and a human. One of those three owns the sharpest axe in the land. Another, the most balanced sword in the land. And another, the heaviest hammer in the land. Using the following clues, please tell me: the colour of each house from left to right, the occupants of each house, and the weapons of each person. Clues: the dwarf and orc hate each other and refuse to be neighbors, the human lives in a blue house, the orc does not use swords, the yellow house contains the hammer, the human lives to the left of the dwarf, the red house is on the far left. Answer question in or der of House,Occupatants,weapon, represented by H,O,W...(example: H: red,yellow, green.O:dwarf,orc,human. W: sword,hammer,axe) ")
if question == "H: red, blue, yellow. O: orc, human, dwarf. W: axe, sword, hammer":
    print("Correct")
    score += 1
else:
    print("Incorrect")

#question 4
question = input("Who was the inventor of math? ")
if question == "doug math":
    print("Correct")
    score += 1
else:
    print("Incorrect")

#question 5
question = input("Did you have fun? ")
if question == "yes":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print("You got " + str((score / 5) * 100) + "%." )
print("You got " + str(score) + " questions correct!!!" )

if score == 5:
    print("You are a genius")
else:
    print("You are NOT a genius! Try again!")
=======
print("Welcome to my quiz game")

playing = input("Would you like to play? yes or no: ").lower()

if playing != "yes":
    quit()

print("Well alright then! let's play!")
score = 0

#question 1
question = input("What does CPU stand for?: ").lower()
if question == "central processing unit":
    print("Correct!!!")
    score += 1
else: 
    print("YOU ARE WRONG!!!!!!!")

#question 2
question = input("Who is the main protagonist in Final Fantasy 7?: ").lower()
if question == "cloud strife":
    print("Correct!!!")
    score += 1
else: 
    print("YOU ARE WRONG!!!!!!!")

#question 3
question = input("Who is the main antagonist in Final Fantasy 7?: ").lower()
if question == "sephiroth":
    print("Correct!!!")
    score += 1
else: 
    print("YOU ARE WRONG!!!!!!!")

#question 4
question = input("What game in Sans Undertale from?: ").lower()
if question == "undertale":
    print("Correct!!!")
    score += 1
else: 
    print("YOU ARE WRONG!!!!!!!")

#question 5
question = input("What is 2+2?: ").lower()
if question == "4":
    print("Correct!!!")
    score += 1
else: 
    print("YOU ARE WRONG!!!!!!!")

print("You got" + str(score) + "questions correct!")
print("You got " + str((score / 5) * 100) + "%.")