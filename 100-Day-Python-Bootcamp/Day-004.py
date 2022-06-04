#Random Module
# you need to type 'import randon'
# To create a module make another file create a variable or whatever print(filename.variablename)
import random

random_integer = random.randint(1 ,10)
print(random_integer)

random_float = random.random()
print (random_float)
























rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

map = [rock, paper, scissors]
user1 = map[choice]
print(user1)

rand = random.randint(0, 2)
print("Computer chose: \n" + map[rand])

if choice == rand:
  print("It's a draw")
elif choice == 0 and rand == 1:
  print("You loose!")
elif choice == 0 and rand == 2:
  print("You win!")
elif choice == 1 and rand == 0:
  print("You win!")
elif choice == 1 and rand == 2:
  print("You loose!")
elif choice == 2 and rand == 0:
  print("You loose!")
elif choice == 2 and rand == 1:
  print("You win!")