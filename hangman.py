import random
from wordlist import word_animals

'''
wordlist is a file which contains the tuple word_animals which include
a variety of fruits.
'''

def dispaly_space(space):
    print(" ".join(space))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(word_animals)
    space = ["_"] * len(answer)
    #display_answer(answer)  -  uncomment to view answer 

    incorrect_Guesses = 0
    guessed_letters = set()
    print("*** GUESS THE FRUIT ***")
    print()
    
    while True:
        dispaly_space(space)
        
        
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue  

        if guess in guessed_letters:
            print(f"You already guessed {guess}")
            continue
        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    space[i] = guess
        else:
            incorrect_Guesses += 1           

        if incorrect_Guesses == 20:
            print("You are out of guessess. \n")           
            break
        elif "_" not in space:
            print(f"YOU WIN. The word was {answer}")
            break

if __name__ == '__main__':
    main()
