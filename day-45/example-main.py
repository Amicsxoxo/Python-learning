from bs4 import BeautifulSoup
# Imported beautifulsoup module

with open(file="day-45/empire.html", mode= "r", encoding= "utf-8") as file:
  # Open the copied source code of the empire website
  soup = BeautifulSoup(file, "html.parser")
  # Used beautifulsoup to read the file

movie_tags = soup.select(selector=".content_content__i0P3p h2 strong")
# Got all the movie tags using the css selector

movies = []
# Created an empty movie list
for tags in movie_tags:
  # Loop through the movie tag list
  movie_name = tags.get_text()
  # Got the movie name from the tags
  movies.append(movie_name)
  # Added the movie name to movies list

ranking_list = []
# Created a ranking list
for movie in movies:
  # Looped through the movie text list
  ranking_list.append((movie.split(")"))[1:])
  # Removed the number and extra parentesis in the text

ranking_list = ranking_list[1:]
# Removed the website heading that has the same selector as the movie text name

lists = []
# Created an empty list 
for _ in ranking_list:
  # Looped through the ranking list 
  names = ""
  # Created an empty string variable
  for __ in _:
    # Looping through the looping list
    names += __
    # Appending the movie name text, it was in a list so had to arrange it together as a string
  names += ")"
  # Added the mistakenly removed parentsis
  lists.append(names)
  # Added the corrected movie names in a new list


with open(file="day-45/movies.docx", mode="w") as file:
  # Opened a new file in write mode
  while ")" in lists:
    # Looping through the list for extra parentisis, if parentesis are not available again the loop stops
    lists.remove(")")
    # Removes the extra parentesis if they exists
  lists.reverse()
  # Reverse the list from 100 - 1 to 1 - 100
  for values in lists:
    # Looping through the final list
    file.write(f"{values}\n")
    # Writing the list values in a new file and giving spaces