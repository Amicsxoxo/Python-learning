# import smtplib

# my_email = "saviouralex812@gmail.com"
# password = "xhnryjjabcpsjbcq"
 
# with smtplib.SMTP("smtp.gmail.com") as connection:
#   connection.starttls()
#   connection.login(user= my_email, password= password)
#   connection.sendmail(from_addr=my_email, to_addrs="codetesters@aol.com", msg="Subject:Hello\n\nThis is the body of my first smtp email")

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
week_day = now.weekday()
print(week_day)

date_of_birth = dt.datetime(year= 2007, month= 5, day=6)

print(date_of_birth)