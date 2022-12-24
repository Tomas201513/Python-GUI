#!/usr/bin/env python3
import os
import requests
import time
from time import *
from time import sleep
import datetime
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
from tkinter import *
from mttkinter import mtTkinter
from tkinter.ttk import Progressbar
from tkinter import filedialog,scrolledtext,messagebox,ttk
from tkVideoPlayer import TkinterVideo
from threading import Thread
from playsound import playsound
import urllib.request
from PIL import Image, ImageTk
import customtkinter

window = Tk()
window.geometry("920x720")
window.resizable(False,False)
window.title("new post flag")
window.config(background="#D4D4D4")


def play_video():
        newWindow = Toplevel(window)
        newWindow.title("New Window")
        newWindow.geometry("400x400")

        Label(newWindow,
          text ="Register user here").grid(row=0, column=2)
        Label(newWindow,
          text ="").grid(row=1, column=1)
        Label(newWindow,
          text ="Username: ").grid(row=2, column=1)
        Label(newWindow,
          text ="(telegram)").grid(row=3, column=1)
        Label(newWindow,
          text ="").grid(row=4, column=1)
        Label(newWindow,
          text ="assigned link: ").grid(row=5, column=1)
        Button(master=newWindow, text="Submit",command=submit).grid(row=6, column=1)

        




menubar = Menu(window,fg='#1a3f5c')

help_image=Image.open('pictures/help.png')
sized_help_image=help_image.resize((12, 12))
display_help_image=ImageTk.PhotoImage(sized_help_image)

view_info = Menu(menubar, 
    tearoff=0, 
    fg = '#3c5998')
view_info.add_command(label='Add user',
    font=("Arial",8,'bold'),
    command=play_video)
menubar.add_cascade(label='Edit',
    font=("Arial",9,'bold'), 
    menu=view_info,
    image=display_help_image)
    
window.config(menu=menubar)

window.mainloop()
