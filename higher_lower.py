from higher_lower_data import data
from higher_lower_art import logo
from higher_lower_art import vs
import random

import os


score = 0
game = True
while game:
  print(logo)
  if score > 0:
    print(f"You're right! current score: {score}")
    
  if score == 0:
    random_choice_1 = random.choice(data)
  random_choice_2 = random.choice(data)

  if random_choice_1 == random_choice_2:
      random_choice_2 = random.choice(data)

  print(f"Compare A: {random_choice_1['name']}, a {random_choice_1['description']}, from {random_choice_1['country']}")

  print(vs)

  print(f"Compare B: {random_choice_2['name']}, a {random_choice_2['description']}, from {random_choice_2['country']}")
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()

  if (random_choice_1['follower_count'] > random_choice_2['follower_count']) and answer == "a":
    score += 1
    game = True
    random_choice_1 = random_choice_2
    os.system('cls')
  elif (random_choice_2['follower_count'] > random_choice_1['follower_count']) and answer == "b":
    score += 1
    game = True
    random_choice_1 = random_choice_2
    os.system('cls')
  else:
    os.system('cls')
    game = False
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")



