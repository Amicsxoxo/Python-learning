import pandas

data = pandas.read_csv("./exercise_1/Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

num_of_gray = 0
num_of_black = 0
num_of_cinnamon = 0

num_of_gray=  len(data[data["Primary Fur Color"] == "Gray"])



num_of_cinnamon = (data[data["Primary Fur Color"] == "Cinnamon"])


num_of_black = data[data["Primary Fur Color"] == "Black"]

print(num_of_gray ,"\n", num_of_black ,"\n" ,num_of_cinnamon)