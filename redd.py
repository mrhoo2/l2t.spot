# Goes to /r/listentothis and sorts by top weekly posts.
import requests
import json


r = requests.get(r'http://reddit.com/r/listentothis/top/.json')
print r

r.text
data = r.json()

for child in data['data']['children']:
    print child['data']['secure_media']['oembed']['title'], "\r\n"
    print

# print data['data']['children'][0]['data']['secure_media']['oembed']['title']
