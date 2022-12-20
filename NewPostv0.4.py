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
from playsound import playsound


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


   with console.status("[bold yellow] Searching New Post . . .") as status:
    display2.set("Scaning started!")

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
                By.CLASS_NAME, "x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1heor9g.xt0b8zv.xo1l8bm")
              try:
                name = driver.find_element(
                  By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]/h2[1]/span[1]/a[1]/strong[1]/span[1]")
              except:
                name = driver.find_element(
                  By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]/h2[1]/span[1]/a[1]/strong[1]/span[1]")
              

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
               
                if sttime == "Just now" or sttime == "1m" or sttime == "2m" or sttime == "1 m" or sttime == "2 m" or \
                   sttime == "3m" or sttime == "4m"or sttime == "3 m" or sttime == "4 m":

                      links = [elem.get_attribute('href') for elem in times]
                      newlink=links[0]

                      with open('./links/file.txt','r') as f:
                        lastlink=f.readlines()[-1]
                        if newlink!=lastlink:                          
                          try: 
                              print("Here is New Link -->   ",str(newlink))                                
                    
                            
                              with open("./links/file.txt", 'a+') as f:
           
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
                             
                              display5.set(f"{fbname} at {current_clock}")
                              playsound('alarm/a1.wav') #alarm
                              print('alarm!')

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

                              if stop == 1:   #⛔
                                clean()
                                break

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
    
    global stop
    stop = 1
    display2.set("Stoping in less than 10 seconds..")
    
def clean():

  display3.set("")
  display4.set("")
  display5.set("")
  display6.set("")
  progress['value'] = 0
  window.update_idletasks()
  display2.set("Stoped!")
  sleep(3)
  display2.set("")


def save():

  fn=entry.get()
  print(fn)
  f = open(fn, "w")
  filetxt=txt.get(1.0,END)
  f.write(filetxt)
  f.close()
  txt.delete('1.0', END)
  entry.delete(0, END)
  display1.set("saved!")


def Name(name):

    s = display3.get()
    s = f"{name} "
    display3.set(s)

def lastpost(sttime):

    s = display4.get()
    s = f"{sttime}"
    display4.set(s)


# def linkfound(fbname,newlink):
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     s += f"\n{fbname} at\n {current_time}"
#     display5.set(s)
#     display6.set(f"{newlink} ")

        

def openfile():

    filepath=filedialog.askopenfilename(title="open file",filetypes=((("all files","*.*"),("text files","*.txt"))))    
    file=open(filepath,'r')
    filename=os.path.basename(file.name)
    entry.delete(0, END)
    entry.insert(0,filename)
    txt.insert('1.0',str(file.read()) )
    file.close
    display1.set("opened")

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



s=' '
Label(window, text='New Feeed Notifier',fg='#3b5998',font=('Arial',35,'bold'),
             compound='bottom',).pack()

from PIL import Image, ImageTk
WIDTH=56
HEIGHT=53
xVelocity=0.00005    #0.009
yVelocity=0
canvas=Canvas(window,width=WIDTH,height=HEIGHT)
canvas.place(x=355,y=1)    #x=0
image=Image.open('pic/fb1.png')
sizedimg=image.resize((50, 50))
pic=ImageTk.PhotoImage(sizedimg)
myimage=canvas.create_image(2,2,image=pic,anchor=NW)


txt=scrolledtext.ScrolledText(window,width= 110, height= 10)
txt.place(x=10,y=70)
# txt.focus_set()
entry=Entry(window, width= 25)
entry.place(x=350,y=245)
display1 = StringVar()
display1.set("")
Label(window,font=('Arial',9),text = display1.get(), textvariable = display1).place(x = 300,y = 249) #595
# Label(window,font=('Arial',9),text = display1.get(), textvariable = display1).place(x = 428,y = 268)


import customtkinter
customtkinter.set_appearance_mode("System")
# customtkinter.set_default_color_theme("blue")
button6 = customtkinter.CTkButton(master=window,font=('Arial',10,'bold'), fg_color=('#516fad'),height= 0.4, width=0.8, text='Clear',command=clear)
button6.place(x=560,y=249)

button7 = customtkinter.CTkButton(master=window,font=('Arial',13,'bold'),  fg_color=('#516fad'), text='Open',command=openfile)
button7.place(x=280,y=300)

button8 = customtkinter.CTkButton(master=window,font=('Arial',13,'bold'),  fg_color=('#516fad'), text='Save',command=save)
button8.place(x=500,y=300)

button7 = customtkinter.CTkButton(master=window, font=('Arial',13,'bold'),  fg_color=('#516fad'),text='Start',command=start_thread)
button7.place(x=280,y=380)

button8 = customtkinter.CTkButton(master=window, font=('Arial',13,'bold'), fg_color=('#516fad'), text='Stop',command=stop)
button8.place(x=500,y=380)


s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='#d4d4d4', background='#297d4e')
progress = Progressbar(window, style="red.Horizontal.TProgressbar", orient = HORIZONTAL,length = 140, mode = 'determinate')
progress.place(x =385,y = 698)



display2 = StringVar()
display2.set("")
Label(window,font=('Arial',8),text = display2.get(), textvariable = display2).place(x =538,y = 700)
# 542 385



images=Image.open('pic/sp3.png')
sizedimgs=images.resize((35, 35))
pics=ImageTk.PhotoImage(sizedimgs)
varun_labels = Label(image=pics)
varun_labels.place(x=10,y=490)
display3 = StringVar()
display3.set("")
lbl3=Label(window,font=('Arial',15,'bold'),fg='#ee4e2e',text = display3.get(), textvariable = display3).place(x =70,y = 495)


imaget=Image.open('pic/dt.png')
sizedimgt=imaget.resize((40, 40))
pict=ImageTk.PhotoImage(sizedimgt)
varun_labelt = Label(image=pict)
varun_labelt.place(x=10,y=534)
display4 = StringVar()
display4.set("")
lbl4=Label(window,font=('Arial',15,'bold'),fg='#ee4e2e',text = display4.get(), textvariable = display4).place(x =70,y = 540)


imagep=Image.open('pic/bs1.png')
sizedimgp=imagep.resize((40, 40))
picp=ImageTk.PhotoImage(sizedimgp)
varun_labelp = Label(image=picp)
varun_labelp.place(x=10,y=595)
display5 = StringVar()
display5.set("")
Label(window,fg='#1a3f5c',font=('Arial',13,'bold'),text = display5.get(), textvariable = display5).place(x =70,y = 605)



# ee4e2e   orange
# 1a3f5c   blue


display6 = StringVar()
display6.set("")
Label(window,fg='#1a3f5c',font=('Arial',10),text = display6.get(), textvariable = display6).place(x =0,y = 680)

time_lable=Label(window,fg='#1a3f5c',font=("Arial",30,'bold'))
time_lable.place(x =660,y = 500)
day_lable=Label(window,fg='#1a3f5c',font=("Arial",20,'bold'))
day_lable.place(x =660,y = 550)
date_lable=Label(window,fg='#1a3f5c',font=("Arial",20,'bold'))
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