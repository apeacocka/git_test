import os
from auction_art import gavel
print(gavel)


bids = {}
bidding_finished = False
clear = lambda: os.system('clear')

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bidding_record=bids)
    elif should_continue == 'yes':
        clear()






# #Dictionaries and Nesting

# #Dictionaries have two parts: key (word in dictionarie) value (definition)

# #Create dictionarie
# #{Key: Value}
# #separate key and value pairs with a comma

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.", 
#     "Function": "A piece of code that you can easily call over and over again.",
# }

# #How to get a specific item from the dictionarie
# #You must provide the key in it's actual data type
# print(programming_dictionary["Bug"])

# #Adding new items to dictionary.
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

# #Create empty dictionary
# # empty_dictionary = {}
# # #Wipe an existing dictionary the same way
# # programming_dictionary = {}

# #Edit dictionary item
# programming_dictionary["Bug"] = "Bug overdone"

# #Loop through a dictionary this way only provides the keys
# for thing in programming_dictionary:
#     print(thing)

# #To get the value as well as key
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


#Part 2

# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99, 
#   "Draco": 74,
#   "Neville": 62,
# }

# student_grades = {}

# for key in student_scores:
#     score = student_scores[key]
#     if score > 90:
#         student_grades[key] = "Outstanding"
#     elif score > 80:
#         student_grades[key] = "Exceeds Expectations"
#     elif score > 70:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"
    
# print(student_grades)


#Nesting Lists and Dictionaries
# {
#     Key: [List],
#     Key2: {Dict},
# }

# capitals = {
#     "France": "Paris",
#     "Germany": "Berlin",
# }

# #Nesting a list in a Dictionary
# #Leaving an extra comma at the end makes it easy to continue adding to the dictionary
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 14},
#     "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
# }
# print(travel_log)
#You can nest a list in a list
# ["A", "B", ["C", "D"]]

#Nestin a dictionary inside a list

# [{
#     Key: [List],
#     Key2: {Dict},
# },
# {
#     Key: Value,
#     Key2: Value,
# }]

# travel_log = [
#     {
#         "country": "France", 
#         "cities_visited": ["Paris", "Lille", "Dijon"], 
#         "total_visits": 12
#     },
#     {
#         "country": "Germany", 
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
#         "total_visits": 5
#     },
# ]

# print(travel_log)

# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above

# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇

# def add_new_country(country_visited, times_visited, cities_visited):
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["visits"] = times_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)



# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)










