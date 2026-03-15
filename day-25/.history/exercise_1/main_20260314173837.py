import pandas

data = pandas.read_csv("./exercise_1/Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

num_of_gray = 0
num_of_black = 0
num_of_cinnamon = 0

num_of_gray=  len(data[data["Primary Fur Color"] == "Gray"])



num_of_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])


num_of_black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
  "Fur color" : ["Gray" , "Cinnamon" , "Black"],
  "Count"
}