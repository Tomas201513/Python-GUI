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
# window.attributes('-alpha',0.2)
# window.overrideredirect(1)


def scanning():
  
    for i in range(0,100000000000000000000000000000):

      if stop == 1:#⛔
        clean()
        break

      if connect():

        try:
          print('initializing...')
          display_progress.set("initializing...")
          progress['value'] = 25
          window.update_idletasks()

          converted_list = []
          
          with open('./links/fb_pages.txt', 'r') as file:
              lines_next = file.readlines()
              for element in lines_next:
                    converted_list.append(element.strip())
          x = len((lines_next))

          chrome_options = Options()
          prefs = {"profile.default_content_setting_values.geolocation": 2}
          chrome_options.add_experimental_option("prefs", prefs)
          chrome_options.add_argument("--disable-infobars")
          chrome_options.add_argument("--start-maximized")
          chrome_options.add_argument("--disable-notifications")
          chrome_options.add_argument("--disable-popup-blocking")
          chrome_options.add_argument("--incognito")
          

          if show_browser.get()==0:
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            print("browser not visible")
          else:
            print("visible browser")

          progress['value'] = 50
          window.update_idletasks()
          
          driver = webdriver.Chrome(
            service=Service(
                ChromeDriverManager().install())
                , options=chrome_options)
          sleep(delay)
          y = x-1
          for _ in range(1, x):
              driver.execute_script("window.open('');")
          
              if stop == 1:   #⛔
                  clean()
                  break

          progress['value'] = 75
          window.update_idletasks()

          for i in range(x):
              driver.switch_to.window(driver.window_handles[i])
              sleep(10)
              driver.get(converted_list[i])
              if stop == 1:   #⛔
                clean()
                break
              sleep(delay)
              
          progress['value'] = 100
          window.update_idletasks()
          progress['value'] = 100
          display_scaned_username.set(" ·  ·  ·")
          display_release_datetime.set(" ·  ·  ·")


          with console.status("[bold yellow] Searching New Post . . .") as status:
            display_progress.set("Scaning started!")

            while True:

                  if stop == 1:   #⛔
                    clean()
                    break
                  sleep(10)
                  
                  for i in range(x):
                      driver.switch_to.window(
                        driver.window_handles[i])

                      sleep(delay)
                      if stop == 1:   #⛔
                        clean()
                        break
                      driver.refresh()
                      sleep(delay)
                      times = driver.find_elements(
                        By.CLASS_NAME, "x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.\
                            x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.\
                                xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz\
                                    .x1heor9g.xt0b8zv.xo1l8bm")
                      try:
                        name = driver.find_element(
                          By.XPATH, 
                          "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]\
                            /div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]\
                                /div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]\
                                    /div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]\
                                        /div[1]/div[1]/span[1]/h2[1]/span[1]/a[1]/strong[1]/span[1]")
                      except:
                        name = driver.find_element(
                          By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]\
                            /div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]\
                                /div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]\
                                    /div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]\
                                        /div[2]/div[1]/div[1]/span[1]/h2[1]/span[1]/a[1]/strong[1]/span[1]")
                      

                      for ttime in times:
                        
                        body_elem = driver.find_element(
                              By.TAG_NAME, 'body')
                        body_elem.send_keys(Keys.ARROW_DOWN)
                        if stop == 1:   #⛔
                          clean()
                          break
                        sleep(delay)
                        body_elem.send_keys(Keys.ARROW_UP)
                        if stop == 1:   #⛔
                          clean()
                          break
                        sleep(delay)
                        sttime = ttime.text
                        print(sttime)
                        fbname=name.text
                        Name(fbname)
                        lastpost(sttime)

                        if stop == 1:   #⛔
                          clean()
                          break
                        sleep(delay)
                        if stop == 1:   #⛔
                          clean()
                          break
                      
                        if sttime == "Just now" or sttime == "1m" or sttime == "2m" or\
                             sttime == "1 m" or sttime == "2 m" or sttime == "3m" or\
                                 sttime == "4m"or sttime == "3 m" or sttime == "4 m" or sttime == "5m":

                              links = [elem.get_attribute('href') for elem in times]
                              newlink=links[0]
                              display_new_post.set(" ·  ·  ·")

                              with open('./links/link_found_by_bot.txt','r') as f:
                                lastlink=f.readlines()[-1]
                                if newlink!=lastlink:                          
                                  notify_telegram_bot(fbname,newlink)
                        else:
                          pass
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


