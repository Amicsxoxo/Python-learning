import pandas

data = pandas.read_csv("./Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

num_of_gray = 0
for data["Primary Fur Color"] == "Gray"