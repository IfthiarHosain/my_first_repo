import requests
import json
query=input("what type of news are you interested ")
url="https://newsapi.org/v2/everything?q=query&from=2024-12-09&sortBy=publishedAt&apiKey=c80169619eca4699846441829083d330"
r=requests.get(url)
news=json.loads(r.text)
for article in news["articles"]:
 print(article["title"])
 print(article["description"])
 print("________")