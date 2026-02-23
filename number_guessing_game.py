import random
from number_guessing_game_logo import logo

print(logo)
print("Welcome to number guessing game")
print("I'm guessing of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' of 'hard': ")

total_number = []

for numbers in range(1,101):
  total_number.append(numbers)


random_number = random.choice(total_number)

if difficulty == "easy":

  game_status = True
  attempt = 11
  while game_status:
    attempt -= 1
    print(f"You have {attempt} attempts to guess a number.")
    guess = int(input("Make a guess: "))
    if guess == random_number:
      print(f"You got it the answer is {random_number}")
      attempt = 12
      game_status = False
    elif attempt == 1:
      game_status = False
      print("You lose")
    elif guess > random_number:
      print("Too high")
    elif guess < random_number:
      print("Too low")
    print("Guess again")
    
   
elif difficulty == "hard":

  game_status = True
  attempt = 6
  while game_status:
    attempt -= 1
    print(f"You have {attempt} attempts to guess a number.")
    guess = int(input("Make a guess: "))
    if guess == random_number:
      print(f"You got it! The answer is {random_number}")
      attempt = 12
      game_status = False
    if attempt == 1:
      game_status = False
      print("You lose")
    elif guess > random_number:
      print("Too high")
    elif guess < random_number:
      print("Too low")
    print("Guess again")
    
   
