from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#Create and configure the webdriver
driver = webdriver.Chrome(options= chrome_options)
#Navigate to the web page
driver.get("https://secure-retreat-92358.herokuapp.com/")

# total_num = driver.find_element(By.ID, "mwDw")
# total_num.click()

# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# all_portals.click()

# fake_search = driver.find_element(By.ID, "p-search")
# fake_search.click()



fname = driver.find_element(By.NAME, "fName")
lname = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
submit = driver.find_element(By.TAG_NAME, "button")

fname.send_keys("Chima")
lname.send_keys("John")
email.send_keys("chima.jon@email.com")
submit.click()

# driver.quit()