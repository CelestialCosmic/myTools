import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

option = webdriver.EdgeOptions()
option.add_argument("user-data-dir=C:\\Users\\root\\AppData\\Local\\Microsoft\\Edge\\User Data2")
browser = webdriver.Edge(options=option)
browser.get('https://stackoverflow.com/questions/39471163/selenium-page-down-by-actionchains')
for i in range(5):
    ActionChains(browser)\
        .scroll_by_amount(0, 100)\
        .perform()
    time.sleep(1)    

input()