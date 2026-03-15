import pandas

data = pandas.read_csv("./exercise_1/Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

num_of_gray = 0
num_of_black = 0
num_of_cinnamon = 0
for _ in data[data["Primary Fur Color"] == "Gray"]:
  if data["Primary Fur Color"] == "Gray":
    num_of_gray += 1
  elif data["Primary Fur Color"] == "Black":
    num_of_black += 1
  elif data["Primary Fur Color"] == "Cinnamon":
    num_of_cinnamon += 1

print(num_of_gray , "\n" ,num_of_black, "\")
