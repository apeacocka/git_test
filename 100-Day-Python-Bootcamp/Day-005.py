password_list = []

for char in range(1, nr_letters + 1):
  password_list += random.choice(letters)
# append do the same as +=
for char in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")