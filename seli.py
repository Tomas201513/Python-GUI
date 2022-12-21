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




# import tkinter as tk

# window = Tk()

# menubar = Menu(window)
# show_all = BooleanVar()
# show_all.set(True)
# show_done = BooleanVar()
# show_not_done = BooleanVar()

# view_menu = Menu(menubar)
# view_menu.add_checkbutton(label="Show All", onvalue=1, offvalue=0, variable=show_all)
# view_menu.add_checkbutton(label="Show Done", onvalue=1, offvalue=0, variable=show_done)
# view_menu.add_checkbutton(label="Show Not Done", onvalue=1, offvalue=0, variable=show_not_done)
# menubar.add_cascade(label='View', menu=view_menu)
# window.config(menu=menubar)
# print(show_all.get())

# window.mainloop()


# from playsound import playsound

# playsound('alarm/a1.wav')
# print('alarm!')


# # Import the required libraries
# from tkinter import *
# from tkinter import ttk

# # Create an instance of tkinter frame or window
# win = Tk()

# # Set the size of the window
# win.geometry("700x350")

# # Define a function to get the output for selected option
# def selection():
#    selected = "You selected the option " + str(radio.get())
#    label.config(text=selected)

# radio = IntVar()
# Label(text="Your Favourite programming language:", font=('Aerial 11')).pack()

# # Define radiobutton for each options
# r1 = Radiobutton(win, text="C++", variable=radio, value=1, command=selection)

# r1.pack(anchor=N)
# r2 = Radiobutton(win, text="Python", variable=radio, value=2, command=selection)

# r2.pack(anchor=N)
# r3 = Radiobutton(win, text="Java", variable=radio, value=3, command=selection)

# r3.pack(anchor=N)

# # Define a label widget
# label = Label(win)
# label.pack()

# win.mainloop()


# import tkinter as tk
# from tkVideoPlayer import TkinterVideo

# root = tk.Tk()

# videoplayer = TkinterVideo(master=root, scaled=True)
# videoplayer.load(r"videos/mosh.mp4")
# videoplayer.pack(expand=True, fill="both")

# videoplayer.play() # play the video

# root.mainloop()



# import pygame
# import random
# from pycollision import Collision

# pygame.init()

# screen = pygame.display.set_mode((1000, 800))

# player_rect = pygame.Rect(0, 0, 50, 50)

# collision_check = Collision(r"pic/d1.png", (15, 15), wall_collision=False) # set wall collision to True if you want to check the collision only at the walls, this will be much faster
# collision_object = pygame.image.load(r"pic/d1.png").convert_alpha()

# colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for x in
#           range(len(collision_check.collision_points()))]

# running = True
# speed = 1.5
# pos_x, pos_y = (10, 10)

# coll_font = pygame.font.SysFont('Consolas', 50)

# while running:

#     screen.fill((255, 255, 255))

#     for event in pygame.event.get():

#         if event.type == pygame.QUIT:
#             running = False

#     pos_x, pos_y = pygame.mouse.get_pos()

#     colliding, pos = collision_check.smart_check((pos_x, pos_y)) # checks if the point is first inside the outer rectangle then checks if it is inside the image
#     # rect = (player_rect.x, player_rect.y, player_rect.x+player_rect.width, player_rect.height+player_rect.y)
#     # colliding, pos = collision_check.rect_collide(rect)
#     if colliding:
#         screen.fill((255, 16, 8))
#         screen.blit(coll_font.render("Collision", True, (255, 255, 255)), (50, 50))

#     screen.blit(collision_object, (0, 0))

#     # for color, x in zip(colors, collision_check.collision_points()):  # uncomment this to get colourful rectangles
#     #     x = (x[0], x[1], x[2] - x[0], x[3] - x[1])
#     #     pygame.draw.rect(screen, color, pygame.Rect(x), width=3)

#     player_rect = pygame.Rect(pos_x, pos_y, 50, 50)
#     pygame.draw.rect(screen, (0, 0, 0), player_rect)

#     pygame.display.update()





# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
# from tkinter import *
# from tkinter.ttk import *

# # creates a Tk() object
# master = Tk()

# # sets the geometry of main
# # root window
# master.geometry("200x200")


# # function to open a new window
# # on a button click
# def openNewWindow():
	
# 	# Toplevel object which will
# 	# be treated as a new window
# 	newWindow = Toplevel(master)

# 	# sets the title of the
# 	# Toplevel widget
# 	newWindow.title("New Window")

# 	# sets the geometry of toplevel
# 	newWindow.geometry("200x200")

# 	# A Label widget to show in toplevel
# 	Label(newWindow,
# 		text ="This is a new window").pack()


# label = Label(master,
# 			text ="This is the main window")

# label.pack(pady = 10)

# # a button widget which will open a
# # new window on button click
# btn = Button(master,
# 			text ="Click to open a new window",
# 			command = openNewWindow)
# btn.pack(pady = 10)

# # mainloop, runs infinitely
# mainloop()


# import urllib.request
# def connect(host='http://google.com'):
#     try:
#         urllib.request.urlopen(host) #Python 3.x
#         return True
#     except:
#         return False
# # test
# print( "connected" if connect() else "no internet!" )

# Python program to test
# internet speed
  
# import speedtest  
  
  
# st = speedtest.Speedtest()
  
# option = int(input('''What speed do you want to test:  
  
# 1) Download Speed  
  
# 2) Upload Speed  
  
# 3) Ping 
  
# Your Choice: '''))
  
  
# if option == 1:  
  
#     print(st.download())  
  
# elif option == 2: 
  
#     print(st.upload())  
  
# elif option == 3:  
  
#     servernames =[]  
  
#     st.get_servers(servernames)  
  
#     print(st.results.ping)  
  
# else:
  
#     print("Please enter the correct choice !") 


# import speedtest module 
import speedtest

speed_test = speedtest.Speedtest()

def bytes_to_mb(bytes):
  KB = 1024 # One Kilobyte is 1024 bytes
  MB = KB * 1024 # One MB is 1024 KB
  return int(bytes/MB)

download_speed = bytes_to_mb(speed_test.download())
print("Your Download speed is", download_speed, "MB") 