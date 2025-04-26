import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

# 代理
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = "127.0.0.1:18010"

# 禁止自动控制出现
chrome_options = Options()
chrome_options.add_argument('--proxy-server=%s' % proxy.http_proxy)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

q = input("输入你需要的关键词，支持搜索引擎语法\n")
q = '+'.join(q.split())
url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'

# 启动浏览器
browser = webdriver.Chrome(options=chrome_options)
browser.get(url)
browser.implicitly_wait(1)
urls = []
for i in range(30):
    scroll_origin = ScrollOrigin.from_viewport(10, 10)
    ActionChains(browser)\
        .scroll_from_origin(scroll_origin, 0, 500)\
        .perform()
    time.sleep(0.5)
browser.execute_script("""var data=document.querySelectorAll('span.ylgVCe.ob9lvb').forEach(v=>v.remove())""")
elements = browser.find_elements(By.CLASS_NAME,"qLRx3b.tjvcx.GvPZzd.dTxz9.cHaqb")
with open("./url.txt",encoding="utf-8",mode="w") as f:
    for element in elements:
        source = element.text
        f.write(source+"\n")
print("等待程序结束")
time.sleep(5)


# 第一部分完成