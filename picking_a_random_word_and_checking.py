import random

word_list = ["ardvark", "baboon", "camel"]
numb_of_words = len(word_list)
#number of words in the list

chosen_word = random.choice(word_list)
print(f'The chosen word is {chosen_word}.')
display = []
word_length = len(chosen_word)
for _ in range(word_length):
  display += "_"
  # print(display)

list_of_chosen_word = []
for letter in chosen_word:
  list_of_chosen_word += letter
# print(list_of_chosen_word)


while not list_of_chosen_word == display:
  guess = input("Guess a letter: ").lower()

  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
    
  print(display)

print("You have guessed the right word")