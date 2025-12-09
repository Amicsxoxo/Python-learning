print("Welcome to the love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name2_lower = name2.lower()
name1_lower = name1.lower()

true = name1_lower.count("t") + name2_lower.count("t") +name1_lower.count("r") + name2_lower.count("r") + name1_lower.count("u") + name2_lower.count("u") + name1_lower.count("e") + name2_lower.count("e")
love = name1_lower.count("l") + name2_lower.count("l") +name1_lower.count("o") + name2_lower.count("o") + name1_lower.count("v") + name2_lower.count("v") + name1_lower.count("e") + name2_lower.count("e")

true_love = str(true) + str(love)
if int(true_love) < 10 or int(true_love) > 90:
  print(f"Your love score is {true_love}%, you go togther like coke and mentos")
elif int(true_love) >= 40 and int(true_love) <= 50:
  print(f"Your love score is {true_love}%, you are alright together")
else:
  print(f"Your score is {true_love}%")




