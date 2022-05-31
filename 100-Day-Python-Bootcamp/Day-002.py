print("Welcome to the tip calculator.")
total = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
peeps = input("How many people to split the bill? ")
amount = round((float(total) / int(peeps)) * 1.12,2)
amount = "{:.2f}".format(amount)
print(f"Each person should pay: ${amount}")

print("\n")
print("\n")
print("\n")

print(123 + 456)
print("\n")
print("\n")
print("\n")
#Python will remove the underscore, but you can write this way to simulate commas
print(123_456_789)
print("\n\n\n")
# Intergers are int, whole numbers. 
# Numbers with deciamls are called float
# Boolean is true or false
num_char = len(input("What is your name? "))
#Can't concatinate a string and integer
#print("Your name has " + num_char + " characters.")
#To see the type you are dealing with
print(type(num_char))
#Can also do type conversion or type casting
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")
print("\n\n\n")
a = 123
print(type(a))
a = str(123)
print(type(a))
b = float(123)
print(type(b))
c = float(123)
print(type(c))
#String is converted to float and 70 is added
print(70 + float("100.5"))
#My solution
two_digit_number = input("\n\nType a two digit number: ")
new_a = int(two_digit_number[0])
new_b = int(two_digit_number[1])
print(new_a + new_b)
print("\n\n\n")
#For math: Multiply with * and divide with /
#Even when division has no remainder, it still creates a float type
#To the power of is written 2 ** 2 and 2 ** 6
#PEMDAS (), **, *, /, +, -. Calculation goes left to right


#BMI Calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

h1 = float(height)
w2 = int(weight)
bmi = w2 % (h1 ** 2)
print(bmi)