def notify_telegram_bot(fbname,newlink):
    try: 
        print("Here is New Link -->   ",str(newlink))                                
    
        with open("./links/link_found_by_bot.txt", 'a+') as f:

            f.writelines("\n")
            f.writelines(
                    "New Post on " + newlink)

        current_time = datetime.datetime.now().strftime(
                      "Post Date : %Y/%m/%d" + '\n' + '\n' + "Post Time : %I:%M:%S")

        current_clock = datetime.datetime.now().strftime("%I:%M:%S")
        try:

            s =s+fbname+'\n'
            print(s)
        except:
         pass
    
        display_new_post.set(f"{fbname} at {current_clock}")
        
        ring() #bell

        message_body = str(current_time) + '\n' + \
        "Here Is The Link  \N{thumbs up sign}   :" + \
        '\n' + str(newlink)

        bot_token = '5698535655:AAGfcd8MAvLMCZzgWEp7_2ZEiPCtsMgxzMs'
        bot_chatID = '395490182'
    
        try:    
            url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&text={message_body}"
            requests.post(url)
            print('send!')

        except:
            print('unable to send /check the bot')

        # if stop == 1:#⛔
        #  clean()
        #  break

    except:
        pass


def ring():
     try:
        if Ring_bell.get()==1:
            playsound('alarm/a1.wav') #alarm
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
    t = Thread (target = scanning)
    t.start()
    


def stop():
    ''' Used to stop the thread that run the scanning'''

    global stop
    stop = 1
    display_progress.set("Stoping in less than 10 seconds..")
    display_scaned_username.set(" ·  ·  ·")
    display_release_datetime.set(" ·  ·  ·")
    
def clean():
  ''' Used to clean all label txt and progress bar .....called when pressing stop button'''

  display_scaned_username.set("")
  display_release_datetime.set("")
  display_new_post.set("")
  progress['value'] = 0
  window.update_idletasks()
  display_progress.set("Stoped!")
  sleep(3)
  display_progress.set("")


def save():
  '''used to save the updated file using dialogu box.....called pressing save button '''

  fn=entry.get()
  print(fn)
  f = open(fn, "w")
  filetxt=scrolledtext_box.get(1.0,END)
  f.write(filetxt)
  f.close()
  scrolledtext_box.delete('1.0', END)
  entry.delete(0, END)
  file_status_label.set("saved!")


def Name(name):
    ''' Used to display name of scanned fb page'''

    s = display_scaned_username.get()
    s = f"{name} "
    display_scaned_username.set(s)

def lastpost(sttime):
    ''' Used to display last post date of scanned fb page'''

    s = display_release_datetime.get()
    s = f"{sttime}"
    display_release_datetime.set(s)


# def linkfound(fbname,newlink):
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     s += f"\n{fbname} at\n {current_time}"
#     display_new_post.set(s)
#     display6.set(f"{newlink} ")

        

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


def timeupdate():
    ''' Used to display current date time....it time round 24 hour it will clear last send link label'''

    time_string=strftime("%I:%M:%S %p")
    time_lable.config(text=time_string)
    
    if time_string=='12:00:01 AM':
      display_new_post.set("")

    date_string=strftime("%B %d, %Y")
    date_lable.config(text=date_string)

    day_string=strftime("%A")
    day_lable.config(text=day_string)

    window.after(1000,timeupdate) #update each minute

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





console = Console()     #to print to terminal

delay = random.randint(3, 6)

Label(window, 
    text='New Feeed Notifier',
    fg='#3b5998',
    font=('Arial',35,'bold'),
    compound='bottom',).pack()      #the big title

#the f logo and motion 
WIDTH=56
HEIGHT=53
xVelocity=0.00005    #0.009
yVelocity=0
canvas=Canvas(window,
    width=WIDTH,
    height=HEIGHT)
canvas.place(x=355,y=1)    
fb_image=Image.open('pictures/fb_logo.png')
sized_fb_image=fb_image.resize((50, 50))
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
entry.place(x=350,y=245)

#label that show status of file opened/saved...
file_status_label = StringVar()
file_status_label.set("")
Label(window,
    font=('Arial',9),
    text = file_status_label.get(), 
    textvariable = file_status_label).place(x = 300,y = 249) 


customtkinter.set_appearance_mode("System")
# customtkinter.set_default_color_theme("blue")
button_clear = customtkinter.CTkButton(master=window,
    font=('Arial',10,'bold'), 
    fg_color=('#516fad'),
    height= 0.4, 
    width=0.8, 
    text='Clear',
    command=clear)
button_clear.place(x=560,y=249)  


button_open = customtkinter.CTkButton(master=window,
    font=('Arial',13,'bold'),  
    fg_color=('#516fad'), 
    text='Open',
    command=openfile)
button_open.place(x=280,y=300)


button_save = customtkinter.CTkButton(master=window,
    font=('Arial',13,'bold'),  
    fg_color=('#516fad'), 
    text='Save',
    command=save)
button_save.place(x=500,y=300)


button_start = customtkinter.CTkButton(master=window, 
    font=('Arial',13,'bold'),  
    fg_color=('#516fad'),
    text='Start',
    command=start_thread)
button_start.place(x=280,y=380)


