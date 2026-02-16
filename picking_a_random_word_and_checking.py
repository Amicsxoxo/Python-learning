import random
from hangman_art import stages, hangman_logo
from hangman_word_list import word_list





numb_of_words = len(word_list)
#number of words in the list

chosen_word = random.choice(word_list)
print(hangman_logo)

lives = 6
display = []
word_length = len(chosen_word)
for _ in range(word_length):
  display += "_"



  # my style
  # print(display)

# list_of_chosen_word = []
# for letter in chosen_word:
#   list_of_chosen_word += letter
# # print(list_of_chosen_word)


# while not list_of_chosen_word == display:
end_of_game = False
while not end_of_game:
  
  guess = input("\nGuess a letter: ").lower()
  if guess in display:
    print(f"You've guessed {guess} before")

  if guess not in chosen_word:
    lives -= 1 
    print(f"The letter {guess} is not in the word")
  

  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

   
  print(display)
  print(stages[lives])
  
  
  if "_" not in display:
    end_of_game = True
    print("You won")
  elif lives == 0:
    end_of_game = True
    print("You lost")

