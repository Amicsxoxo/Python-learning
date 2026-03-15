# data_list = []
# with open("./weather_data.csv") as file:
#   data_list += (file.readlines())
# for data in range(len(data_list)):
#   data_list[data] = data_list[data].strip()


# import csv
# with open("./weather_data.csv") as data_file:
#   data = csv.reader(data_file)
#   temperature = []
#   for row in data:
#     print(row)
#     if row[1] != "temp":
#       temperature.append(int(row[1]))

#   print(temperature)

import pandas

data = pandas.read_csv("./weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()

# # print(temp_list)

# print(data["temp"].max())

# # Convert data to columns
# print(data.condition)
# print(data["condition"])

# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
temp = (monday.temp  * 1.8) + 32
print(monday)
print(temp)

data_dict = {
  "students" : ["Amy" , "John" , "Chima"],
  "scores" : [23,34,2]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_file")