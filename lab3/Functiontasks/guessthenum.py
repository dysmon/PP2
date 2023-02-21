import random

def GuessGame():
    x = (random.randrange(1, 20))

    name = input("Hello! What is your name?\n")

    guess = int(input(f"""\nWell, {name}, I am thinking of a number between 1 and 20.
Take a guess.\n"""))

    tries = 1
    while(guess!=x):
        if(guess>x):
            print("""\nYour guess is too up.""")
            print("Take a guess.")
        elif(guess<x):
            print("""\nYour guess is too low.""")
            print("Take a guess.")
        tries+=1
        guess = int(input())

    if(guess==x):
        print(f"\nGood job, {name}! You guessed my number in {tries} guesses!")