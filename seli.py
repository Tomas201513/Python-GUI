# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
# from colorama import Fore, Back, Style
# import random
# import pyfiglet

# randomnumber = round(random.uniform(0, 1000))
# randomsleeptime = round(random.uniform(10, 25))


# chrome_options = webdriver.ChromeOptions()
# prefs = {
# "profile.default_content_setting_values.geolocation": 2}
# chrome_options.add_experimental_option("prefs", prefs)
# chrome_options.add_argument("--disable-infobars")
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--disable-notifications")
# chrome_options.add_argument("--disable-popup-blocking")
# chrome_options.add_argument("--incognito")

# driver = webdriver.Chrome(service=Service(
# ChromeDriverManager().install()), options=chrome_options)
# driver.get("https://www.facebook.com/muferihat.kamil.ahmed")
# x = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[1]")
# # driver.save_screenshot("screenshot.png")
# print(x)
# #  element = driver.find_element_by_id("lst-ib")
# x.save_screenshot("image.png")
# driver.close()







# def linkfound(name,newlink):
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     s += f" Post from {name} at {current_time}\n:{newlink}\n"
#     display5.set(s)


# x=['tomas','tesfa','betti','naol']
# # global s
# s=' '

# for i in x:
#  s =s+ ' '+ i
#  print(s)


# import required module
# from playsound import playsound

# playsound('alarm/a1.wav')
# print('alarm!')



import tkinter as tk

window = Tk()

menubar = Menu(window)
show_all = BooleanVar()
show_all.set(True)
show_done = BooleanVar()
show_not_done = BooleanVar()

view_menu = Menu(menubar)
view_menu.add_checkbutton(label="Show All", onvalue=1, offvalue=0, variable=show_all)
view_menu.add_checkbutton(label="Show Done", onvalue=1, offvalue=0, variable=show_done)
view_menu.add_checkbutton(label="Show Not Done", onvalue=1, offvalue=0, variable=show_not_done)
menubar.add_cascade(label='View', menu=view_menu)
window.config(menu=menubar)
print(show_all.get())



window.mainloop()