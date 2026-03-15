import pandas

data = pandas.read_csv("./exercise_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

num_of_gray = 0
for _ in data[data["Primary Fur Color"] == "Gray"]:
  num_of_gray += 1

print(num_of_gray)