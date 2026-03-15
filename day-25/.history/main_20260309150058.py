data_list = []

with open("./weather_data.csv") as file:
  data_list += (file.readlines())
  
for data in data_list:
  data = data.strio("\n")
  

print(data_list)