# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
count = 0
sum_numbers = 0
for tag in tags:
    # Extract numbers from the span tags
    try:
        number = int(tag.contents[0])
        sum_numbers += number
        count += 1
    except ValueError:
        continue
print('Count:', count)
print('Sum:', sum_numbers)
