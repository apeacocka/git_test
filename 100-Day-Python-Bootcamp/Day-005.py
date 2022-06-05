#for loop

#for item in list_of_items:
# Do something to each item
#Loops allows us to execute the same line of code multiple times
#Inside a foor loop = indented
#A for loop will run for as many times as there are items in the list
from turtle import st

from more_itertools import nth


fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")

print("\n\n")

#Average height
#don't use len() or sum()

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
 
total_height = 0
for height in student_heights:
    total_height += height

number_of_students = 0
#A for loop will run for as many times as there are items in the list
for student in student_heights:
    number_of_students += 1

print(round(total_height / number_of_students))


print("\n\n")
#Day 5.2 Highest Score
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")

#Loops and the range() function
#Range function generates a range of numbers to loop through
#for number in range(a, b):
#   print(number)

#This is for the items 1-10 but not including 10
for number in range(1, 10):
    print(number)
#To indicate the step when moving through a range add another comma and the amount
for number in range(1, 11, 3):
    print(number)

#How to add all numbers from 1 to 100
our_total = 0
for number in range(1, 101):
    our_total += number
print(our_total)

print("\n\n")
#Day 5.3 Adding Evens
evens = 0
for even in range(2,101, 2):
    evens += even
print(evens)

print("\n\n")
#Day 5.4 FizzBuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 ==0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

print("\n\n")
#Password Generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

# print(password)

password_list = []
for char in range(1, nr_letters + 1):
#This work the same as +=
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")