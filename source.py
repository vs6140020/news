import datetime

def getSource():
  currentTime = datetime.datetime.now()
  if(currentTime.hour < 12):
    return 'google-news-in'
  elif(12 <= currentTime.hour <18):
    return 'the-times-of-india'
  else:
    return 'the-hindu'
  