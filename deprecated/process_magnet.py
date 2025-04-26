import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions import *
url = "https://ggbases.dlgal.com/user/myfav.so?p=3"

# option = webdriver.FirefoxOptions()
# option.binary_location = firefox_bin
def login(browser,user_name,password):
    try:
        browser.find_element(By.XPATH,'//*[@id="touch"]/caption/span[2]/a[6]').click()
    except:
        return False
    browser.maximize_window()
    browser.implicitly_wait(2)
    mailLoginBtn = browser.find_element(By.XPATH,'/html/body/div[1]/fieldset/table/tbody/tr[1]/td/div/p[1]/input[2]').click
    time.sleep(1)
    browser.find_element(By.XPATH,'//*[@id="touch"]/tbody/tr[1]/td/div/p[1]/input[3]').send_keys(user_name)
    browser.find_element(By.XPATH,'//*[@id="touch"]/tbody/tr[1]/td/div/p[2]/input').send_keys(password)
    time.sleep(1)
    submitBtn = browser.find_element(By.XPATH,'/html/body/div[1]/fieldset/table/tbody/tr[1]/td/div/p[3]/input[1]').click
    # selenium.webdriver.common.actions.Actions(browser).click(mailLoginBtn).perform();
    time.sleep(10)
    return True
    

def collectFavList(browser):
    # tr.dtr:nth-child(4) > td:nth-child(2) > a:nth-child(1)
    # /html/body/div[1]/fieldset/table/tbody/tr[4]/td[2]/a
    # tr.dtr:nth-child(9) > td:nth-child(2) > a:nth-child(1)
    # /html/body/div[1]/fieldset/table/tbody/tr[9]/td[2]/a
    baseXPATH1 = "/html/body/div[1]/fieldset/table/tbody/tr["
    baseXPATH2 = "]/td[2]/a"
    for i in range(0,50):
        xpath = baseXPATH1+str(i)+baseXPATH2
        try:
            linkElement = browser.find_element(By.XPATH,xpath)
            print(linkElement.get_attribute())
        except:
            print("error!")
            break
    time.sleep(99)

def main():
    browser = webdriver.Chrome()
    browser.get(url)
    user_name = "vyseru@lyft.live"
    password = "9czfbx*@c?Ud@#R84*43"
    if(login(browser,user_name,password) == False):
        print("登录未成功")
        return
    collectFavList(browser)
    


main()