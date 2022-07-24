from tkinter import Y


print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount= bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
#Using round comma ,2 specifies the number of decimal places
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")


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

bmi = int(weight) / float(height) ** 2
bmi_int = int(bmi)
print(bmi_int)

#To round use the round function, you can specify the number of places after a comma
round(8 / 3, 2)
#Use two division symbols // to eliminate the decimal point (makes it an integer)
#Everytime you do regular the division the result is a floating point number
#By using a variable you can continue doing calculations
result = 4 / 2
#This divides the result above by the number 2
result /= 2
#User scores a point
score = 0
#Add or subtract from total
score += 1
#F strings let you mix different types, you place the different types in {}
#print(f"your score is {score}")

#Your life in weeks
age = input("What is your current age?")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")

