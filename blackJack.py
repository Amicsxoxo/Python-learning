import random
from blackJack_logo import logo

def games():
  start_game = input("\nDo you want to play a game of BlackJack? Type 'y' of 'n': ")


  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

  computer_choice = []
  human_choice = []
  human_total = 0
  computer_total = 0
  def random_choice():
    return random.choice(cards)

  def computers_choice():
    return  computer_choice.append(random_choice())

  def humans_choice():
    return  human_choice.append(random_choice())



  if start_game == "y":
    computers_choice()
    computers_choice()
    humans_choice()
    humans_choice()

    for numbers in human_choice:
      human_total += numbers
    for numbers in computer_choice:
      computer_total += numbers
    
    def calculation(human,computer):
      if human == computer:
        print("You draw")

      elif human > 21 and computer < 21:
        print("You lose")

      elif computer > 21 and human < 21:
        print("You win")

      elif computer == 21 and (human < 21 or human > 21):
        print("You lose")

      elif human == 21 and (computer < 21 or computer > 21):
        print("You win")

      elif human > 21 and computer > 21:
        if human > computer:
          print("You lose")
        elif human < computer:
          print("You win")

      elif human < 21 and computer < 21:
        if human > computer:
          print("You win")
        elif human < computer:
          print("You lose")
      
    
    print(logo)
    print(f"Your cards are: {human_choice}, current score: {human_total}")
    print(f"Computer's first card: {computer_choice[0]}")
    option = True

    while option:
      continuation = input("Type 'y' to get another card, type 'n' to pass: ").lower()



      if continuation == "y":
        computers_choice()
        humans_choice()
        print(f"Your hand: {human_choice}")

        human_total = 0
        computer_total = 0
        for numbers in human_choice:
          human_total += numbers
        for numbers in computer_choice:
          computer_total += numbers

        if 11 in human_choice and human_total > 21:
          human_total -= 10
        if 11 in computer_choice and computer_total > 21:
          computer_total -= 10

        if human_total > 21 or computer_total >21:
          print(f"\nYour final hand, final score {human_choice}")
          print(f"Computer's final hand, final score {computer_choice}")
          calculation(human=human_total, computer=computer_total)
          option = False
          games()


      else:
        if human_total < 17:
          humans_choice()
        if computer_total < 17:
          computers_choice()
        
        human_total = 0
        computer_total = 0

        for numbers in human_choice:
          human_total += numbers
        for numbers in computer_choice:
          computer_total += numbers

       


       
        print(f"\nYour final hand: {human_choice}, final score {human_total}")
        print(f"Computer's final hand: {computer_choice}, final score {computer_total}")
        calculation(human=human_total, computer=computer_total)
        option = False
        games()
    
    

games()