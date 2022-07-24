import random
from highlowart import logo, vs
from highlowdata import data
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess and returns True if they got it right. Or False if they got it wrong.""" 
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    cls()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()

#Tasks

#Display art

#Generate a random account from the game data

#account_a = random.choice(data)
#account_b = random.choice(data)
#if account_a == account_b:
  #account_b = random.choice(data)

#Format account data into printable format

#account_name = account_a["name"]
#account_descr = account_a["description"]
#account_country = account_a["country"]
#print(f"{account_name}, a {account_descr}, from {account_country}")

#Make this a function instead of doing it for both accounts

#def format_dat(account):
  #account_name = account["name"]
  #account_descr = account["description"]
  #account_country = account["country"]
  #print(f"{account_name}, a {account_descr}, from {account_country}")

#print(f"Compare A: {format_data(account_a)}.")
#print(vs)
#print(f"Against B: {format_data(account_b)}.")

#Ask user for a guess

#input("Who has more followers? Type 'A' or 'B': ").lower()

#Check if user is correct
#How many followers each have

#def check_answer(guess, a_followers, b_followers):
  #if a_followers > b_followers:
    #return guess == "a"
  #else:
    #return guess == "b"

#is_correct = check_answer(guess, a_follower_count, b_follower_count)



#a_follower_count = account_a["follower_count"]
#b_follower_count = account_b["follower_count"]

##Get follower count of each account
##Use if statement to check if user is correct

#Give user feedback on their guess
#Score keeping

    # if is_correct:
    #   score += 1
    #   print(f"You're right! Current score: {score}.")
    # else:
    #   game_should_continue = False
    #   print(f"Sorry, that's wrong. Final score: {score}")

#Make the game repeatable

#Making account at position B become the next account at position A

#Clear the screen between rounds

#


# def format_data(account):
#     """Format account into printable format: name, description and country"""
#     account_name = account["name"]
#     account_descr = account["description"]
#     account_country = account["country"]
#     return f"{account_name}, a {account_descr}, from {account_country}."

# def check_answer(guess, a_followers, b_followers):
#     """Checks followers against user's guess and returns True if they got it right. Or False if they got it wrong."""
#     if a_followers > b_followers:
#         return guess == "a"
#     else:
#         return guess == "b"

# print(logo)
# score = 0
# game_should_continue = True
# account_b = random.choice(data)

# while game_should_continue:

#     account_a = account_b
#     account_b = random.choice(data)
    
#     while account_a == account_b:
#         account_b = random.choice(data)
    
#     print(f"Compare A: {format_data(account_a)}")
#     print(vs)
#     print(f"Against B: {format_data(account_b)}")

#     guess = input("Who has more followers? Type 'A' or 'B': ").lower()

#     a_follower_count = account_a["follower_count"]
#     b_follower_count = account_b["follower_count"]
#     is_correct = check_answer(guess, a_follower_count, b_follower_count)

#     cls()
#     print(logo)

#     if is_correct:
#         score += 1
#         print(f"You're right! Current score: {score}")
#     else:
#         game_should_continue = False
#         print(f"Sorry, that's wrong. Final score: {score}")

