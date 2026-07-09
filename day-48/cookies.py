from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

#Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#Create and configure the webdriver
driver = webdriver.Chrome(options= chrome_options)
#Navigate to the web page
driver.get("https://orteil.dashnet.org/experiments/cookie/")


while True:
  cookies = driver.find_element(By.ID, "cookie")

  buyMoney = driver.find_element(By.ID, "money")

  buyCursor = driver.find_element(By.ID, "buyCursor")
  buyGrandma = driver.find_element(By.ID, "buyGrandma")
  buyFactory = driver.find_element(By.ID, "buyFactory")
  buyMine = driver.find_element(By.ID, "buyMine")
  buyShipment = driver.find_element(By.ID, "buyShipment")
  buyAlchemy = driver.find_element(By.ID, "buyAlchemy lab")
  buyPortal = driver.find_element(By.ID, "buyPortal")
  buyTime  = driver.find_element(By.ID, "buyTime machine")

  money = ""
  text = (buyMoney.text)
  for n in text.split(","):
    money += n
  money = int(money)


  cursorCost = ""
  text = ((((buyCursor.text).split("\n")[0]).split())[-1])
  for n in text.split(","):
    cursorCost += n
  cursorCost = int(cursorCost)

  grandmaCost = ""
  text = ((((buyGrandma.text).split("\n")[0]).split())[-1])
  for n in text.split(","):
    grandmaCost += n
  grandmaCost = int(grandmaCost)

  factoryCost = ""
  text = ((((buyFactory.text).split("\n")[0]).split())[-1])
  for n in text.split(","):
    factoryCost += n
  factoryCost = int(factoryCost)
  
  mineCost = ""
  text = ((((buyMine.text).split("\n")[0]).split())[-1])
  for n in text.split(","):
    mineCost += n
  mineCost = int(mineCost)

  alchemyCost = ""
  text = ((((buyAlchemy.text).split("\n")[0]).split())[-1])
  for n in text.split(","):
    alchemyCost += n
  alchemyCost = int(alchemyCost)

  shipmentCost = ""
  text = ((((buyShipment.text).split("\n")[0]).split())[-1])
  for n in text.split(","):
    shipmentCost += n
  shipmentCost = int(shipmentCost)

  portalCost = ""
  text = ((((buyPortal.text).split("\n")[0]).split())[-1])
  for n in text.split(","):
    portalCost += n
  portalCost = int(portalCost)

  timeCost = ""
  text = ((((buyTime.text).split("\n")[0]).split())[-1])
  for n in text.split(","):
    timeCost += n
  timeCost = int(timeCost)



  def cookie():
    randNum = random.randint(1,20)
    for n in range(randNum):
      cookies.click()

  cookie()
  
  if money > timeCost:
    buyTime.click()
    cookie()
  elif money > portalCost:
    buyPortal.click()
    cookie()
  elif money > alchemyCost:
    buyAlchemy.click()
    cookie()
  elif money > shipmentCost:
    buyShipment.click()
    cookie()
  elif money > mineCost:
    buyMine.click()
    cookie()
  elif money > factoryCost:
    buyFactory.click()
    cookie()
  elif money > grandmaCost:
    buyGrandma.click()
  elif money > cursorCost:
    buyCursor.click()
  else:
    randNum = random.randint(1,400)
    for n in range(randNum):
      cookie()
  