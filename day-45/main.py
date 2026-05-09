from bs4 import BeautifulSoup
# Imported the beautiful soup module



with open("day-45/website.html", "r", encoding='utf-8') as file:
  # Open the html file as file and changed the default encoding, also set it to read only mode
  soup = BeautifulSoup(file, "html.parser")
  # beautiful soup read the file 

# print(soup.title.string)
# print the string in the title tag

anchor_tag = soup.find_all(name='a')
# Find all the anchor tags in the file

# print(anchor_tag)
# Prints the all the anchor tags found

for tags in anchor_tag:
  # For loop
  print(tags.get_text())
  # Gets all the text in the anchor tag
  print(tags.get("href"))
  # Gets all the href links in the anchor tags

heading = soup.find_all(name="h1", id="name")
# Finds a h1 tag with an id of name
print(heading)
# Prints it out

section_heading = soup.find_all(name= "h3" , class_ = "heading")
# finds all the h3 tags with a class of heading, take note of how the class is been spelt
print(section_heading)
# Prints it 

company_url = soup.select_one(selector="p a")
# The selector is your css selector it can be compounded, it can also accept class like #classname, id as in .idname
print(company_url.get("href"))
# Printing the companys url href