import datetime as dt


now_date = dt.datetime.now()


today = str(now_date.date()).split("-")
date = ""
for letters in today:
  date += letters
print(date)