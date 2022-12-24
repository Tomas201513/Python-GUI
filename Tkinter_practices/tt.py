# from tkinter import *
# root=Tk()
# root.overrideredirect(True) # turns off title bar, geometry
# root.geometry('400x100+200+200') # set new geometry

# # make a frame for the title bar
# title_bar = Frame(root, bg='#2e2e2e', relief='raised', bd=2,highlightthickness=0)

# # put a close button on the title bar
# close_button = Button(title_bar, text='X', command=root.destroy,bg="#2e2e2e",padx=2,pady=2,activebackground='red',bd=0,font="bold",fg='white',highlightthickness=0)

# # a canvas for the main area of the window
# window = Canvas(root, bg='#2e2e2e',highlightthickness=0)

# # pack the widgets
# title_bar.pack(expand=1, fill=X)
# close_button.pack(side=RIGHT)
# window.pack(expand=1, fill=BOTH)
# xwin=None
# ywin=None
# # bind title bar motion to the move window function

# def move_window(event):
#     root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))
# def change_on_hovering(event):
#     global close_button
#     close_button['bg']='red'
# def return_to_normalstate(event):
#     global close_button
#     close_button['bg']='#2e2e2e'


# title_bar.bind('<B1-Motion>', move_window)
# close_button.bind('<Enter>',change_on_hovering)
# close_button.bind('<Leave>',return_to_normalstate)
# root.mainloop()

# from tkinter import *
# from webbrowser import *

# root=Tk()
# root.overrideredirect(True) # turns off title bar, geometry
# root.geometry('400x100+200+200') # set new geometry
# root.attributes('-topmost', True)

# lastClickX = 0
# lastClickY = 0

# def SaveLastClickPos(event):
#     global lastClickX, lastClickY
#     lastClickX = event.x
#     lastClickY = event.y

# def Dragging(event):
#     x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
#     root.geometry("+%s+%s" % (x , y))

# # make a frame for the title bar
# title_bar = Frame(root, bg='#2e2e2e', relief='raised', bd=2,highlightthickness=0)

# # put a close button on the title bar
# close_button = Button(title_bar, text='X', command=root.destroy,bg="#2e2e2e",padx=2,pady=2,activebackground='red',bd=0,font="bold",fg='white',highlightthickness=0)

# window = Canvas(root, bg='#2e2e2e',highlightthickness=0)

# # pack the widgets
# title_bar.pack(expand=1, fill=X)
# close_button.pack(side=RIGHT)
# window.pack(expand=1, fill=BOTH)

# title_bar.bind('<Button-1>', SaveLastClickPos)
# title_bar.bind('<B1-Motion>', Dragging)
# root.mainloop()

import requests

try:

    url="https://api.callmebot.com/start.php?user=@Tomas201513&text=There+is+a+link+from+muferihat"
    requests.get(url)
    print("done")
except:
    print("fail")

