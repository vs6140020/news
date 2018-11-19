from newsapi import NewsApiClient

newsapi = NewsApiClient('')

def get(source):
 global newsapi
 topHeadlines = newsapi.get_top_headlines(sources=source)
 return topHeadlines
