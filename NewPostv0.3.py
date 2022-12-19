#!/usr/bin/env python3 
import requests
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
from time import sleep
from tkinter import *
from mttkinter import mtTkinter
from tkinter import ttk
from tkinter.ttk import Progressbar
window = Tk()
window.geometry("920x720")
window.resizable(False,False)
window.title("new post flag")
window.config(background="#D4D4D4")
from tkinter import filedialog,scrolledtext
import os,time
from time import *
from threading import Thread


console = Console()
delay = random.randint(3, 6)

def scanning():
   print('initializing')
   display2.set("initializing...")

   progress['value'] = 25
   window.update_idletasks()

   converted_list = []

   with open('./links/flagpagelink.txt', 'r') as file:
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
   chrome_options.add_argument('--headless')
   chrome_options.add_argument('--disable-gpu')
   
   progress['value'] = 50
   window.update_idletasks()
   
   driver = webdriver.Chrome(service=Service(
      ChromeDriverManager().install()), options=chrome_options)
   sleep(delay)
   y = x-1
   for _ in range(1, x):
      driver.execute_script("window.open('');")
      if stop == 1:   #⛔
        display3.set("")
        display4.set("")
        display2.set("Stoped!")
        break

   progress['value'] = 75
   window.update_idletasks()

   for i in range(x):
      driver.switch_to.window(driver.window_handles[i])
      sleep(10)
      driver.get(converted_list[i])
      if stop == 1:   #⛔
        display3.set("")
        display4.set("")
        display2.set("Stoped!")
        break
      sleep(delay)
      
   progress['value'] = 100
   window.update_idletasks()
   progress['value'] = 100


   with console.status("[bold yellow] Searching New Post . . .") as status:
    display2.set("Searching started!")

    while True:

          if stop == 1:   #⛔
             display3.set("")
             display4.set("")
             display2.set("Stoped!")
             break
          sleep(10)
          
          for i in range(x):
              driver.switch_to.window(
                driver.window_handles[i])

              sleep(delay)
              if stop == 1:   #⛔
                display3.set("")
                display4.set("")
                display2.set("Stoped!")
                break
              driver.refresh()
              sleep(delay)
              times = driver.find_elements(
                By.CLASS_NAME, "x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1heor9g.xt0b8zv.xo1l8bm")
              name = driver.find_element(
                By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]/h2[1]/span[1]/a[1]/strong[1]/span[1]")
              for ttime in times:
                
                body_elem = driver.find_element(
                      By.TAG_NAME, 'body')
                body_elem.send_keys(Keys.ARROW_DOWN)
                if stop == 1:   #⛔
                  display2.set("Stoped!")
                  display3.set("")
                  display4.set("")
                  break
                sleep(delay)
                body_elem.send_keys(Keys.ARROW_UP)
                if stop == 1:   #⛔
                  display2.set("Stoped!")
                  display3.set("")
                  display4.set("")
                  break
                sleep(delay)
                sttime = ttime.text
                print(sttime)
              
                Name(name.text)
                lastpost(sttime)

                if stop == 1:   #⛔
                  display2.set("Stoped!")
                  display3.set("")
                  display4.set("")
                  break
                sleep(delay)
                if stop == 1:   #⛔
                  display2.set("Stoped!")
                  display3.set("")
                  display4.set("")
                  break

                if sttime == "Just now" or sttime == "1m" or sttime == "2m" or sttime == "1 m" or sttime == "2 m":
                      links = [elem.get_attribute(
                          'href') for elem in times]
                      newlink=links[0]
                      with open('./links/file.txt','r') as f:
                        lastlink=f.readlines()[-1]
                        if newlink!=lastlink:                          
                          try: 
                              print("Here is New Link -->   ",
                                    str(newlink))
                                    
                              linkfound(newlink)
                              display2.set("Here is New Link -->   ",
                                    str(newlink))

                              with open("./links/file.txt", 'a+') as f:
                                f.writelines("\n")
                                f.writelines(
                                      "New Post on " + newlink)
                              bot_token = '5270788758:AAF0N5nfEjlynElbiCuQwr-DZWJMsschP3w'
                              bot_chatID = '395490152'

                              current_time = datetime.datetime.now().strftime(
                                "Post Date : %Y/%m/%d" + '\n' + '\n' + "Post Time : %H:%M:%S")

                              message_body = str(current_time) + '\n' + \
                                "Here Is The Link  \N{thumbs up sign}   :" + \
                                '\n' + str(newlink)
                              send_text = 'https://api.telegram.org/bot' + bot_token + \
                                '/sendMessage?chat_id=' + bot_chatID + \
                                '&text=' + str(message_body)
                              if stop == 1:   #⛔
                                display3.set("")
                                display4.set("")
                                display2.set("Stoped!")
                                break
                              
                              try:
                                requests.post(send_text)
                                print("Bot Send Link --> ", str(newlink))
                              except:
                                print("No Link Found")
                                pass

                          except:
                              pass
                else:
                  pass

def start_thread():
    global stop
    stop = 0

    t = Thread (target = scanning)
    t.start()


def stop():
    progress['value'] = 0
    window.update_idletasks()
    global stop
    stop = 1
    display2.set("Stoping in less than 10 seconds..")

