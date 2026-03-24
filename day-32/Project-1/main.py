import random
import datetime as dt
import smtplib


#Checking the weekday
now = dt.datetime.now()
week_day = now.weekday()

#Created a variable containing my password and email
my_email = "saviouralex812@gmail.com"
password = "xhnryjjabcpsjbcq"
 
#Checks if the day is monday
if week_day == 1:
  #Opened and read the quote.txt file and convertered the lines to a list
  with open("day-32/Project-1/quotes.txt", mode= "r") as data:
    quotes = data.readlines()
  #Generates a random quote from my quotes list
  monday_quote = random.choice(quotes)
  #Opens the smtp class and starts connection, encrytion, login then sends the email to the given address
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user= my_email, password= password)
    connection.sendmail(from_addr=my_email, to_addrs="codetesters@aol.com", msg=f"Subject:Monday starting quotes\n\n{monday_quote}")

