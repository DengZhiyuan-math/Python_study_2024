import json
import urllib.request

url = 'http://py4e-data.dr-chuck.net/comments_2348170.json'

uh = urllib.request.urlopen(url)
data = uh.read().decode()

info = json.loads(data)

print(sum(item['count'] for item in info['comments']))
