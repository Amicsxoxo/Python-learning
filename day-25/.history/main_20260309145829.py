data_list = []

with open("./weather_data.csv") as file:
  data_list += file.readlines()

print(data_list)