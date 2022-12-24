# Import the required libraries
from tkinter import *
from tkinter import ttk
import time
import random
import pyfiglet
from rich import print
from rich.console import Console
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests


console = Console()
delay = random.randint(3, 6)
converted_list = []

with open('./links/flagpagelink.txt', 'r') as file:
    lines_next = file.readlines()
    for element in lines_next:
        converted_list.append(element.strip())
x = len((lines_next))

def begin():
    
    chrome_options = Options()
    prefs = {"profile.default_content_setting_values.geolocation": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=chrome_options)
    time.sleep(delay)
    y = x-1
    for _ in range(1, x):
        driver.execute_script("window.open('');")

    for i in range(x):
        driver.switch_to.window(driver.window_handles[i])
        time.sleep(10)
        driver.get(converted_list[i])
        time.sleep(delay)

def run():
    while running:
         time.sleep(10)
         for i in range(x):
            driver.switch_to.window(
               driver.window_handles[i])
            time.sleep(delay)
            driver.refresh()
            time.sleep(delay)
            times = driver.find_elements(
               By.CLASS_NAME, "x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1heor9g.xt0b8zv.xo1l8bm")
            for ttime in times:

               body_elem = driver.find_element(
                     By.TAG_NAME, 'body')
               body_elem.send_keys(Keys.ARROW_DOWN)
               time.sleep(delay)
               body_elem.send_keys(Keys.ARROW_UP)
               time.sleep(delay)
               sttime = ttime.text
               print(sttime)
               time.sleep(delay)
               def stop():
                  print("hi")

               if sttime == "Just now" or sttime == "1m" or sttime == "2m" or sttime == "1 m" or sttime == "2 m":
                     links = [elem.get_attribute(
                        'href') for elem in times]
                     try:
                        print("Here is New Link -->   ",
                              str(links[0]))
                        with open("./links/file.txt", 'a+') as f:
                           f.writelines("\n")
                           f.writelines(
                                 "New Post on " + links[0])
                        time.sleep(delay)
                        notify_tg_bot()
                        # def notify_tg_bot():
                        import datetime
                        bot_token = '5698535655:AAGfcd8MAvLMCZzgWEp7_2ZEiPCtsMgxzMs'
                        bot_chatID = '-615901499'

                        current_time = datetime.datetime.now().strftime(
                           "Post Date : %Y/%m/%d" + '\n' + '\n' + "Post Time : %H:%M:%S")

                        message_body = str(current_time) + '\n' + \
                           "Here Is The Link  \N{thumbs up sign}   :" + \
                           '\n' + str(links[0])
                        send_text = 'https://api.telegram.org/bot' + bot_token + \
                           '/sendMessage?chat_id=' + bot_chatID + \
                           '&text=' + str(message_body)
                        time.sleep(delay)
                        try:
                           requests.post(send_text)
                           print("Bot Send Link --> ", str(links[0]))
                        except:
                           print("No Link Found")
                           pass

                     except:
                        pass
               else:
                     pass


    root.after(1000, run)

def start():
    global running
    running = True

def stop():
    global running
    running = False


running = True
root = Tk()
root.geometry("1200x1000")

Button(root, text="begin",command=begin,bg='#cc823f',height=2, width= 13).place(x=360, y=500)

Button(root, text="run",command=run,bg='#cc823f',height=2, width= 13).place(x=500, y=500)
Button(root, text="start",command=start,bg='#cc823f',height=2, width= 13).place(x=360, y=600)
Button(root,text='stop',command= stop  ,bg='#cc823f',height=2, width= 13).place(x=500, y=600)

root.after(1000, run)
root.mainloop()