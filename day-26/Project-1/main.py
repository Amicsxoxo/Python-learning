import pandas

csv_file = pandas.read_csv("day-26/Project-1/nato_phonetic_alphabet.csv")

nato = {row.letter : row.code for (index,row) in csv_file.iterrows() }

# nato_code = [value for letters in users_input for (key,value) in nato.items() if letters == key]


message = True

while message:
  
  users_input = input("Enter a word: ").upper()
  try:
    nato_code = [nato[letter] for letter in users_input ]
  except KeyError:
    print("Sorry, only letters in the alphabet please. ")
  else:
    print(nato_code)
    message = False

#Editted at Day 30

