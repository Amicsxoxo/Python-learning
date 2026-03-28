import requests
from datetime import datetime
import smtplib
import time

#My email and password
my_email = "saviouralex812@gmail.com"
password = "xhnryjjabcpsjbcq"

#My longitude and latitude
MY_LAT = 6.524379
MY_LONG = 3.379206


#Checks if the iss is within 5 degrees of my location
def position_close():

  #Accesses the iss location api
  response_ = requests.get(url="http://api.open-notify.org/iss-now.json")
  response_.raise_for_status()
  data_ = response_.json()

  #Gets the longitude and latitude of the iss
  longitude = float(data_["iss_position"]["longitude"])
  latitude = float(data_["iss_position"]["latitude"])

  if ( (MY_LAT - 5) <= latitude <= (MY_LAT + 5) ) and ( (MY_LONG - 5) <= longitude <= (MY_LONG + 5) ):
    return True
  else:
    return False

def is_dark():
#Parameters needed to access the sunset sunrise api
  parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted" : 0,
  }
  #Accessing the sunrise sunset api
  response  = requests.get(url= "https://api.sunrise-sunset.org/json", params= parameters)
  response.raise_for_status()
  data = response.json()

  #Getting the sunrise sunset times
  sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
  sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


  #Checks my current time
  time_now = datetime.now()
  print(time_now.hour)
  if (time_now.hour < sunrise or time_now.hour > sunset):
    return True
  else:
    return False

while True:
  time.sleep(60)
  if position_close() and is_dark():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()

    #Logining in with my email and password
    connection.login(user= my_email, password= password )
    connection.sendmail(from_addr= my_email, to_addrs= "codetesters@aol.com", msg= f"Subject:The iss is above you\n\nLook up")
    pass