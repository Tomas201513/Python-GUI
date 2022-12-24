# import tkinter as tk

# root = tk.Tk()
# #root.geometry('300x300')

# txt = 'Sample Text'

# lbl = tk.Label(root, font='Bell 36 bold', width=len(txt))
# lbl.pack(pady=5)

# def animate_label(text, n=0):
#     if n < len(text)-1:
#         # not complete yet, schedule next run one second later
#         lbl.after(1000, animate_label, text, n+1)
#     # update the text of the label
#     lbl['text'] = text[:n+1]

# # start the "after loop" one second later
# root.after(1000, animate_label, txt)
# root.mainloop()


import tkinter as tk
from tkinter import *
my_w = tk.Tk()
my_w.geometry("300x150")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title

sb1 = Spinbox(my_w, from_= 0, to = 10,width=5)
sb1.grid(row=1,column=1,padx=20,pady=20)

my_list=['One', 'Two', 'Three', 'Four', 'Five']
sb2 = Spinbox(my_w,values=my_list,width=10)
sb2.grid(row=1,column=2,padx=20,pady=20)

my_w.mainloop()  # Keep the window open
