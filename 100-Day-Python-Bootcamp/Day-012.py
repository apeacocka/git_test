#Number Guessing Game

import random
from divinethedigits import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    #Checks whether the answer is correct
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinknig of a number between 1 and 100")
    answer = random.randint(1, 100)
    #print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")
game()

#Namespaces: Local vs Global Scope

#Scope
# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

#Local Scope exists within functions
#When you create a variable inside a function it is only available inside the fucntion
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
# drink_potion()
# print(potion_strength)

# #Global Scope
# player_health = 10
# def drink_potion():
#     potion_strength = 2
#     print(player_health)

#Global and Local scope applies to all things named, variables and functions etc
#Everything you give a name to has a namespace and is valid in terms of global or local scope

#Block Scope

#No block scope in python, this means that if you create an if statement with a new variable inside the if, while, for. It has the same
#scope as the enclosing function or else it has global scope

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# #How to modify a global variable
# enemies = 1

# def increase_enemies():
#     #this is a new variable, not related to the same named variable above in the global scope
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

#You can define a global variable inside a function with the keyword global
#global enemies
#This brings the global variable inside the local scope

################### Scope ####################

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

# # Local Scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)

# # Global Scope
# player_health = 10

# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)

#     drink_potion()

# print(player_health)

# # There is no Block Scope

# game_level = 3

# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)


# # Modifying Global Scope

# enemies = 1

# def increase_enemies():
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1

# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

# #Global Constants

# PI = 3.14159
# URL = "https://www.google.com"
# TWITTER_HANDLE = "@yu_angela"

#Make it all upper case if you don't want the global values to ever be changed (soft rule)

