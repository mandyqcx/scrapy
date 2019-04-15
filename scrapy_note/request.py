import requests
import io
import sys
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

res = requests.get(
    "https://www.elastic.co/guide/en/logstash/current/index.html")
# print(res.status_code)
# print(res.apparent_encoding)
# print(res.encoding)
res.encoding = 'UTF-8'
# print(res.headers)
# print(res.text)


content = res.text
soup = BeautifulSoup(content, 'html5lib')
div = soup.find_all(class_="book")
for i in div:
    print(i)

