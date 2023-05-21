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