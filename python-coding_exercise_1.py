age = input("What is your current age? ")
age_as_int = int(age)

year = 90 - age_as_int
months = year * 12
week = year * 52
days = year* 365

# print(year)
# print(week)
# print(days)

print(f"Your have {year} years,{months} months, {week} weeks, {days} days left.")