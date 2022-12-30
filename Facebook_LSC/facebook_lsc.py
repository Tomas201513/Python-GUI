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


def ጀምር():
    for i in range(0,100000000000000000000000000000):

        if stop == 1:#⛔
            clean()
            break
        if connect():
    
            try:
        
                display_progress.set("initializing..")
                progress['value'] = 25
                window.update_idletasks()
                fb_home_url = 'https://www.facebook.com/'
                disbled_link = 'checkpoint/disabled/?next'
                password_fail = 'login/?privacy_mutation_token'
                print(account_from_googlesheet.get())
                if account_from_googlesheet.get() == 0:
                    df=pd.read_excel("account_counter/accounts.xlsx", engine='openpyxl')
                    username=df['username'].tolist()
                    password=df['password'].tolist()
                    print(f"read from local excel\n{username}")

                elif account_from_googlesheet.get() ==1:
                    scopes = [

                        'https://www.googleapis.com/auth/spreadsheets',
                        'https://www.googleapis.com/auth/drive',
                    ]
                    creds = ServiceAccountCredentials.from_json_keyfile_name(
                        "./key.json", scopes=scopes)
                    files = gspread.authorize(creds)
                    workbook = files.open("Account_Mgt")
                    sheet = workbook.worksheet('Sheet2')
                    username=sheet.col_values(1)
                    password=sheet.col_values(2)
                    print(f"read from google spreadsheet\n{username}")
                else:
                    print("coudnt get accounts")
                
                with open('Working_Accounts.txt','r+')as f:
                    j=f.readline()
                for i in range(j,len(username)):
                    try:
                        with open('Working_Accounts.txt','r+')as f:
                            f.write(f"{i} \n")
                    except Exception as e:
                        print(e)
                    like_progress['value'] = 0
                    window.update_idletasks()
                    share_progress['value'] = 0
                    window.update_idletasks()
                    comment_progress['value'] = 0
                    window.update_idletasks()
                    if i==0:
                        like_count.set(total_coment)
                        share_count.set(total_coment)
                        comment_count.set(total_coment)
                    else:
                        pass
                    account_counter.set(f"{i+1} / {len(username)}")
                    display_scaned_username.set(username[i])
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

                    sleep(delay)# 💤 
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
                    
                    sleep(delay)# 💤 
                    if stop == 1:   #⛔
                        clean()
                        break
                    driver.find_element(By.NAME, "login").click()
                    sleep(delay)# 💤 

                    current_url = driver.current_url
                    if home_url == current_url:
                    
                        login()
                    elif disbled_link in current_url:
                        console.print("Login Disabled", style="red")
                        f = open('logfiles/Disabled_Accounts.txt', 'a')
                        f.write(str(i) + ' ' + str(username[i]) + '\n')
                        f.close()

                        disabled_counter=disabled_counter+1
                        disabled_account_count.set(disabled_counter)

                    elif password_fail in current_url:
                        console.print("Password Fail", style="red")
                        f = open(
                            'logfiles/Password_Fail_Accounts.txt', 'a')
                        f.write(str(i) + ' ' + str(username[i]) + '\n')
                        f.close()
                        paswd_fail_counter=paswd_fail_counter+1
                        failed_account_count.set(paswd_fail_counter)
                       
                    else:
                        console.print("Login Failed", style="red")
                        f = open('logfiles/Failed_Accounts.txt', 'a')
                        f.write(str(self.i) + ' ' + str(self.username) + '\n')
                        f.close()
                        failed_counter=failed_counter+1
                        paswd_fail_accounts_count.set(failed_counter)
                        

                    if i==len(username):
                        try:
                            with open('logfiles/Working_Accounts.txt','r+') as f:
                                f.truncate()
                            report()
                            print("reported")
                        except Exception as e:
                            print(e)
                            print("coudnt report")
                        try:
                            with open('logfiles/Working_Accounts.txt','r+') as f:
                                f.truncate()
                            report()
                            print("interupt truncated")
                        except Exception as e:
                            print(e)
                            print("coudnt interupt truncated")
                        try:
                            Working_Accounts = open('logfiles/Working_Accounts.txt', 'r+')
                            Working_Accounts.truncate()
                        
                            Disabled_Accounts = open('logfiles/Disabled_Accounts.txt', 'r+')
                            Disabled_Accounts.truncate()
                            
                            Failed_Accounts = open('logfiles/Failed_Accounts.txt', 'r+')
                            Failed_Accounts.truncate()

                            Password_Fail_Accounts = open('logfiles/Password_Fail_Accounts.txt', 'r+')
                            Password_Fail_Accounts.truncate()
                        
                        except Exception as e:
                            print(e)
                        if stop == 1:   #⛔
                            clean()
                            break
            except Exception as e:
                    print(e)
                    print("some error")
        else:
            if stop == 1:#⛔
                clean()
                break
            clean()
            print("No internet")
            display_progress.set((""))
            connection_status.set("No internet ...")
            sleep(3)# 💤 
            connection_status.set("")
