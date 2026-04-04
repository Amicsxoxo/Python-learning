import requests
import smtplib
import os
from random import randint
from email.message import EmailMessage

#Set my email and password
my_email = "saviouralex812@gmail.com"
password = "xhnryjjabcpsjbcq"
#Set the threshold of the change required for the notification to send
threshold = 1
#Set the parameters for the news api
parameters_1 = {
  "apikey" : os.environ.get("SMI_API"),
  "function" : "NEWS_SENTIMENT",
  "symbol" : "TSLA",
  "sort" : "LATEST"
}
#Set the parameters for the daily trading data
parameters_2 = {
  "apikey" : os.environ.get("SMI_API"),
  "symbol" : "TSLA",
  "function" : "TIME_SERIES_DAILY",
}

#Calling the trading data api
response = requests.get(url="https://www.alphavantage.co/query" , params= parameters_2)
trading_data = response.json()

#Accesing the daily trading data dictionary
daily_data = trading_data["Time Series (Daily)"]

#Accessing the key list in the daily trading data of todays and yesterdays daily data
key_list = []
for key,value in daily_data.items():
  key_list.append(key)
key_list = key_list[:2]

#Getting the closing price of today and yesterday
todays_close = float(daily_data[key_list[0]]["4. close"])
yesterday_close = float(daily_data[key_list[1]]["4. close"])

#Checking the percentage increase or decrease in todays and yesterday closing price and rounding it
percent_increase = round((((todays_close - yesterday_close  ) / yesterday_close) * 100), 2)

#Checks if the threshold is reached
if -threshold > percent_increase  or percent_increase > threshold:
  response_1 = requests.get(url="https://www.alphavantage.co/query" , params= parameters_1)
  trading_news = response_1.json()
  print(trading_news)
  latest_news = trading_news["feed"][randint(0,40)]
  #Creates the message because the mail can't encode the emoji
  news_title = latest_news["title"]
  summary = latest_news["summary"]
  source = latest_news["source"]
  sentiment = latest_news["overall_sentiment_label"]

  #Checks if the threshold was crossed with a positive or negative value and uses the accurate emoji
  if -threshold > percent_increase:
    subject = f"TSLA 📉{percent_increase}%"
  elif percent_increase > threshold:
    subject = f"TSLA 📈{percent_increase}%"

  #Creates the smtp email
  with smtplib.SMTP("smtp.gmail.com") as connection:
    #Uses the emailmessage class and creates the subject and the remaining contents of the mail
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = my_email
    msg['To'] =  "codetesters@aol.com"
    msg.set_content(f"Title: {news_title}\n {summary}.\n Source: {source}\n {sentiment}")

    #Starts the connection to the email, login and sends the mail
    connection.starttls()
    connection.login(user= my_email, password=password)
    connection.send_message(msg)