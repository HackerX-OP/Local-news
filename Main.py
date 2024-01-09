import requests
import json
import os
import time

month = time.strftime('%m')
year = time.strftime('%Y')

date = time.strftime('%d')
date = int(date) - 1

query = input("On which topic you want to search news: ")
url = f"https://newsapi.org/v2/everything?q={query}&from={year}-{month}-{date}&sortBy=publishedAt&apiKey=424ae6b58d7548ffbfb1e47e0b160281"

news = requests.get(url)

news_dic = json.loads(news.text)
data =  news.json()
for i in range(11):
    articles  = data.get('articles')
    
    title =  articles[i].get('title')
    author = articles[i].get('author')
    desc = articles[i].get('description')

    print(title)
    print(desc)
    print("------------------------------------------------------------")

