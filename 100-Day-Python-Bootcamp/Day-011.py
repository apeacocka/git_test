#Blackjack
import random
import os
from blackjack import logo

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():

  print(logo)

  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"   Your cards: {user_cards}, current score: {user_score}")
    print(f"   Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  cls()
  play_game()








# another_card = True



# def card_selector():
#     randnum = random.randint(0, 12)
#     card = cards[randnum]
#     return card

# uc1 = card_selector()
# uc2 = card_selector()
# pc1 = card_selector()
# pc2 = card_selector()
# current_score = uc1 + uc2
# computer_score = pc1 + pc2

# while another_card:
#     if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
#         if current_score == 21:
#             print("You win!")
#             another_card = False
#         elif computer_score == 21:
#             print("You Lose!")
#             another_card = False
#         if current_score > 21:
#             if 11 in (uc1 or uc2):

#             else:
#                 print("You Lose!")
#                 another_card = False

#         else:
#             print("You Lose!")
#             another_card = False

#         print(f"Your cards: {uc1}, {uc2}, current score: {current_score}")
#         print(f"Computer's first card: {computer_score}")


#     else:
#         clear