def save():
  fn=entry.get()
  print(fn)
  f = open(fn, "w")
  filetxt=txt.get(1.0,END)
  f.write(filetxt)
  f.close()
  txt.delete('1.0', END)
  display1.set("saved!")

def Name(name):
    s = display3.get()
    s = f"{name} "
    display3.set(s)

def lastpost(sttime):
    s = display4.get()
    s = f"{sttime} ago"
    display4.set(s)

def linkfound(name,newlink):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    s += f" Post from {name} at {current_time}\n:{newlink}\n"
    display5.set(s)


def openfile():
    filepath=filedialog.askopenfilename(title="open file",filetypes=((("all files","*.*"),("text files","*.txt"))))    
    file=open(filepath,'r')
    filename=os.path.basename(file.name)
    entry.delete(0, END)
    entry.insert(0,filename)
    txt.insert('1.0',str(file.read()) )
    file.close
    display1.set("file opened")

def timeupdate():
    time_string=strftime("%I:%M:%S %p")
    time_lable.config(text=time_string)
    if time_string=='12:00:01 AM':
      display5.set("")
    date_string=strftime("%B %d, %Y")
    date_lable.config(text=date_string)

    day_string=strftime("%A")
    day_lable.config(text=day_string)

    window.after(1000,timeupdate) #update each minute
def clear():
    txt.delete('1.0', END)
    entry.delete(0, END)
    display1.set("")



from PIL import Image, ImageTk
WIDTH=900
HEIGHT=55
xVelocity=0
yVelocity=0
canvas=Canvas(window,width=WIDTH,height=HEIGHT)
canvas.place(x=190,y=5)
image=Image.open('pic/xx.png')
sizedimg=image.resize((50, 50))
pic=ImageTk.PhotoImage(sizedimg)
myimage=canvas.create_image(2,2,image=pic,anchor=NW)



Label(window, text='New Feed Notifier',fg='#3b5998',font=('Arial',35,'bold'),
             compound='bottom',).pack()

txt=scrolledtext.ScrolledText(window,width= 110, height= 10)
txt.place(x=10,y=70)
# txt.focus_set()

entry=Entry(window, width= 25)
entry.place(x=350,y=245)
display1 = StringVar()
display1.set("")
Label(window,text = display1.get(), textvariable = display1).place(x = 410,y = 270)


import customtkinter
customtkinter.set_appearance_mode("System")
# customtkinter.set_default_color_theme("blue")
button6 = customtkinter.CTkButton(master=window,  fg_color=('#516fad'),height= 0.4, width=1, text='clear',command=clear)
button6.place(x=560,y=246)

button7 = customtkinter.CTkButton(master=window,  fg_color=('#516fad'), text='Open',command=openfile)
button7.place(x=280,y=300)

button8 = customtkinter.CTkButton(master=window,  fg_color=('#516fad'), text='Save',command=save)
button8.place(x=500,y=300)

button7 = customtkinter.CTkButton(master=window,   fg_color=('#516fad'),text='Start',command=start_thread)
button7.place(x=280,y=380)

button8 = customtkinter.CTkButton(master=window,  fg_color=('#516fad'), text='Stop',command=stop)
button8.place(x=500,y=380)


s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='#d4d4d4', background='green')
progress = Progressbar(window, style="red.Horizontal.TProgressbar", orient = HORIZONTAL,length = 150, mode = 'determinate')
progress.place(x =280,y = 430)

display2 = StringVar()
display2.set("")
Label(window,text = display2.get(), textvariable = display2).place(x =440,y = 430)




Label(window,font=('Arial',15),text="Scaning: ").place(x =10,y = 500)
display3 = StringVar()
display3.set("")
lbl3=Label(window,font=('Arial',15,'bold'),text = display3.get(), textvariable = display3).place(x =115,y = 500)

Label(window,font=('Arial',15),text="Last Post: ").place(x =10,y = 540)
display4 = StringVar()
display4.set("")
lbl4=Label(window,font=('Arial',15,'bold'),text = display4.get(), textvariable = display4).place(x =115,y = 540)

Label(window,font=('Arial',15),text="Found links: ").place(x =10,y = 590)
display5 = StringVar()
display5.set("")
Label(window,fg='#1a3f5c',font=('Arial',15),text = display5.get(), textvariable = display5).place(x =150,y = 590)

time_lable=Label(window,font=("Arial",30))
time_lable.place(x =660,y = 500)
day_lable=Label(window,font=("Arial",20))
day_lable.place(x =660,y = 550)
date_lable=Label(window,font=("Arial",20))
date_lable.place(x =660,y = 585)
timeupdate()

# current_value = StringVar(value=0)
# spin_box = Spinbox(window,from_=0,to=5,textvariable=current_value,wrap=True)
# spin_box.place(x=10,y=600)

image_width=pic.width()
image_height=pic.height()
while True:
    coordinate=canvas.coords(myimage)
    if(coordinate[0]>=WIDTH-image_width or coordinate[0]<0):
        xVelocity=-xVelocity
    if(coordinate[1]>=HEIGHT-image_height or coordinate[1]<0):
        yVelocity=-yVelocity
    canvas.move(myimage,xVelocity,yVelocity)
    window.update()




window.mainloop()