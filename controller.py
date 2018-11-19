import fetchNews, pushNotifications, source
from articleBean import Article
import queue, threading

articles = queue.Queue(maxsize = 20)

def main():
  news_source = source.getSource()
  initiate(news_source)

def initiate(source):
  global articles
  populateList(source)
  if(not(articles.empty())):
    threading.Timer(50.0, sendNotifications).start()
  
def populateList(source):
  global articles
  headlines=fetchNews.get(source)
  headlines = headlines['articles']
  for headline in headlines:
    content = str(headline['content']).encode("utf-8").strip()
    url = str(headline['url'])
    article = Article(content, url)
    articles.put(article)

def sendNotifications():
  global articles
  article = articles.get()
  push(article)
  if(not(articles.empty())):
    threading.Timer(600.0,sendNotifications).start()
    
def push(article):
  pushNotifications.push(article.content, article.url)
  
main()