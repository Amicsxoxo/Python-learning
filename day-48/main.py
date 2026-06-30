from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://www.amazon.co.uk/Instant-Pot-Electric-Pressure-Stainless/dp/B00OP26T4K/?th=1")



# driver.quit()