#Conditional if/else statements, indentation is very important
#if condition: ****You must use the colon
# do this
#else: *****You must use the colon
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
  if year % 100 != 0:
    print("Leap year.")
  if year % 400 == 0:
    print("Leap year.")
else:
  print("Not a leap year.")



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