#ROCK, PAPER, SCISSORS in Python.
import random
options = ("r", "p", "s")
userChoice = input("Choose ROCK(R) or PAPER(P) or SCISSORS(S): ").lower()

#continue and break can be used only in loops (while, for etc)
while userChoice not in options:
    userChoice = input("Choose ROCK(R) or PAPER(P) or SCISSORS(S)").lower()
while True:
    compChoice = random.choice(options)
    print(compChoice)
    winCondition = {"r":"s", "p":"r", "s":"p"}

    if compChoice == userChoice:
        print("IT'S A TIE. Try again.")
        userChoice = input("Choose ROCK(R) or PAPER(P) or SCISSORS(S): ").lower()
        continue
    elif winCondition[compChoice] == userChoice:
        print("COMPUTER WINS")
    else:
        print("YOU WIN")    
    break






"""if((compChoice == "r" and userChoice == "s") or
    (compChoice == "p" and userChoice == "r") or
    (compChoice == "s" and userChoice == "p")):
    print("COMPUTER WINS")
else:
    print("YOU WIN")    



if ((compChoice == "s" and userChoice == "r") or
    (compChoice == "r" and userChoice == "p") or
    (compChoice == "p" and userChoice == "s")):
    print("YOU WIN")

"""



