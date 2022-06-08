#Functions with Outputs
#Build Calculator

from calc_art import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
     "+": add, 
     "-": subtract,
     "*": multiply, 
     "/": divide,
}

def calculator():
    print(logo)

    num1 = float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
            
calculator()
#Return can be used to pass the output to another function

#Functions are good for repeated tasks
#Function with input
#def my_fucntion(something):
#   do this with something
#   then do this
#   finally do this

#Function with output will replace in the line of code where the function is called and save it in a variable
#return is key word for function with output
#def my_function():
#   result = 3 * 2
#   return result

#output = my_function()

#Instead of print you can use return
#Return output replaces the part of the code where the function was called

#Multiple return values
#return keyword is the end of the function

# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs"
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return (f"{formated_f_name} {formated_l_name}")

#    print(f"{formated_f_name} {formated_l_name}")



# formated_string = format_name(input("What is your first name? "), input("What is your last name? "))
# print(formated_string)


# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False

# def days_in_month(year, month):
#     if month > 12 or month < 1:
#         return "Invalid Month"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month - 1]
  
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)


#Docstrings are used to create documentation along the way
#Use 3 quotes inside the function to give it it's explanation
#3 quotes can be used for multi line commments, official guidance is to avoid this


# def format_name(f_name, l_name):
#     """Take a first and last name and format it
#     to return the title case version of the name"""
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs"
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return (f"{formated_f_name} {formated_l_name}")

# format_name()

# def add(n1, n2):
#   return n1 + n2
 
# def subtract(n1, n2):
#   return n1 - n2
 
# def multiply(n1, n2):
#   return n1 * n2
 
# def divide(n1, n2):
#   return n1 / n2
 
# print(add(2, multiply(5, divide(8, 4))))