def login():
    if stop == str(1):   #⛔
        clean()
        return
    if Read_from_bot.get()==0:

        with open('links/fblink.txt','r') as f:
            link=f.readline()
        print(link)

    elif Read_from_bot.get()==1:
        try:
            url = f"https://api.telegram.org/bot{tooken}/getUpdates?offset=-1"

            links = requests.get(url, verify=False)
            time.sleep(delay)

            getText = links.text

            data = json.loads(getText)

            try:
                link = data['result'][0]['message']['text']
            except Exception as e:
                print(e)
                pass

            try:
                link = data['result'][0]['edited_message']['text']
            except Exception as e:
                print(e)
                pass
            print(link)
        except Exception as e:
            print(e)
    else:
        print("can't get link")

    

    driver.get(link)
    sleep(delay)
    if stop == str(1):   #⛔
        clean()
        return
    print("loged in")

    #like
    try: 
        if lik==1:
            print("like is on")
            like(driver)
            if stop == str(1):   #⛔
                clean()
                return
        elif lik==0:
            print("like is off")
    except Exception as e:
        print(e)
        print("like is not working")

    #share
    try:
        if shar==1:
            print("share is on")
            share(driver)
            if stop == str(1):   #⛔
                clean()
                return
        elif shar==0:
            print("share is off")
    except Exception as e:
        print(e)
        print("share is not working")

    #comment
    try:
        if coment==1:
            comment(driver)
            if stop == str(1):   #⛔
                clean()
                return
        elif coment==0:
            print("comment is off")
    except Exception as e:
        print(e)
        print("comment is not working")

    #logout
    try:
        logout(driver)
    except Exception as e:
        print(e)
        print("logout isnt working")
    display_progress.set("")
    progress['value'] = 0
    sleep(5)# 💤 

    
                          
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
                        sleep(delay)# 💤 
                        like_button.click()
                        like_count.set(like_count+1)
                        like_progress['value'] = 100
                        window.update_idletasks()       
                        ring()
                        print(f"{track_likes} times Liked " + '\N{thumbs up sign}')
                        track_likes+=1
                        driver.implicitly_wait(30)
                        sleep(delay)# 💤 
                        break
                    else:
                        pass
                        if stop == 1:   #⛔
                            clean()
                            break
    except Exception as e:
        print(e)
        like=driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]")
        like.click()
        like_progress['value'] = 100
        window.update_idletasks()


def share(driver):
    
    share=driver.find_element(By.XPATH,
        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]")
    share.click()

    sleep(delay)# 💤 

    s=driver.find_element(By.XPATH,
        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]")
    s.click()
    share_progress['value'] = 100
    window.update_idletasks()




def comment(driver):
    sleep(delay)# 💤 
    comment=driver.find_element(By.XPATH,
        "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[5]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/p[1]")
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.PAGE_DOWN)

    comment.send_keys("bertu")
    comment.send_keys(Keys.ENTER)
    comment_progress['value'] = 100
    window.update_idletasks()

