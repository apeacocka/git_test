alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    else:
        end_txt += char
 
  print(f"Here's the {cipher_direction}d result: {end_text}")

from caesar_art import logo
should_continue = True
print(logo)

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == "no":
        should_continue = False
        print("Goodbye")



#Functions that allow you to give them input
#Arguments and Parameters

#Functions take a complex set of instructions and puts them inside a block of code that is named
#Call the function to execute the code fucntion()

#def my_fucntion():
#   do this
#   then do this
#   finally do this


# def my_function():
#     print("Monkey")
#     print("Leopard")
#     print("Giraffe")

# my_function()

#Functions that allow for input.
#The variable 'name' is the parameter and the value it contains is the argument
#Paramter is the name of the data being passed in, the argument is the actual value of the data

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")

# greet_with_name("Tom")

#Functions with more than 1 input
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
# #These are positional arguments in python
# greet_with("Aaron Peacock", "Nowhere")

#To avoid positional erros, use Keyword Argumnets

#Keyword Arguments

# def my_fucntion(a, b, c):
#     print(f"Print {a}")
#     print(f"Print {b}")
#     print(f"Print {c}")

# my_fucntion(c="Angela", b="London", a="Dog")

# import math
# from turtle import width

# from cairo import HINT_STYLE_SLIGHT

# def paint_calc(height, width, cover):
#     area = height * width
#     num_of_cans = math.ceil(area / cover)
#     print(f"You'll need {num_of_cans} cans of paint")

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


#Prime number checker

# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#             print("It's a prime number")
#     else:
#         print("It's not a prime number")

# n = int(input("Check this number: "))
# prime_checker(number=n)

#Caesar Cipher Part 1

#To stop it from producing an error at the end of the alphabet, just put it twice in the variable.
#The index() function stops at the first item it finds
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def encrypt(start_text, shift_amount):
#     end_text = ""
#     for letter in start_text:
#         position  = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         end_text += new_letter
#     print(f"The encoded text is {end_text}")

# def decrypt(end_text, shift_amount):
#     deend_text = ""
#     for letter in end_text:
#         position  = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         deend_text += new_letter
#     print(f"The decoded text is {deend_text}")

# if direction == "encode":
#     encrypt(start_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(end_text=text, shift_amount=shift)

#Cipher Part 3

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     if cipher_direction == "decode":
#         shift_amount *= -1
#     for letter in start_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         end_text += alphabet[new_position]
#     print(f"The {cipher_direction}d text is {end_text}")

# caesar(start_text=text, shift_amount=shift, cipher_direction=direction)