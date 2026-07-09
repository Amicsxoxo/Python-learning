from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= chrome_options)
driver.get("https://www.python.org/")


whole_table = driver.find_elements(By.CLASS_NAME, "shrubbery")
new_table = whole_table[1]
new_table = new_table.text.split("\n")
new_table = new_table[2:]
# print(new_table)

final_dict = {}
for n in range(int(len(new_table)/2)):
  final_dict[n] = {"time": new_table[(n*2)], "name" : new_table[(n*2) + 1] }

print(final_dict)

{0: {'time': '2026-07-13', 'name': 'EuroPython 2026'}, 1: {'time': '2026-07-13', 'name': 'SciPy 2026'}, 2: {'time': '2026-07-14', 'name': 'PyLadies Amsterdam: Building with Coding Agents — Ship a Python Streamlit dashboard'}, 3: {'time': '2026-07-17', 'name': 'DjangoGirls Tamale 2026'}, 4: {'time': '2026-07-18', 'name': 'EuroSciPy 2026'}}

driver.quit()