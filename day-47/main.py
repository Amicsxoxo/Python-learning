from bs4 import BeautifulSoup
import requests
import smtplib
import os

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

url = "https://www.amazon.co.uk/Instant-Pot-Electric-Pressure-Stainless/dp/B00OP26T4K/ref=sr_1_4?crid=1Z9K7QG8X5E3&keywords=instant+pot&qid=1685614412&sprefix=instant+pot%2Caps%2C78&sr=8-4"

headers = {
  "Accept-Language":"en-US",
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/}"
}

response = requests.get(url= url, headers= headers)
soup = BeautifulSoup(response.text, "html.parser")

print(soup.prettify())

# whole = soup.select(selector=".a-price-whole")
# frac = soup.select(selector=".a-price-fraction")
# whole_price = str(whole[0].getText())
# whole_price_list = whole_price.split(",")
# whole_price = ""
# for _ in whole_price_list:
#   whole_price += _

# frac_price = str(frac[0].getText())

# total_price = whole_price + "." + frac_price
# total_price = float(total_price)

# print(type(total_price))
# print(total_price)

# if total_price < 200000:
#   with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user= my_email, password= password)
#     connection.sendmail(from_addr=my_email,to_addrs= "codetesters@aol.com",  msg= f"Subject:Price alert\n\nThe product price is now below 200,000\nThe price is ${total_price}")
# else:
#   pass