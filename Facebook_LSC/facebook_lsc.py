import os
import time
from time import *
from time import sleep
import pandas as pd
import json
import random
import requests
import pyfiglet
import gspread
from rich import print
from rich.console import Console
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv

import urllib.request
from tkinter import *
from mttkinter import mtTkinter
from tkinter.ttk import Progressbar
from tkinter import filedialog,scrolledtext,messagebox,ttk
from tkVideoPlayer import TkinterVideo
from threading import Thread
from playsound import playsound
from PIL import Image, ImageTk
import customtkinter

load_dotenv()

window = Tk()
# window.title('Resizable')
window.geometry("920x700")#920x720
window.resizable(False,False)
window.title("new post flag")
window.config(background="#D4D4D4")
# window.attributes('-alpha',0.2)
# window.overrideredirect(1)


def login():
    for i in range(0,100000000000000000000000000000):
        if stop == 1:#⛔
            clean()
            break
        if connect():

            try:

                for i in range(0,len(username)):
                    display_progress.set("initializing..")
                    progress['value'] = 25
                    fb_home_url = 'https://www.facebook.com/'
                    if account_from_googlesheet == 0:
                        df=pd.read_excel("account/accounts.xlsx", engine='openpyxl')
                        username=df['username'].tolist()
                        password=df['password'].tolist()
                        print(f"read from local excel\n{username}")

                    elif account_from_googlesheet ==1:
                        self.scopes = [

                            'https://www.googleapis.com/auth/spreadsheets',
                            'https://www.googleapis.com/auth/drive',
                        ]
                        self.creds = ServiceAccountCredentials.from_json_keyfile_name(
                            "./key.json", scopes=self.scopes)
                        self.files = gspread.authorize(self.creds)
                        self.workbook = self.files.open("Account_Mgt")
                        self.sheet = self.workbook.worksheet('Sheet2')
                        username=sheet.col_values("A")
                        password=sheet.col_values("B")
                        print(f"read from google spreadsheet\n{username}")


                    chrome_options = webdriver.ChromeOptions()
                    prefs = {"profile.default_content_setting_values.geolocation": 2}
                    chrome_options.add_experimental_option("prefs", prefs)
                    chrome_options.add_argument("--disable-infobars")
                    chrome_options.add_argument("--start-maximized")
                    chrome_options.add_argument("--disable-notifications")
                    chrome_options.add_argument("--disable-popup-blocking")
                    chrome_options.add_argument("--incognito")
                
                    display_progress.set("")
                    progress['value'] = 75
                
                    if show_browser.get()==0:
                        chrome_options.add_argument('--headless')
                        chrome_options.add_argument('--disable-gpu')
                        print("browser not visible")
                    else:
                        print("visible browser")

                    driver = webdriver.Chrome(service=Service(
                                            ChromeDriverManager().install()), options=chrome_options)
            
                    display_progress.set("")
                    progress['value'] = 100

                    sleep(delay)
                    if stop == 1:   #⛔
                        clean()
                        break

                    driver.get(fb_home_url)
                    sleep(delay)# 💤 

                    if stop == 1:   #⛔
                        clean()
                        break
                    print(username[i])
                    print(password[i])
                    
                    driver.find_element(By.XPATH,
                                        "//input[@id='email']").send_keys(username[i])
                

                    driver.find_element(By.XPATH,
                                        "//input[@id='pass']").send_keys(password[i])
                    
                    sleep(delay)
                    if stop == 1:   #⛔
                        clean()
                        break
                    driver.find_element(By.NAME, "good job").click()

                    sleep(delay)
                    if stop == 1:   #⛔
                        clean()
                        break
                    with open('links/fblink.txt','r') as f:
                        target_post=f.readline()
                    print(target_post)
                    driver.get(target_post)
                    

                    
                    sleep(delay)
                    if stop == 1:   #⛔
                        clean()
                        break
                    print("loged in")

                    #like
                    try: 
                        if lik==1:
                            print("like is on")
                            like(driver)
                            if stop == 1:   #⛔
                                clean()
                                break
                        elif lik==0:
                            print("like is off")
                    except:
                        print("like is not working")

                    #share
                    try:
                        if shar==1:
                            print("share is on")
                            share(driver)
                            if stop == 1:   #⛔
                                clean()
                                break
                        elif shar==0:
                            print("share is off")
                    except:
                        print("share is not working")

                    #comment
                    try:
                        if coment==1:
                            comment(driver)
                            if stop == 1:   #⛔
                                clean()
                                break
                        elif coment==0:
                            print("comment is off")
                    except:
                        print("comment is not working")

                    #logout
                    try:
                        logout(driver)
                    except:
                        print("logout isnt working")
                    display_progress.set("")
                    progress['value'] = 0
                    sleep(5)

            except:
                    pass
        else:
            if stop == 1:#⛔
                clean()
                break
            clean()
            print("No internet")
            display_progress.set((""))
            connection_status.set("No internet ...")
            sleep(3)
            connection_status.set("")

