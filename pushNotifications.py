import requests

def push(content, url):
 payload = {
  "app_key": "",
  "app_secret": "",
  "target_type": "app",
  "content": content,
  "content_type": "url",
  "content_extra": url
 }
 r = requests.post('https://api.pushed.co/1/push',data=payload)
 print(r.text)
 return r
