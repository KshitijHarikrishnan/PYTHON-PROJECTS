#NUMBER GAME in Python.
import random

print("NUMBER GUESSING GAME\n")


number = 0
guess = int(input("Enter a number between 1 - 100: "))
tries = 0

answer = random.randint(1,100)

while True:
    '''
To increase no of tries, you can also use: 
if number.isdigit():
    tries += 1
    '''
    if guess < answer:
        print("HIGHER")
        guess = int(input("Enter a number between 1 - 100: "))
        tries += 1
    elif guess > answer:
        print("LOWER")
        guess = int(input("Enter a number between 1 - 100: "))
        tries += 1
    else: 
        print(f"CORRECT. The answer was {answer}")
        break


print(f"You took {tries + 1} tries")    
