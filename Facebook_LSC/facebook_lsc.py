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
    driver.get(home_url)
    sleep(5)# 💤 
    print(username[i])
    print(password[i])