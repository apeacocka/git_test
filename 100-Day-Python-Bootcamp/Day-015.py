#Coffe Machine
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0



            
def is_resource_sufficient(order_ingredients):
    """"Returns true when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return true when the payment is accepted, or False if the money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}.")

power_on = True

while power_on:

    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        power_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])



# def check_resources(choice):
#     if choice == "espresso":
#         if resources["water"] < MENU["espresso"]["ingredients"]["water"]: 
#             print("Sorry there is not enough water.")
#             return
#         elif resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
#             print("Sorry there is not enough coffee.")
#         else:
#             return "Please insert coins."
#     if choice == "latte":
#         if resources["water"] < MENU["latte"]["ingredients"]["water"]: 
#             print("Sorry there is not enough water.")
#             return
#         elif resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
#             print("Sorry there is not enough coffee.")
#             return
#         elif resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
#             print("Sorry there is not enough coffee.")
#             return
#         else:
#             return "Please insert coins."
#     if choice == "cappuccino":
#         if resources["Water"] < MENU["cappuccino"]["ingredients"]["water"]: 
#             print("Sorry there is not enough water.")
#             return
#         elif resources["Milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
#             print("Sorry there is not enough coffee.")
#             return
#         elif resources["Coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
#             print("Sorry there is not enough coffee.")
#             return
#         else:
#             return "Please insert coins."

# def money_in():
#     int(input("how many quarters?: "))
#     int(input("how many dimes?: "))
#     int(input("how many nickels?: "))
#     int(input("how many pennies?: "))




# if choice == "espresso":
#             if resources["Water"] < 50:

#                 coffee_machine()
#             elif resources["Coffee"] < 18:
#                 print("Sorry there is not enough coffee.")
#                 coffee_machine()
#                 print("Yum!")
            
#         elif choice == "latte":
#             if resources["Water"] < 200:
#                 print("Sorry there is not enough water.")
#                 coffee_machine()
#             elif resources["Milk"] < 150:
#                 print("Sorry there is not enough milk.")
#                 coffee_machine()
#             elif resources["Coffee"] < 24:
#                 print("Sorry there is not enough coffee.")
#                 coffee_machine()
#             else:
#                 print("Milky")
#                 coffee_machine()
#         elif choice == "cappuccino":
#             if resources["Water"] < 250:
#                 print("Sorry there is not enough water.")
#                 coffee_machine()
#             elif resources["Milk"] < 100:
#                 print("Sorry there is not enough milk.")
#                 coffee_machine()
#             elif resources["Coffee"] < 24:
#                 print("Sorry there is not enough coffee.")
#                 coffee_machine()
#             else:
#                 print("Frothy")
#         elif choice == "resources":
#             print(f"Water: {resources['Water']}ml\nMilk: {resources['Milk']}ml\nCoffe: {resources['Coffee']}g\nMoney: ${profit}") 
#         else:
#             power_on = False