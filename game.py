"""A number-guessing game."""
# create a function that takes in a int and returns an integer
# import random
# take in user input for name (input function)
# print statement for comp saying its thinking of a number
# generate random number (num=random.randint(1,100))
# set an integer = 0 then
# use a while loop  
# take in input of guess
# if guess == to num then print integer from line 7 (number of tries) and 
# 'you won!'
# break 
# if guess > num, print 'your guess is too high, try again' 
# if guess < num, print 'your guess is too low, try again' 
# outside first loop, make second while loop 'wanna play again'
# Put your code here

import random
num = random.randint(1,100)

def play_game(num):
    print("Howdy, what's your name? ")
    name = input("(Type in your name)")
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
        elif guess > num:
            print("Your guess is too high, try again.")
        elif guess < num:
            print("Your guess is too low, try again.")
    while True:
        print("Wanna play again?")
        answer = input("> ")
        answer = answer.lower()
        if answer.startswith("y"):
            play_game(num)
        else:
            print("Okay, bye!")
            break
play_game(num)







