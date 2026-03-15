import pandas

csv_file = pandas.read_csv("Project-1/nato_phonetic_alphabet.csv")

file = pandas.DataFrame(csv_file)

nato = {alpha : code for (index.row) }