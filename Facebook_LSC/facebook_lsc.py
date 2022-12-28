import time
from time import sleep
import pandas as pd
import json
import random
import requests
import pyfiglet
from rich import print
from rich.console import Console
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os
load_dotenv()


fb_home_url = 'https://www.facebook.com/'
df=pd.read_excel("account/accounts.xlsx", engine='openpyxl')
username=df['username'].tolist()
password=df['password'].tolist()


for i in range(0,len(username)):

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.geolocation": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(service=Service(
                        ChromeDriverManager().install()), options=chrome_options)
    driver.get(fb_home_url)
    sleep(5)# 💤 
    print(username[i])
    print(password[i])
    
    driver.find_element(By.XPATH,
                        "//input[@id='email']").send_keys(username[i])
   

    driver.find_element(By.XPATH,
                        "//input[@id='pass']").send_keys(password[i])
    
    sleep(5)
    driver.find_element(By.NAME, "login").click()

    sleep(20)
    with open('links/fblink.txt','r') as f:
        target_post=f.readline()
    print(target_post)
    driver.get(target_post)

    sleep(15)
    print("loged in")
 #like
    try:
        like_buttons = driver.find_elements(By.CLASS_NAME,
                                                        "x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x3nfvp2.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x5ve5x3")

        for like_button in like_buttons:
                    cheker_like = like_button.get_attribute("aria-label")
                    if cheker_like == "Like":
                        time.sleep(delay)
                        like_button.click()
                        print(f"{track_likes} times Liked " + '\N{thumbs up sign}')
                        track_likes+=1
                        driver.implicitly_wait(30)
                        time.sleep(delay)
                        break
                    else:
                        pass
    except:
        like=driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]")
        like.click()


# #share
#     share=driver.find_element(By.XPATH,
#         "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]")
#     share.click()

#     sleep(20)

#     s=driver.find_element(By.XPATH,
#         "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
#     s.click()




#comment
    sleep(20)
    comment=driver.find_element(By.XPATH,
        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/p[1]")
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.PAGE_DOWN)

    comment.send_keys("bertu")
    comment.send_keys(Keys.ENTER)

#logout

    sleep(5)
    driver.delete_all_cookies()
    account = driver.find_element(By.CLASS_NAME, "x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.xzsf02u.x1rg5ohu")
    account.click()
    sleep(10)
    logout = driver.find_element(
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[5]/div[1]")
    print(account)
    logout.click()

    sleep(50)# 💤 


