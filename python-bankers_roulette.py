import random

test_seed = int(input("What is your seed: "))
random.seed(test_seed)

nameAsCSV = input("Give me everbodies names, seperated by a comma. ")
names = nameAsCSV.split(", ")

# -- First Choice


# randNum = random.randint(0,1000)
# if randNum <= 250:
#   payee = names[0]
# elif randNum > 250 and randNum <= 500:
#   payee = names[1]
# elif randNum > 500 and randNum <= 750:
#   payee = names[2]
# elif randNum > 750:
#   payee = names[3]
# print(f"{payee} is going to buy the meal today!")


# -- Second Choice


# x = len(names)
# payee = random.randint(0,x - 1)
# print(f"{names[payee]} is going to buy the meal today!")

payee = random.choice(names)
print(f"{payee} is going to buy the meal today!")