button_stop = customtkinter.CTkButton(master=window, 
    font=('Arial',13,'bold'), 
    fg_color=('#516fad'), 
    text='Stop',command=stop)
button_stop.place(x=500,y=380)

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
            y = 698)


#taskbar description bottom
display_progress = StringVar()
display_progress.set("")
Label(window,
    font=('Arial',8),
    text = display_progress.get(), 
    textvariable = display_progress).place(x =538,y = 700)

#No internet label  
connection_status = StringVar()
connection_status.set("")
Label(window,
    font=('Arial',11),
    text = connection_status.get(), 
    textvariable = connection_status).place(x =420,y = 500)

#scanning image and label
scan_user_image=Image.open('pictures/scan_user.png')
sized_scan_user_image=scan_user_image.resize((25, 25))
display_sized_scan_user_image=ImageTk.PhotoImage(sized_scan_user_image)
scan_user_label = Label(image=display_sized_scan_user_image)
scan_user_label.place(x=15,y=495)
display_scaned_username = StringVar()
display_scaned_username.set("")
Label(window,
    font=('Arial',15,'bold'),
    fg='#ee4e2e',
    text = display_scaned_username.get(), 
    textvariable = display_scaned_username).place(x =70,y = 495)

# date image and labele that show date and time  of the post
datetime_image=Image.open('pictures/datetime.png')
sized_datetime_image=datetime_image.resize((30, 30))
display_sized_datetime_image=ImageTk.PhotoImage(sized_datetime_image)
datetime_label = Label(image=display_sized_datetime_image)
datetime_label.place(x=15,y=538)
display_release_datetime = StringVar()
display_release_datetime.set("")
lbl4=Label(window,
    font=('Arial',15,'bold'),
    fg='#ee4e2e',
    text = display_release_datetime.get(), 
    textvariable = display_release_datetime).place(x =70,y = 540)

#bell image and label that show new post 
bell_image=Image.open('pictures/bell.png')
sized_bell_image=bell_image.resize((32, 32))
display_sized_bell_image=ImageTk.PhotoImage(sized_bell_image)
bell_label = Label(image=display_sized_bell_image)
bell_label.place(x=12,y=595)
display_new_post = StringVar()
display_new_post.set("")
Label(window,
    fg='#1a3f5c',
    font=('Arial',13,'bold'),
    text = display_new_post.get(), 
    textvariable = display_new_post).place(x =70,y = 605)

#label that show present date and time 
time_lable=Label(window,
    fg='#1a3f5c',
    font=("Arial",30,'bold'))
time_lable.place(x =660,y = 500)

day_lable=Label(window,
    fg='#1a3f5c',
    font=("Arial",20,'bold'))
day_lable.place(x =660,y = 550)

date_lable=Label(window,
    fg='#1a3f5c',
    font=("Arial",20,'bold'))
date_lable.place(x =660,y = 585)

timeupdate()


#menubar/taskbar
menubar = Menu(window,fg='#1a3f5c')

#setting
setting_images=Image.open('pictures/setting.png')
sized_setting_image=setting_images.resize((12, 12))
display_setting_image=ImageTk.PhotoImage(sized_setting_image)

global show_browser
show_browser = IntVar()

global Ring_bell
Ring_bell = IntVar()  
Ring_bell.set(1)
show_not_done = BooleanVar()
view_menu = Menu(menubar, 
    tearoff=0, 
    fg = '#3c5998')
view_menu.add_checkbutton(label="Show browser",
    font=("Arial",8,'bold'), 
    onvalue=1, 
    offvalue=0, 
    variable=show_browser)
view_menu.add_checkbutton(label="Notification bell",
    font=("Arial",8,'bold'), 
    onvalue=1, 
    offvalue=0, 
    variable=Ring_bell)
menubar.add_cascade(label='Edit',
    font=("Arial",9,'bold'), 
    menu=view_menu,
    image=display_setting_image)
window.config(menu=menubar)

#help ⋮
help_image=Image.open('pictures/help.png')
sized_help_image=help_image.resize((12, 12))
display_help_image=ImageTk.PhotoImage(sized_help_image)
view_info = Menu(menubar, 
    tearoff=0, 
    fg = '#3c5998')
view_info.add_command(label='Demo',
    font=("Arial",8,'bold'),
    command=play_video)
view_info.add_command(label='Contact',
                font=("Arial",8,'bold'))
menubar.add_cascade(label='Help',
            font=("Arial",9,'bold'),
            menu=view_info,
            image=display_help_image)
window.config(menu=menubar)


window.protocol("WM_DELETE_WINDOW",close)
window.mainloop()




##value up and down aim to create level up and down sleep time
# current_value = StringVar(value=0)
# spin_box = Spinbox(window,from_=0,to=5,textvariable=current_value,wrap=True)
# spin_box.place(x=10,y=600)