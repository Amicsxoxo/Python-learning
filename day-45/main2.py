# Check the websites "robot.txt" to know what is allowed or not before web scraping

from bs4 import BeautifulSoup

import requests

response = requests.get("https://news.ycombinator.com/news")
# Gets all the data from the website

yc_webpage = response.text
# Gives you the html text from the website

soup = BeautifulSoup(yc_webpage, "html.parser")
# Beautful soup reads the html text


scores_list = []
# Created an empty list for the scores
article_scores = soup.find_all(name= "span", class_ ="score")
# Finds all the scores by using their tags and class
for score in article_scores:
  # For loop for all the article scors
  text = score.text
  # Gets the score text from the article
  scores_list.append(int(text.split()[0]))
  # Adds all the score text to the created score list


text_list = []
link_list = []
# Created a list for the title text and links 
articles =  soup.select(selector=".title .titleline a")
# Selects all the title tag using thier css selector
for article in articles[::2]:
  # For loop going through all the  even title tags, because the odd ones are the subtext and not the title
  text_list.append(article.get_text())
  # Gets the title text and appends it in the created text list
  link_list.append(article.get("href"))
  # Gets all the title links and appends it in the created link list

# print(text_list)
# print(link_list)
# print(scores_list)
# Prints the score list, title test list, and the link list
maxscore = max(scores_list)
upvote_link = link_list[scores_list.index(maxscore)]
upvote_text = text_list[scores_list.index(maxscore)]
print(scores_list.index(maxscore))
print(upvote_link)
print(upvote_text)
print(maxscore)


