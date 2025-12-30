import urllib.request
from bs4 import BeautifulSoup
import ssl
import re

# SSL 忽略证书部分
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def get_links(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup('a')


def follow_link(url, position):
    tags = get_links(url)
    return tags[position - 1].get('href')


def extract_name(url):
    match = re.search(r'known_by_([A-Za-z]+)\.html', url)
    if match:
        return match.group(1)


start = input("Enter URL: ")
position = 18        # 题目位置从1开始，所以18→下标17
repeat = 7           # 重复次数

current_url = start
names = []

for i in range(repeat):
    current_url = follow_link(current_url, position)
    names.append(extract_name(current_url))

print("Sequence:", names)
print("Last name:", names[-1])
