import pandas

csv_file = pandas.read_csv("Project-1/nato_phonetic_alphabet.csv")

nato = {row.letter : row.code for (index,row) in csv_file.iterrows() }

users_input = input("Enter a word: ").upper()

nato_code = [value for letters in users_input for (key,value) in nato.items() if letters == key]
nato_code = [nato[users_input]]

print(nato_code)