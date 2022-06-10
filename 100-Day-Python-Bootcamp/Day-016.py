from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True



while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)


        















#Object Oriented Programming (OOP)

#Procedural programming, setup procedures that do particular things, 
#mostly working top to bottom and jumping to functions if neccessary

#OOP is splitting a larger task into smaller reusable pieces but it goes further

#How to use OOP

#Modeled on something real (like a waiter)
#   Attributes: What it has (plate, tray, item)
#   Methods: What it does (deliver food, take payment) (function)
#Class: Can generate as many of the same object as we want
#Object: What is created

# #   car = CarBlueprint()    each word has a capital         car is object, CarBlueprint is class
# #New object
# from turtle import Turtle, Screen
# import turtle
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)

# my_screen = Screen()
# #Object.attribute
# print(my_screen.canvheight)
# #Object.method()
# my_screen.exitonclick()

#Integrating packages

# from turtle import left
# from prettytable import PrettyTable

# table = PrettyTable()

# table.add_column("Pokemon name",["Pikachu","Squirtle","Charmander"]) 
# table.add_column("Type", ["Electric", "Water", "Fire"])

# table.align = "l"

# print(table)

