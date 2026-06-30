from bs4 import BeautifulSoup
import requests
import smtplib
import os

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")

url = "https://appbrewery.github.io/instant_pot/"

headers = {
  "Accept-Language":"en-US",
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/}"
}

response = requests.get(url= url, headers= headers)
soup = BeautifulSoup(response.text, "html.parser")

whole = soup.select(selector=".a-price-whole")
frac = soup.select(selector=".a-price-fraction")
total_price = str(whole[0].getText()) + str(frac[0].getText())
total_price = float(total_price)
print(type(total_price))
print(total_price)

if total_price < 100:
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user= my_email, password= password)
    connection.sendmail(from_addr=my_email,to_addrs= "codetesters@aol.com",  msg= f"Subject:Price alert\n\nThe product price is now below $100\nThe price is ${total_price}")
else:
  pass