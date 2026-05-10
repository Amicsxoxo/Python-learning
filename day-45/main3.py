import requests
from bs4 import BeautifulSoup


response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")


empire_page = response.text
soup = BeautifulSoup(empire_page, "html.parser")

print(soup.prettify())

# movie_tags = soup.select(selector=".content_content__i0P3p h2 strong")

# movies = []
# for tags in movie_tags:
#   movies.append(tags.get_text())
#   print(tags)

# print(movies)