def logout(driver):
    sleep(delay)# 💤 
    driver.delete_all_cookies()
    account_counter = driver.find_element(By.CLASS_NAME, "x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.xzsf02u.x1rg5ohu")
    account_counter.click()
    print('logout')
    sleep(delay)# 💤 
    logout = driver.find_element(
        By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[5]/div[1]")
    print(account_counter)
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
     except Exception as e:
        print(e)
        print("unable to ring!")


def connect(host='http://google.com'):
    ''' Used to test interet connection'''

    try:
        urllib.request.urlopen(host)
        return True
    except Exception as e:
        print(e)
        return False

def start_thread():
    ''' Used to start the thread that run the scanning'''

    global stop
    stop = 0
    t = Thread (target = ጀምር)
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
  sleep(3)# 💤 
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
    except Exception as e:
        print(e)
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
 
    lik.set(1)
    shar.set(1)
    coment.set(0)
    show_browser.set(0)
    Ring_bell.set(1)
    Read_from_bot.set(1)
    account_from_googlesheet.set(1)
    send_report.set(1)





def report():

        url = f"https://api.telegram.org/bot{reporter}/sendDocument?chat_id={reported_to_chat_id}"

        tobe_reported_docs=['Disabled_Accounts.txt','Failed_Accounts.txt','Password_Fail_Accounts.txt']
        doc_count=0
        for docs in tobe_reported_docs:
            doc_count+=1
            files = {'document': open(f'logfiles/{docs}', 'rb')}
            response= requests.post(url, files=files)
            status=response.status_code
            if status==200:
                print("Report sent!")

                if doc_count==3:
                    requests.post(f'https://api.telegram.org/bot{reporter}/sendMessage?chat_id={reported_to_chat_id}&text=sheet2_report👆\
                    \n{track_likes} total likes from sheet2!\n{track_share} total share from sheet2!\n{track_comment} total comment from sheet2!')
                    requests.post(f'https://api.telegram.org/bot{reporter}/sendMessage?chat_id={reported_to_chat_id}&text=➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖')

                    requests.post(f'https://api.telegram.org/bot{reporter}/sendMessage?chat_id={reporter_amin_chat_id}&text=sheet2_report_succesfully_sent💪🏿\
                         \n{track_likes} total likes from sheet2!\n{track_share} total share from sheet2!\n{track_comment} total comment from sheet2!')
                    requests.post(f'https://api.telegram.org/bot{reporter}/sendMessage?chat_id={reporter_hop_chat_id}&text=sheet2_report_succesfully_sent💪🏿\
                     \n{track_likes} total likes from sheet2!\n{track_share} total share from sheet2!\n{track_comment} total comment from sheet2!')
                     
            else:
                print("couldnt send report ")


console = Console()     #to print to terminal
delay = random.randint(3, 6)

global tooken,reporter,reported_to_chat_id,reporter_amin_chat_id,reporter_hop_chat_id
tooken=os.getenv('bot_tooken')
reporter=os.getenv('reporter_bot')
reported_to_chat_id=os.getenv('reported_to')
reporter_amin_chat_id=os.getenv('reporter_amin')
reporter_hop_chat_id=os.getenv('reporter_hop')

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
button_start.place(x=370,y=600)


button_stop = customtkinter.CTkButton(master=window, 
    font=('Arial',13,'bold'), 
    fg_color=('#516fad'), 
    text='Stop',command=stop)
button_stop.place(x=620,y=600)

button_default = customtkinter.CTkButton(master=window, 
    font=('Arial',13,'bold'), 
    fg_color=('#516fad'), 
    text='Set default',command=default)
button_default.place(x=70,y=600)



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
progress.place(x =370,
            y = 678)

#like progress bar
l = ttk.Style()           
l.theme_use('clam')
l.configure("red.Horizontal.TProgressbar", 
    foreground='#d4d4d4', 
    background='#297d4e')
like_progress = Progressbar(window, 
    style="red.Horizontal.TProgressbar", 
    orient = HORIZONTAL,
    length = 20, 
    mode = 'determinate')
like_progress.place(x =370,y = 400)

# share  progress bar
sh = ttk.Style()           
sh.theme_use('clam')
sh.configure("red.Horizontal.TProgressbar", 
    foreground='#d4d4d4', 
    background='#297d4e')
share_progress = Progressbar(window, 
    style="red.Horizontal.TProgressbar", 
    orient = HORIZONTAL,
    length = 20, 
    mode = 'determinate')
share_progress.place(x =370,y = 450)

# comment progress bar
c = ttk.Style()           
c.theme_use('clam')
c.configure("red.Horizontal.TProgressbar", 
    foreground='#d4d4d4', 
    background='#297d4e')
comment_progress = Progressbar(window, 
    style="red.Horizontal.TProgressbar", 
    orient = HORIZONTAL,
    length = 20, 
    mode = 'determinate')
comment_progress.place(x =370,y = 500)





#taskbar description bottom
display_progress = StringVar()
display_progress.set("")
Label(window,
    font=('Arial',8),
    text = display_progress.get(), 
    textvariable = display_progress).place(x =520,y = 680)

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
Checkbutton(window, text = " Like",
					variable = lik, ##516fad
                    font=("Arial",9,'bold'),
                    fg="#5c0013",
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 10).place(x=27,y=350)
global shar
shar = IntVar()
shar.set(1)
Checkbutton(window, text = " Share",
					variable = shar, ##516fad
                    font=("Arial",9,'bold'),
                    fg="#5c0013",
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 10).place(x=30,y=400)
global coment
coment = IntVar()
coment.set(0)
Checkbutton(window, text = " Comment",
					variable = coment, ##516fad
                    font=("Arial",9,'bold'),
                    fg="#5c0013",
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 10).place(x=42,y=450)


global account_from_googlesheet
account_from_googlesheet = IntVar()
account_from_googlesheet.set(1)
Checkbutton(window, text = " Read account from googlesheet",
					variable = account_from_googlesheet,
                    font=("Arial",9,'bold'),
                    fg="#5c0013",
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 29).place(x=38,y=500)
global show_browser
show_browser = IntVar()
show_browser.set(0)
Checkbutton(window, text = " Show browser",
					variable = show_browser, ##516fad
                    font=("Arial",9,'bold'),
                    fg="#5c0013",
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 11).place(x=160,y=350)
global Ring_bell
Ring_bell = IntVar()
Ring_bell.set(1)
Checkbutton(window, text = " Ring bell",
					variable = Ring_bell,
                    font=("Arial",9,'bold'),
                    fg="#5c0013",
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 10).place(x=150,y=400)

global Read_from_bot
Read_from_bot = IntVar()
Read_from_bot.set(1)
Checkbutton(window, text = " Read link from bot",
					variable = Read_from_bot,
                    font=("Arial",9,'bold'),
                    fg="#5c0013",
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 15).place(x=160,y=450)
global send_report
send_report = IntVar()
send_report.set(1)
Checkbutton(window, text = " Send report",
					variable = send_report,
                    font=("Arial",9,'bold'),
                    fg="#5c0013",
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 15).place(x=30,y=550)


#current account_counter

scan_user_image=Image.open('pictures/contact2.png')
sized_scan_user_image=scan_user_image.resize((25, 25))
display_sized_scan_user_image=ImageTk.PhotoImage(sized_scan_user_image)
scan_user_label = Label(image=display_sized_scan_user_image)
scan_user_label.place(x=450,y=312)
display_scaned_username = StringVar()
display_scaned_username.set("")
Label(window,
    font=('Arial',15,'bold'),
    fg='#1a3f5c',
    text = display_scaned_username.get(), 
    textvariable = display_scaned_username).place(x =500,y = 312)

global total_like
total_like=0

global total_share
total_share=0

global total_coment
total_coment=0

# current account_counter
account_counter = StringVar()
account_counter.set(f"")
Label(window,
    fg='#3b5998',
    font="Arial 9 bold ",
    text = account_counter.get(), 
    textvariable = account_counter).place(x =445,y = 338)

#total like
Label(window,
    fg='#3b5998',
    font="Arial 12 bold",
    text = 'Like: ', 
    ).place(x =400,y = 400)
like_count = StringVar()
like_count.set(0)
Label(window,
    fg='#3b5998',
    font="Arial 12 bold ",
    text = like_count.get(), 
    textvariable = like_count).place(x =450,y = 400)

#total Share
Label(window,
    fg='#3b5998',
    font="Arial 12 bold",
    text = 'Share: ', 
    ).place(x =400,y = 450)
share_count = StringVar()
share_count.set(0)
Label(window,
    fg='#3b5998',
    font="Arial 12 bold ",
    text = share_count.get(), 
    textvariable = share_count).place(x =460,y = 450)

#Comment
Label(window,
    fg='#3b5998',
    font="Arial 12 bold",
    text = 'Comment: ', 
    ).place(x =400,y = 500)
comment_count = StringVar()
comment_count.set(0)
Label(window,
    fg='#3b5998',
    font="Arial 12 bold ",
    text = comment_count.get(), 
    textvariable = comment_count).place(x =490,y = 500)



global disabled_counter
disabled_counter=0

global failed_counter
failed_counter=0

global paswd_fail_counter
paswd_fail_counter=0

#total Disabled accounts
Label(window,
    fg='#3b5998',
    font="Arial 12 bold",
    text = 'Disabled accounts: ', 
    ).place(x =600,y = 400)
disabled_account_count = StringVar()
disabled_account_count.set(0)
Label(window,
    fg='#3b5998',
    font="Arial 12 bold ",
    text = disabled_account_count.get(), 
    textvariable = disabled_account_count).place(x =750,y = 400)

#total Failed accounts
Label(window,
    fg='#3b5998',
    font="Arial 12 bold",
    text = 'Failed accounts: ', 
    ).place(x =600,y = 450)
failed_account_count = StringVar()
failed_account_count.set(0)
Label(window,
    fg='#3b5998',
    font="Arial 12 bold ",
    text = failed_account_count.get(), 
    textvariable = failed_account_count).place(x =750,y = 450)

#total password fail accounts
Label(window,
    fg='#3b5998',
    font="Arial 12 bold",
    text = 'Password fail: ', 
    ).place(x =600,y = 500)
paswd_fail_accounts_count = StringVar()
paswd_fail_accounts_count.set("0")
Label(window,
    fg='#3b5998',
    font="Arial 12 bold ",
    text = paswd_fail_accounts_count.get(), 
    textvariable = paswd_fail_accounts_count).place(x =750,y = 500)




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


