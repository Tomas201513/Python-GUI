import time 
# from time import sleep   
import urllib.request
from colorama import Fore, Back, Style

def connect():
        try:
            urllib.request.urlopen('http://google.com') #Python 3.x
            return True
        except:
            return False

for i in range(0,100):
    try:
        if connect():
            print(Back.GREEN, Fore.YELLOW)
            print("good")
            sleep(3)
        else:
            print(Back.RED, Fore.YELLOW)
            print("bad")
            sleep(3)
    except:
        print("not working")
# print("not working")