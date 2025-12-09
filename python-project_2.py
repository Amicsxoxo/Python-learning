print("Welcome to Treasure island.")
print("Your mission is to find treasure.")

#ASCII ART

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
first_direction = input('You\'re at an cross road, where are you going "left" OR "right"? ').lower()

# second_direction = input("You are at a river, there is an island across, Do you wait for a boat or swim. wait OR swim? ")

# third_direction  = input("You arrived at the island unharmed, Pick a door red, blue or Yellow? ")

if first_direction == "left":
  second_direction = input('You\'r at a river, there is an island across, Do you wait for a "boat" or "swim". ').lower()
  if second_direction == "wait":
      third_direction  = input("You arrived at the island unharmed, Pick a door red, blue or yellow? ").lower()
      if third_direction == "yellow":
       print("You win")
      else:
       print("Game Over")
  else:
      print("Game Over")
else:
  print("Game Over")