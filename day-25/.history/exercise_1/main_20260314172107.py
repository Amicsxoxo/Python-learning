import pandas

data = pandas.read_csv("./Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

num_of_gray = 0
data["Primary Fur Color"] == "Gray"