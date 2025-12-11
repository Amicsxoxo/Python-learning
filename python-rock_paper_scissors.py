import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = [rock, paper, scissors]

human_choice = int(input("What did you choose? Type 0 for rock, 1 for paper, 2 for scissors \n"))

computer_choice = random.randint(0,2)

# if computer_choice == 0 and human_choice == 0:
#   print(f"You chose: \n{choice[human_choice]} \n \n computer choose \n{choice[computer_choice]}")
# elif computer_choice == 1 and human_choice == 0:
#   print(f"You chose: \n{choice[human_choice]} \n \n computer choose \n{choice[computer_choice]}")
# elif computer_choice == 2 and human_choice == 0:
#   print(f"You chose: \n{choice[human_choice]} \n \n computer choose \n{choice[computer_choice]}")
# elif computer_choice == 0 and human_choice == 1:
#   print(f"You chose: \n{choice[human_choice]} \n \n computer choose \n{choice[computer_choice]}")
# elif computer_choice == 1 and human_choice == 1:
#   print(f"You chose: \n{choice[human_choice]} \n \n computer choose \n{choice[computer_choice]}")
# elif computer_choice == 2 and human_choice == 1:
#   print(f"You chose: \n{choice[human_choice]} \n \n computer choose \n{choice[computer_choice]}")
# elif computer_choice == 0 and human_choice == 2:
#   print(f"You chose: \n{choice[human_choice]} \n \n computer choose \n{choice[computer_choice]}")
# elif computer_choice == 1 and human_choice == 2:
#   print(f"You chose: \n{choice[human_choice]} \n \n computer choose \n{choice[computer_choice]}")
# elif computer_choice == 2 and human_choice == 2:
#   print(f"You chose: \n{choice[human_choice]} \n \n computer choose \n{choice[computer_choice]}")

# print(f"You chose: \n{choice[human_choice]} \n \n computer choose \n{choice[computer_choice]}")




# Second trial
if computer_choice == human_choice:
    print(f"You Draw\nYou chose: \n{choice[human_choice]} \n\n Computer choose \n{choice[computer_choice]}")
elif computer_choice == 0 and human_choice == 1:
    print(f"You Win\nYou chose: \n{choice[human_choice]} \n\n Computer choose \n{choice[computer_choice]}")
elif computer_choice == 0 and human_choice == 2:
    print(f"You Lose\nYou chose: \n{choice[human_choice]} \n\n Computer choose \n{choice[computer_choice]}")
elif computer_choice == 1 and human_choice == 0:
    print(f"You Lose\nYou chose: \n{choice[human_choice]} \n\n Computer choose \n{choice[computer_choice]}")
elif computer_choice == 1 and human_choice == 2:
    print(f"You Win\nYou chose: \n{choice[human_choice]} \n\n Computer choose \n{choice[computer_choice]}")
elif computer_choice == 2 and human_choice == 0:
    print(f"You Win\nYou chose: \n{choice[human_choice]} \n\n Computer choose \n{choice[computer_choice]}")
elif computer_choice == 2 and human_choice == 1:
    print(f"You Lose\nYou chose: \n{choice[human_choice]} \n\n Computer choose \n{choice[computer_choice]}")
elif human_choice >= 3 or human_choice < 0:
    print("You inputted an invalid number")

# if human_choice >= 3 or human_choice < 0:
#     print("You inputted an invalid number")
# elif computer_choice == 0 and human_choice == 2:
#   print(f"You Lose\nYou chose: \n{choice[human_choice]} \n\n Computer choose \n{choice[computer_choice]}")
# elif computer_choice == 2 and human_choice == 0:
#     print(f"You Win\nYou chose: \n{choice[human_choice]} \n\n Computer choose \n{choice[computer_choice]}")
# elif computer_choice > human_choice:
#     print(f"You Lose\nYou chose: \n{choice[human_choice]} \n\n Computer choose \n{choice[computer_choice]}")
# elif computer_choice < human_choice:
#    print(f"You Win\nYou chose: \n{choice[human_choice]} \n\n Computer choose \n{choice[computer_choice]}")
# elif computer_choice == human_choice:
#     print(f"You Draw\nYou chose: \n{choice[human_choice]} \n\n Computer choose \n{choice[computer_choice]}")










