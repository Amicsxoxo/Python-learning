import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] 

numbers = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]

symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome with my PyPassword Generator")

nr_letters = int(input("How many letters would you want in your password?\n"))
nr_numbers = int(input("How many numbers would you want im your password?\n"))
nr_symbols = int(input("How many symbols would you want im your password?\n"))


#My solution, I know right it's confusing, but it sha work
#Oya clap for me


# ints = 0
# the_letters = []
# for leters in range(0, nr_letters):
#   ints = random.randint(0,len(letters) - 1)
#   print(ints) 
#   the_letters.append(letters[ints])
# print(the_letters)

# the_numbers = []
# numb = 0
# for number in range(0, nr_numbers):
#   numb = random.randint(0,len(numbers) - 1)
#   print(numb) 
#   the_numbers.append(numbers[numb])
# print(the_numbers)

# the_symbols = []
# numb = 0
# for symbo in range(0, nr_symbols):
#   symbo = random.randint(0,len(symbols) - 1)
#   print(symbo)
#   the_symbols.append(symbols[symbo]) 
# print(the_symbols)


# print("Omo")
# print(the_letters)
# print(the_numbers)
# print(the_symbols)


# number_of_characters = nr_letters + nr_numbers + nr_symbols

# print(number_of_characters)

# final_password = [the_letters + the_numbers + the_symbols]
# passy = final_password[0]
# print(passy)
# last_password = random.sample(passy, len(passy))

# print(last_password)

# snas = ""
# for items in last_password:
#   snas = snas + items
# print(snas)


# #Clap one last time U hear



#Second trial with a lil additions or modifications omoooo
# password = ""

# for char in range(1,nr_letters + 1):
#   password += " " + random.choice(letters)

# for char in range(1,nr_numbers + 1):
#   password += " " + random.choice(numbers)

# for char in range(1,nr_symbols + 1):
#   password += " " + random.choice(symbols)


# passy = password.split(" ")
# print(password)
# print(passy)

# pass_word = ""
# for char in range(1, len(passy)):
#   pass_word += random.choice(passy)
#   print(pass_word)

password_list = []

for char in range(1,nr_letters + 1):
  password_list += random.choice(letters)

for char in range(1,nr_numbers + 1):
  password_list += random.choice(numbers)

for char in range(1,nr_symbols + 1):
  password_list += random.choice(symbols)

print(password_list)
random.shuffle(password_list)
print(password_list)


password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")