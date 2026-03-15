data_list = []

with open("./weather_data.csv") as file:
  data_list += (file.readlines())
  
for data in range(len(data_list)):
  data = data.strip()
  

print(data_list)