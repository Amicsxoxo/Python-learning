import requests
from datetime import datetime

#My username and created token on the pixela api
USERNAME = "chimaroke"
TOKEN = "D4HIWy7V6I0"

#The pixela endpoint url
pixela_endpoint = "https://pixe.la/v1/users"

#The pixela chart creation json
user_params = {
  "token" : TOKEN,
  "username" : USERNAME,
  "agreeTermsOfService" : "yes",
  "notMinor" : "yes"
}
#The requests .post to create an account

# response = requests.post(url= pixela_endpoint, json= user_params)
# print(response.text)

#The graph creation url endpoint
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

#Graph creation json
graph_config = {
  "id" : "graph1",
  "name" : "Running Graph",
  "unit" : "Km",
  "type" : "float",
  "color" : "sora"
}

#The header containing my token
headers = {
  "X-USER-TOKEN" : TOKEN
}

#The request .post that creates my graph
# response = requests.post(url= graph_endpoint, json= graph_config, headers= headers)
# print(response.text)

#Checks today's date
today = datetime.now()


#Graph update url endpoint
graph_update = f"{graph_endpoint}/graph1"
print(graph_update)
#Graph update json
graph_update_config = {
  "date" : today.strftime("%Y%m%d"),
  "quantity" : input("How Km did you run today? ")
}

#Request .post to update  todays data
# response = requests.post(url= graph_update, json= graph_update_config, headers= headers)
# print(response.text)

#Graph pixel change url, change the date to the required date
graph_change = f"{graph_update}/20260403"

#Pixel change json, change to the desired quantity
graph_change_config = {
  "quantity" : "0"
}

#The request .put that changes the pixel on the graph
# response = requests.put(url = graph_change, json= graph_change_config, headers= headers)
# print(response.text)


graph_delete = f"{graph_update}/20260403"

#The request .delete that deletes a particular pixel on a particular date on the graph
# response = requests.delete(url = graph_delete,  headers= headers)
# print(response.text)