def like(driver):
    try:
        like_buttons = driver.find_elements(By.CLASS_NAME,
                                                        "x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x3nfvp2.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x5ve5x3")

        for like_button in like_buttons:
                    cheker_like = like_button.get_attribute("aria-label")
                    if cheker_like == "Like":
                        if stop == 1:   #⛔
                          clean()
                          break
                        time.sleep(delay)
                        like_button.click()
                        ring()
                        print(f"{track_likes} times Liked " + '\N{thumbs up sign}')
                        track_likes+=1
                        driver.implicitly_wait(30)
                        time.sleep(delay)
                        break
                    else:
                        pass
                        if stop == 1:   #⛔
                            clean()
                            break
    except:
        like=driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]")
        like.click()


def share(driver):
    
    share=driver.find_element(By.XPATH,
        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]")
    share.click()

    sleep(delay)

    s=driver.find_element(By.XPATH,
        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
    s.click()




def comment(driver):
    sleep(delay)
    comment=driver.find_element(By.XPATH,
        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/p[1]")
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.PAGE_DOWN)

    comment.send_keys("bertu")
    comment.send_keys(Keys.ENTER)

def logout(driver):
    sleep(delay)
    driver.delete_all_cookies()
    account = driver.find_element(By.CLASS_NAME, "x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.xzsf02u.x1rg5ohu")
    account.click()
    print('logout')
    sleep(delay)
    logout = driver.find_element(
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[5]/div[1]")
    print(account)
    logout.click()
    print('success')


    sleep(delay)# 💤 

def ring():
     try:
        if Ring_bell.get()==1:
            playsound('alarm/like.wav') #alarm
            print('alarm!')
        else:
            print("alarm disabled")
     except:
        print("unable to ring!")


def connect(host='http://google.com'):
    ''' Used to test interet connection'''

    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

def start_thread():
    ''' Used to start the thread that run the scanning'''

    global stop
    stop = 0
    t = Thread (target = login)
    t.start()
    


def stop():
    ''' Used to stop the thread that run the scanning'''

    global stop
    stop = 1
    display_progress.set("Stoping in less than 10 seconds..")
 
    
def clean():
  ''' Used to clean all label txt and progress bar .....called when pressing stop button'''

  progress['value'] = 0
  window.update_idletasks()
  display_progress.set("Stoped!")
  sleep(3)
  display_progress.set("")

def openfile():
    ''' Used to open file sysytem ...called pressing open button'''
    
    
    filepath=filedialog.askopenfilename(title="open file",
                            initialdir='links/',
                            filetypes=((("all files","*.*"),
                            ("text files","*.txt"))))  
    try:
      clear()
      file=open(filepath,'r')
      filename=os.path.basename(file.name)
      entry.delete(0, END)
      entry.insert(0,filename)
      scrolledtext_box.insert('1.0',str(file.read()) )
      file.close
      file_status_label.set("opened")
    except:
      print("no opened file (either you didnt select file and close it or some error catched)")

def save():
  '''used to save the updated file using dialogu box.....called pressing save button '''

  fn=entry.get()
  print(fn)
  f = open(f"./links/{fn}", "w")
  filetxt=scrolledtext_box.get(1.0,END)
  f.write(filetxt)
  print(filetxt)
  f.close()
  scrolledtext_box.delete('1.0', END)
  entry.delete(0, END)
  file_status_label.set("saved!")


def clear():
    ''' Used to cleare the editor and all entry and txt labels....called when small button "clear" pressed '''

    scrolledtext_box.delete('1.0', END)
    entry.delete(0, END)
    file_status_label.set("")


def play_video():
  ''' Used to display demo video'''

  newWindow = Toplevel(master=window)
  newWindow.title("Demo")
  newWindow.geometry("650x400")
  videoplayer = TkinterVideo(master=newWindow, scaled=True)
  videoplayer.load(r"videos/demo.mp4")
  videoplayer.pack(expand=True, fill="both")
  videoplayer.play()

def close():
  ''' Used to display demo video'''

  if messagebox.askyesno("Quit", "Do you really wish to quit?"):
          global stop
          stop=1
          window.destroy()


def show_docmt():
  ''' opens the documentation in a browser'''
  webbrowser.open_new(r'file:/home/amin/Documents/GitHub/Python-GUI/New_feed_notifier/doc/New_feed_notifier_documentation.pdf')

def default():
    pass





console = Console()     #to print to terminal
delay = random.randint(3, 6)



Label(window, 
    text='Post       Promoter',
    fg='#3b5998',
    font=('Arial',35,'bold'),
    compound='bottom',).pack() 


WIDTH=90
HEIGHT=30
xVelocity=0.00005    #0.009
yVelocity=0
canvas=Canvas(window,
    width=WIDTH,
    height=HEIGHT)
canvas.place(x=363,y=11)    
fb_image=Image.open('pictures/lsc.png')
sized_fb_image=fb_image.resize((90, 30))
display_sized_fb_image=ImageTk.PhotoImage(sized_fb_image)
myimage=canvas.create_image(2,
                            2,
                            image=display_sized_fb_image,
                            anchor=NW)


#scrolable text box
scrolledtext_box=scrolledtext.ScrolledText(window,
                                        width= 110, 
                                        height= 10)

scrolledtext_box.place(x=10,y=70)
# scrolledtext_box.focus_set()

#entry
entry=Entry(window, width= 25)
entry.place(x=380,y=248)

#label that show status of file opened/saved...
file_status_label = StringVar()
file_status_label.set("")
Label(window,
    font=('Arial',9),
    text = file_status_label.get(), 
    textvariable = file_status_label).place(x = 15,y = 249) 



customtkinter.set_appearance_mode("System")
# customtkinter.set_default_color_theme("blue")
button_clear = customtkinter.CTkButton(master=window,
    font=('Arial',13,'bold'), 
    fg_color=('#516fad'),
    height= 0.4, 
    width=0.8, 
    text='Clear',
    command=clear)
button_clear.place(x=600,y=249)  


button_open = customtkinter.CTkButton(master=window,
    font=('Arial',13,'bold'),  
    fg_color=('#516fad'), 
    height= 0.4, 
    width=0.8, 
    text='Open',
    command=openfile)
button_open.place(x=280,y=249)


button_save = customtkinter.CTkButton(master=window,
    font=('Arial',13,'bold'),  
    fg_color=('#516fad'), 
    height= 0.4, 
    width=0.8, 
    text='Save',
    command=save)
button_save.place(x=330,y=249)



button_start = customtkinter.CTkButton(master=window, 
    font=('Arial',13,'bold'),  
    fg_color=('#516fad'),
    text='Start',
    command=start_thread)
button_start.place(x=400,y=600)


button_stop = customtkinter.CTkButton(master=window, 
    font=('Arial',13,'bold'), 
    fg_color=('#516fad'), 
    text='Stop',command=stop)
button_stop.place(x=620,y=600)

button_default = customtkinter.CTkButton(master=window, 
    font=('Arial',13,'bold'), 
    fg_color=('#516fad'), 
    text='Set default',command=default)
button_default.place(x=70,y=550)



#progress bar
s = ttk.Style()           
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", 
    foreground='#d4d4d4', 
    background='#297d4e')
progress = Progressbar(window, 
    style="red.Horizontal.TProgressbar", 
    orient = HORIZONTAL,
    length = 140, 
    mode = 'determinate')
progress.place(x =385,
            y = 678)


#taskbar description bottom
display_progress = StringVar()
display_progress.set("")
Label(window,
    font=('Arial',8),
    text = display_progress.get(), 
    textvariable = display_progress).place(x =538,y = 680)

#No internet label  
connection_status = StringVar()
connection_status.set("")
Label(window,
    font=('Arial',11),
    text = connection_status.get(), 
    textvariable = connection_status).place(x =420,y = 500)




#menubar/taskbar
menubar = Menu(window,fg='#1a3f5c')

# #setting
Label(window, 
    text='Configuration',
    fg='#3b5998',
    font="Arial 12 bold underline",
    compound='bottom',).place(x=80,y=312)


global lik
lik = IntVar()
lik.set(1)

global shar
shar = IntVar()
shar.set(1)

global coment
coment = IntVar()
coment.set(0)

global show_browser
show_browser = IntVar()
show_browser.set(0)

global Ring_bell
Ring_bell = IntVar()
Ring_bell.set(1)

global Read_from_bot
Read_from_bot = IntVar()
Read_from_bot.set(1)

global account_from_googlesheet
account_from_googlesheet = IntVar()
account_from_googlesheet.set(1)

Checkbutton(window, text = " Like",
					variable = lik, ##516fad
                    font=("Arial",9,'bold'),
                    fg="#792d6b",
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 10).place(x=27,y=350)
Checkbutton(window, text = " Share",
					variable = shar, ##516fad
                    font=("Arial",9,'bold'),
                    fg="#792d6b",
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 10).place(x=30,y=400)
Checkbutton(window, text = " Comment",
					variable = coment, ##516fad
                    font=("Arial",9,'bold'),
                    fg="#792d6b",
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 10).place(x=40,y=450)

Checkbutton(window, text = " Account from googlesheet",
					variable = account_from_googlesheet,
                    font=("Arial",9,'bold'),
                    fg="#792d6b",
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 23).place(x=42,y=500)



Checkbutton(window, text = " Show browser",
					variable = show_browser, ##516fad
                    font=("Arial",9,'bold'),
                    fg="#792d6b",
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 11).place(x=160,y=350)

Checkbutton(window, text = " Ring bell",
					variable = Ring_bell,
                    font=("Arial",9,'bold'),
                    fg="#792d6b",
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 10).place(x=150,y=400)

Checkbutton(window, text = " Read linkfrom bot",
					variable = Read_from_bot,
                    font=("Arial",9,'bold'),
                    fg="#792d6b",
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 15).place(x=160,y=450)



#help ⋮
help_image=Image.open('pictures/help.png')
sized_help_image=help_image.resize((12, 12))
display_help_image=ImageTk.PhotoImage(sized_help_image)
view_info = Menu(menubar, 
    tearoff=0, 
    fg = '#3c5998')
view_info.add_command(label='Demo video',
    font=("Arial",8,'bold'),
    command=play_video)
view_info.add_command(label='Documentation',
                font=("Arial",8,'bold'),
                command=show_docmt)
menubar.add_cascade(label='Help',
            font=("Arial",9,'bold'),
            menu=view_info,
            image=display_help_image)
window.config(menu=menubar)



window.protocol("WM_DELETE_WINDOW",close)
window.mainloop()


