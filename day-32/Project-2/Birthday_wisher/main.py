#Imported all the necessary modules
import smtplib
import random
import datetime as dt
import pandas

#My email and password
my_email = "saviouralex812@gmail.com"
password = "xhnryjjabcpsjbcq"


#Read the csv file
csv_file = pandas.read_csv("day-32/Project-2/Birthday_wisher/birthdays.csv")

#Created a dictionary containing all their names as the key and the remaining details in a list
birthdays = { row.names : [row.email, row.month, row.day]  for (index,row) in csv_file.iterrows() }


#Checking the present day and month
now = dt.datetime.now()
month = now.month
day = now.day

for index,value in birthdays.items():
  #Comparing the birthday with the current day and month
  birth_day = value[2]
  birth_month = value[1]
  birth_email = value[0]

  #Checking if the birthday day and month macth the current date
  if birth_month == month and birth_day == day:

    #Read all the letter files and saved all of them as lists in a variable
    with open("day-32/Project-2/Birthday_wisher/letter_templates/letter_1.txt") as data:
      letter_1 = data.readlines()
    with open("day-32/Project-2/Birthday_wisher/letter_templates/letter_2.txt") as data:
      letter_2 = data.readlines()
    with open("day-32/Project-2/Birthday_wisher/letter_templates/letter_3.txt") as data:
      letter_3 = data.readlines()

    #Nested all the letter lists into one list
    all_letters = [letter_1,letter_2,letter_3]

    #Convert the randomly chosen letter list into a string
    letter = ""
    for lines in random.choice(all_letters):
      letter += lines

    #Replace Angela with my name Chima
    letter = letter.replace("Angela" , f"Chimaroke")

    #Changing the placeholder to the recievers name
    letter = letter.replace("[NAME]" , f"{index}")

    #Establishing connection and encryption
    connection= smtplib.SMTP("smtp.gmail.com")
    connection.starttls()

    #Logining in with my email and password
    connection.login(user= my_email, password= password )

    #Sending the mail from my address to the birthday celebrants mail while changing the subject to thier name and adding the chosen editted letter
    connection.sendmail(from_addr= my_email, to_addrs= birth_email, msg=f"Subject:Happy Birthday {index}\n\n{letter}")