# number guessing game

import random
import math

def get_name():
    print("Howdy, what's your name? ")
    name = input("(Type in your name) ")
    name = name.title()
    return name

def generate_randnum():
    num = random.randint(1,100)
    return num 

def make_guess():
    guess = int(input(("Your guess? ")))
    return guess

def evaluate_guess(user_guess,gen_num, user_name, user_attempts):
    print("here")
    state = 0
    if user_guess == gen_num:
        print("Well done, {user_name}! You found my number in {user_attempts} tries!")
        state == 1
    elif user_guess > gen_num and user_guess <= 100:
        print("Your guess is too high, try again.")
    elif user_guess < gen_num and user_guess > 0:
        print("Your guess is too low, try again.")
    elif user_guess < 1 or user_guess > 100:
        print("Your guess is out of range! Please make sure you pick a number between 1 and 100.")
    return state

def play_game():
    rand_num = generate_randnum()
    attempts = 10
    for i in range(0,11):
        guess = make_guess() 
        state = evaluate_guess()
        if state == 1:
            break
        attempts -= 1 
    return attempts

def keep_bestscore(user_attempts):
    user_attempts = play_game()

    if user_attempts < best_score:
        best_score = user_attempts
    
    return best_score

def check_win():
    winner = False
    if guess == num:
        winner == True
    return winner

def play():
    
    while True:
        user_name = get_name()

        gen_num = generate_randnum()

        user_guess = make_guess()

        user_attempts = play_game()

        evaluated_user_guess = evaluate_guess(user_guess, gen_num, user_name, user_attempts)

        user_bestscore = keep_bestscore()

        is_winner = check_win(uers_guess, gen_num)

        if is_winner:
            # if rounds_played == 1:
            #     print(f"Well done, {user_name}! You found my number in {num_tries} tries!")
            # if num_tries < best_score:
            #     best_score = num_tries
            #     print(best_score)
            # elif rounds_played > 1:
            #     print(f"Well done, {user_name}! You found my number in {num_tries} tries, but your best score was {best_score}!")
            break
    while True:
        print("Wanna play again? Y/N")
        answer = input("> ")
        answer = answer.title()
        if answer.startswith("Y"):
            play_game()
        else:
            print("Okay, bye!")
            break
play()


# original code

# def play_game():
#     num = random.randint(1,100)
#     print(f"{name} I'm thinking of a number between 1 and 100.")
#     print("Try to guess my number.")
#     guess = 0
#     num_tries = 0
#     rounds_played = 0
#     best_score = math.inf
#     while True:
#         try: 
#             guess = int(input(("Your guess? ")))
#         except ValueError:
#             print("Invalid response. Game over.")
#             break 
#         num_tries += 1 
#         if guess == num:
#             rounds_played += 1 
#             print(rounds_played)
#             if rounds_played == 1:
#                 print(f"Well done, {name}! You found my number in {num_tries} tries!")
#             if num_tries < best_score:
#                 best_score = num_tries
#                 print(best_score)
#             elif rounds_played > 1:
#                 print(f"Well done, {name}! You found my number in {num_tries} tries, but your best score was {best_score}!")
#             break  
#         elif guess > num and guess <= 100:
#             print("Your guess is too high, try again.")
#         elif guess < num and guess > 0:
#             print("Your guess is too low, try again.")
#         elif guess < 1 or guess > 100:
#             print("Your guess is out of range! Please make sure you pick a number between 1 and 100.")
        
#     while True:
#         print("Wanna play again? Y/N")
#         answer = input("> ")
#         answer = answer.title()
#         if answer.startswith("Y"):
#             play_game()
#         else:
#             print("Okay, bye!")
#             break
# play_game()


