#Conditional if/else statements, indentation is very important
#if condition: ou must use the colon
# do this
#else: You must use the colon
# do this
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")
#Comparison Operators
# > Greater than
# < less than
# >= Greater than or equal to
# <= less than or equal to
# == Equal to
# != Not equal to
print("\n\n")
#Modulo divides one number by another and gives you the remainder %
number = int(input("Which number do you want to check? "))
if number % 2 > 0:
  print("This is an odd number.")
else:
  print("This is an even number.")


print("\n\n")

#Nested if/else statements, once the first condition is passed we can check for another condition
#if condition:
# if another condition:
#   do this
# else:
#   do this
#else:
# do this

#if/ elif/ else
#if condition1:
# do a
#elif condition2:
# do b
#else:
# do this
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")

print("\n\n")
#BMI Calculator 2.0
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:
  print(f"Your bmi is {bmi}, you are obese.")
else:
  print(f"Your bmi is {bmi}, you are clinically obese.")

print("\n\n")

#Day 3.3 Leap Year
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not a leap year.")
  else:
    print("Leap year.")
else:
  print("Not a leap year.")

print("\n\n")

#Multiple If statements in succession
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
  elif age <= 18:
    bill = 7
  else:
    bill = 12
  
  wants_photo = input("Do you want a photo taken? Y or N.")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bil is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")

print("\n\n")

#3.4 Pizza Order

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

to_pay = 0

if size == "S":
  to_pay += 15
elif size == "M":
  to_pay += 20
else:
  to_pay += 25

if add_pepperoni == "Y":
  if size == "S":
    to_pay +=2
  else:
    to_pay += 3

if extra_cheese == "Y":
  to_pay += 1

print(f"Your final bill is: ${to_pay}")

print("\n\n")

#Logical Operators
#To check for multiple conditions in the same line of code
# and - both must be true
# or - just one needs to be true
# not - 

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")

print("\n\n")

#Day 3.5 Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

n1 = name1.lower() + name2.lower()

t1 = n1.count("t")
r1 = n1.count("r")
u1 = n1.count("u")
e1 = n1.count("e")

true1 = t1 + r1 + u1 + e1

l1 = n1.count("l")
o1 = n1.count("o")
v1 = n1.count("v")
e2 = n1.count("e")

love1 = l1 + o1 + v1 + e2

true_love = int(str(true1) + str(love1))

if true_love < 10 or true_love > 90:
  print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love >= 40 or true_love <= 50:
  print(f"You score is {true_love}, you are alright together.")
else:
  print(f"Your score is {true_love}")



print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")