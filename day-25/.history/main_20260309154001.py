# data_list = []
# with open("./weather_data.csv") as file:
#   data_list += (file.readlines())
# for data in range(len(data_list)):
#   data_list[data] = data_list[data].strip()
import csv
with open("./weather_data.csv") as data_file:
  data = csv.reader(data_file)
  temperature = []
  for row in data:
    print(row)
    temperature.append(row[1])
    
  for temp in range(1, len(temperature)):
    temperature[temp] = int(temperature[temp])
  print(temperature)


