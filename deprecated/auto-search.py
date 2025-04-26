import requests 
import re
from bs4 import BeautifulSoup

# 代理服务器
http_proxy  = "http://127.0.0.1:18010"
https_proxy = "https://127.0.0.1:18010"
proxies = {
  'http': 'http://127.0.0.1:18010',
  'https': 'http://127.0.0.1:18010',
}
# http头
headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

def google(q):
    s = requests.Session()
    s.proxies.setdefault('http', '127.0.0.1:18010')
    s.proxies.update(proxies)
    q = '+'.join(q.split())
    url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
    r = s.get(url, headers=headers_Get)
    soup = BeautifulSoup(r.text, "html.parser")
    print(r.text)
    search = soup.find_all(string=re.compile(r'<cite[\d\s\D\S]{1,}</cite>'))
    print(search)
    return search

q = "pipe fittings"
# 关键词输入
results = google(q)
if(len(results != 0)):
    for result in google(q):
        print("1")