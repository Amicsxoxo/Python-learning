print("Welcome to Treasure island.")
print("Your mission is to find treasure.")

first_direction = input("You are at an cross road, where are you going left? OR right? ")

# second_direction = input("You are at a river, there is an island across, Do you wait for a boat or swim. wait OR swim? ")

# third_direction  = input("You arrived at the island unharmed, Pick a door red, blue or Yellow? ")

if first_direction == "left":
  second_direction = input("You are at a river, there is an island across, Do you wait for a boat or swim. wait OR swim? ")
  if second_direction == "wait":
      third_direction  = input("You arrived at the island unharmed, Pick a door red, blue or Yellow? ")
      if third_direction == "yellow":
       print("You win")
      else:
       print("Game Over")
  else:
      print("Game Over")
else:
  print("Game Over")