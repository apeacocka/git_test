#Random Module
# you need to type 'import randon'
# To create a module make another file create a variable or whatever print(filename.variablename)
import random

random_integer = random.randint(1 ,10)
print(random_integer)
#can be anything 0.00.... to 0.99....
random_float = random.random()
print (random_float)

random_float = random.random()
print (random_float)

#How to create a random decimal number between 0 and 5
#Multiple by 5

new_num_created = random_float * 5
print(new_num_created)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

#Coin Toss

import random

if random.randint(0, 1) == 0:
  print("Tails")
else: 
  print("Heads")

#Lists
fruits = ["Cherry", "Apple", "Pear"]
#The order is numbered starting at 0
print(fruits[1])
#Use negative index to start counting from the end of the llist
print(fruits[-1])
#To change something in the list
fruits[1] = "Celery"
#To add to list at the end
fruits.append("Pickle")
#To extend a list
fruits.extend(["Buleberry", "Cantelope", "Mango"])


print("\n\n")
#Day 4.2 Who's Playing
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
n = len(names) - 1
random_integer = random.randint(0 ,n)
print(names[random_integer])

#Appedning a list to a list

vegetables = ["Kale", "Tomatoes", "Celery", "Spinach"]
dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])

print("\n\n")

#Day 4.3 Treasure Map

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

place1 = int(position[0]) - 1
place2 = int(position[1]) - 1

if place2 == 1:
  row1[place1] = "X"
elif place2 == 2:
  row2[place1] == "X"
else:
  row3[place2] == "X"

print(f"{row1}\n{row2}\n{row3}")























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