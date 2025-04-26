import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin


chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

num = "005497"
pwd = "Celestial%9961"
url = "http://bolz.21tb.com/els/html/courseStudyItem/courseStudyItem.learn.do?courseId=38b1b90b1d2db6f3d3c79e154e453e31&courseType=NEW_COURSE_CENTER&vb_server=http%3A%2F%2F21tb-video.21tb.com&eln_session_id=elnSessionId.592dc41dd91e4de1abb346da74b25c04"
browser = webdriver.Chrome()
browser.get(url)
browser.implicitly_wait(1)
time.sleep(10)
def DoLogin():
    try:
        browser.find_element(By.ID,'loginName').send_keys(num)
        browser.find_element(By.ID,'swInput').send_keys(pwd)
        browser.find_element(By.CLASS_NAME,'login_Btn').click()
        browser.implicitly_wait(5)
    except:
        pass
    if(browser.find_element(By.CLASS_NAME,'btn-primary')) != []:
        browser.find_element(By.CLASS_NAME,'btn-primary').click()
    browser.find_element(By.XPATH,"/html/body/div[2]/div/main/div/div[2]/div/div[2]/div/div/div[2]/div[2]/div").click()
Lessons = browser.find_element(By.TAG_NAME,"i")
print(Lessons)
for i in Lessons:
    if(i != "100%"|i != "课程评估"):
        i.click()
        
while True:
    elements = browser.find_elements(By.CLASS_NAME,"next-button")
    if elements != []:
        break
time.sleep(120)

