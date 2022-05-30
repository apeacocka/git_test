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





