import requests
import smtplib
import os



my_email = "saviouralex812@gmail.com"
password = "xhnryjjabcpsjbcq"

#Used https://jsonviewer.stack.hu/ to view the json file before formatting

#Used Get-ChildItem Env:   to get all the environment variables and used $env:OWM_API_KEY = "Value" to save the environment variable

parameter = {
  "lat" : 40.837862,
  "lon" : 16.527496,
  "appid" : os.environ.get("OWM_API_KEY"),
  "exclude" : "current,minutely,daily"
}

response = requests.get(url= "https://api.openweathermap.org/data/3.0/onecall", params= parameter)

#Prints the status code of the request if its successfull or the obstacle encountered
print(response.status_code)

response.raise_for_status()
data = response.json()
hourly_data = data["hourly"][:12]

will_rain = False

for hours in hourly_data:
  weather = hours["weather"][0]["id"]
  if weather < 700:
    will_rain = True
    print(weather)

if will_rain:
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user= my_email, password= password)
    connection.sendmail(from_addr=my_email,to_addrs= "codetesters@aol.com",  msg= "Subject:Rain alert\n\nIts going to rain today, remeber to bring an umbrella")

    