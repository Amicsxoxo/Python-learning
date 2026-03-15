import pandas

csv_file = pandas.read_csv("Project-1/nato_phonetic_alphabet.csv")

file = pandas.DataFrame(csv_file)

nato = {row.letter : row.code for (index,row) in file.iterrows() }

users_input = input("Enter a word").upper()

nato_code = [value for (key,value) in nato.items() if users_input == key]

print(nato_code)