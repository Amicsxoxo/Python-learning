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

temp_list = data["temp"].to_list()

# print(temp_list)



# avg_temp = sum(temp_list)/len(temp_list)

# print(avg_temp)
(data["temp"].max())