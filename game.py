# number guessing game

import random

def play_game():
    num = random.randint(1,100)
    print("Howdy, what's your name? ")
    name = input("(Type in your name)")
    name = name.title()
    print(f"{name} I'm thinking of a number between 1 and 100.")
    print("Try to guess my number.")
    num_tries = 0
    guess = 0
    while True:
        guess = int(input(("Your guess? ")))
        num_tries += 1 
        if guess == num:
            print(f"Well done, {name}! You found my number in {num_tries} tries!")
            break 
        elif guess > num and guess <= 100:
            print("Your guess is too high, try again.")
        elif guess < num and guess > 0:
            print("Your guess is too low, try again.")
        elif guess < 1 or guess > 100:
            print("Your guess is out of range! Please make sure you pick a number between 1 and 100.")
    while True:
        print("Wanna play again?")
        answer = input("> ")
        answer = answer.lower()
        if answer.startswith("y"):
            play_game()
        else:
            print("Okay, bye!")
            break
play_game()







