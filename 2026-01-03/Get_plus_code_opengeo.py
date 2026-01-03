# 导入
import json
import urllib.request, urllib.parse

# 引入网址
location = "Kaunas Technology University"

url_API = 'http://py4e-data.dr-chuck.net/opengeo?'
url = url_API + urllib.parse.urlencode({
    "q": location
})

uh = urllib.request.urlopen(url)
# 开始介入数据
data = uh.read().decode()

# 转化为json
js = json.loads(data)

# 打印结果
print(js['features'][0]['properties']['plus_code'])

