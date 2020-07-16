import requests
from bs4 import BeautifulSoup

url = ("https://www.whitehouse.gov/briefings-statements/")
response = requests.get(url)
# print(result.status_code)
soup = BeautifulSoup(response.content,"html.parser")
# print(soup)

soup_title = soup.findAll("h2",{"class":"briefing-statement__title"})
print(len(soup_title))

articles = []

# for x in range(10):
#    print(soup_title[x].a['href'])
for x in range(10):
    single_title = soup_title[x].a.text
    # print(single_title)
    articles.append(single_title)

for article in articles:
    print(article)
