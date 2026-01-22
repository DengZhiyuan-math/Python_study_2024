# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# or pip install beautifulsoup4 to ensure you have the latest version
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def href_reader(url, ctx=None):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # 返回页面中的所有 <a> 标签
    tags = soup('a')
    return tags
def click_third_link(tags):
    return tags[17]

def click_third_name(link):
    match = re.search(r'known_by_([A-Za-z]+)\.html', link)
    if match:
        name = match.group(1)
        return name


html = input("enter the webpage:")
all_names = []
count = 0
all_names.append(click_third_link(href_reader(html, ctx=None)).get('href', None))


while len(all_names) < 7:
    all_names.append(click_third_link(href_reader(all_names[count], ctx=None)).get('href',None))
    count = count + 1

for name in all_names:
    print(click_third_name(name))