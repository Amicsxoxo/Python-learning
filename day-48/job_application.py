from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#Create and configure the webdriver
driver = webdriver.Chrome(options= chrome_options)
#Navigate to the web page
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
time.sleep(5)

job = driver.find_element(By.LINK_TEXT, "Python Developer")
job.click()

time.sleep(5)

easy_apply = driver.find_element(By.CLASS_NAME, "artdeco-button__text")
easy_apply.click()

time.sleep(5)

number = driver.find_element(By.CLASS_NAME, " artdeco-text-input--input")
number.send_keys("12349850")

time.sleep(7)

next_1 = driver.find_element(By.ID, "ember739")
next_1.click()

time.sleep(5)

next_2 = driver.find_element(By.ID, "ember1059")
next_2.click()


next_3 = driver.find_element(By.ID, "ember1069")
next_3.click()

