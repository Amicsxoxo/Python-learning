from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://www.python.org/")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# print(f"The price dollar is {price_dollar.text}.{price_cents.text}")


#Finding elements by name using selenium, the name of the element is q and we can print the tag name, and also get the placeholder value using the get_attribute function with the search bar
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.tag_name)
button = driver.find_element(By.ID, value="submit")
print(button.size)


#Quit closes the entire browser
driver.quit()

#Close is just for that particular tab
#driver.close()