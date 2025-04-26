import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# 填登录的电话和密码
phoneNumber = ""
passwd = ""

# 使用自己的浏览器和设置
option = webdriver.EdgeOptions()
option.add_argument("user-data-dir=C:\\Users\\root\\AppData\\Local\\Microsoft\\Edge\\User Data2")
browser = webdriver.Edge(options=option)

# 模拟登录，如果登录了就不管
browser.get("https://web.everphoto.cn/#dashboard/albums")
browser.implicitly_wait(2)
try:
    browser.find_element(By.XPATH,'//*[@id="everphoto"]/div[1]/div/div[2]/a').click()
    browser.find_element(By.XPATH,'//*[@id="mobile"]').send_keys(phoneNumber)
    browser.find_element(By.XPATH,'//*[@id="password"]').send_keys(passwd)
    browser.find_element(By.XPATH,'//*[@id="everphoto"]/div[1]/div/div[1]/form/div[3]/button').click()
except:
    pass

# 确认登录完成
while True:
    time.sleep(2)
    try:
        browser.find_element(By.CLASS_NAME,"navigator")
        break
    except:
        pass

browser.maximize_window()

# 自动抓取，确认抓取完毕之后手动点击下载，然后暂停转下一个相册去抓
# 如果照片超过一页长，是抓不到的，要动手翻一下
while True:
        try:
            buttonList = browser.find_elements(By.CSS_SELECTOR,".action-button.select-button.unselected")
            if(len(buttonList) == 0):
                listView = browser.find_element(By.XPATH,'//*[@id="dashboard"]/div/div/infinite-list')
                ActionChains(browser)\
                    .scroll_by_amount(0,999)\
                    .perform()
            else:
                for j in range(len(buttonList)):
                    buttonList[j].click()
                    time.sleep(0.1)
            try:
                count = browser.find_element(By.CLASS_NAME,"counts").get_attribute()
                print(count)
            except:pass
        except:
            pass