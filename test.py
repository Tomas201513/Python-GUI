from tkinter import *
from tkinter.ttk import * # gives us extra widgets
# windows 🖼️
window = Tk()
window.geometry("620x820")
window.title("tomiii")
# icon=PhotoImage(file='./pic/botdog.png')
# window.iconphoto(True,icon)
window.config(background="#D4D4D4")


# #labels 🏷️
# photo=PhotoImage(file='./pic/Selenium_log.png')
# label=Label(window,# text='Selenium',font=('Arial',40,'bold'),# bg='green',# bd='20',
#              padx='40',pady='40',relief=RAISED,image=photo,compound='bottom',)
# # label.config(text='selenium')...we can also give the atributes like this
# label.pack()




# #buttons 🛎️
# count=0
# def click():
#     global count
#     count+=1
#     x="😊"
#     print(x*count)
# photo=PhotoImage(file='./pic/click.png')
# button=Button(window,text='click here!',command=click,font=("Comic Sana",30),fg="#053E11",bd="5",
#                     activebackground="#457D8C",activeforeground="black",state=ACTIVE,image=photo,)
# button.pack()


# #entry ⌨️ (Submiting text)
# def submit():
#     name=entry.get()
#     print("hellow "+name )
#     entry.config(state=DISABLED) #to disable after value submited

# def delete():
#     entry.delete(0,END)
    
# def backspace():
#     entry.delete(len(entry.get())-1,END)

# entry=Entry(window,font=("Arial",20),fg="blue",bg='white',show='😊')
# entry.pack(side=LEFT)

# submit_button=Button(window,text="submit",command=submit)
# submit_button.pack(side=RIGHT)

# delete_button=Button(window,text="delete",command=delete)
# delete_button.pack(side=RIGHT)

# backspace_button=Button(window,text="backspace",command=backspace)
# backspace_button.pack(side=RIGHT)




# # checkbutton ✔️ with integer variable...we can also use string...
# # def display():
# #     if (x.get()==1):
# #         print("🥳")
# #     else:
# #         print("🤢")
# # x=IntVar()
# # check=Checkbutton(window,text='agree',variable=x,onvalue=1,offvalue=0,command=display)#fg='',bd='',font='' .......we can customize
# # check.pack()


# #check  with boolean
# def display():
#     if (x.get()):
#         print("🥳")
#     else:
#         print("🤢")
# x=BooleanVar()
# check=Checkbutton(window,text='agree',variable=x,onvalue=True,offvalue=False,command=display)#fg='',bd='',font='' .......we can customize
# check.pack()




# # radiobuttons 🔘
# phone=["samsung","iphone",'nokia']

# def order():
#     print("you ordered "+phone[x.get()])
       
# # pic1=PhotoImage(file='')
# # pic2=PhotoImage(file='')
# # pic3=PhotoImage(file='')
# # phoneimages=['pic1','pic1','pic1']
# x=IntVar()
# for i in range(len(phone)):
#     radio=Radiobutton(window,
#                     text=phone[i],#delete the texts
#                     variable=x,#group radiobuttons together
#                     value=i,#assign radiobuttons different value
#                     # image=phoneimages[i],
#                     command=order,
#                     indicatoron=0, #to remove the little radio circle
#                     ) 
#     radio.pack(anchor=W)




# #scale 🌡️
# def submit():
#     print(f"temprature is {scale.get()}")
# scale=Scale(window,from_=150,to=0,length=300,font=('console',10),orient=VERTICAL,
#                 tickinterval=10,
#                 # showvalue=0,
#                 resolution=1,
#                 troughcolor='#69EAFF',
#                 )
# scale.set(scale['from']/2)
# scale.pack()

# button3=Button(window,text='submit',command=submit)
# button3.pack()







# #listbox 📋--is selectable list

# #listbox add/remove single value
# def submit1():
#     print(listbox.curselection())
# def add():
#     listbox.insert(listbox.size(),entrybox.get())
#     listbox.config(height=listbox.size())
# def delete():
#     listbox.delete(listbox.curselection())
#     listbox.config(height=listbox.size())


# #listbox add/remove multiple value
# def submit1():
#     phone=[]
#     for i in listbox.curselection():
#         phone.insert(i,listbox.get(i))
#     for i in phone:
#         print(i)

# def add():
#     listbox.insert(listbox.size(),entrybox.get())
#     listbox.config(height=listbox.size())
    
# def delete():
#     for i in reversed(listbox.curselection()):
#         listbox.delete(i)
#         listbox.config(height=listbox.size())


# listbox=Listbox(window,selectmode=MULTIPLE)
# listbox.insert(1,"nokia")
# listbox.insert(2,"samsung")
# listbox.insert(3,"iphone")

# listbox.config(height=listbox.size())
# listbox.pack()

# submit_button2=Button(window,text='submit',command=submit1)
# submit_button2.pack()

# entrybox=Entry(window)
# entrybox.pack()

# add=Button(window,text='add',command=add)
# add.pack()

# delete=Button(window,text='delete',command=delete)
# delete.pack()




# # messagebox 💭
# from tkinter import messagebox

# def click():
#     messagebox.showinfo(title='tom messagebox',message='hi')
   
#     messagebox.showwarning(title='warning!',message="i warn you")
   
#     while(True):
#         messagebox.showwarning(title='warning!',message="i warn you")

#     if messagebox.askokcancel(title='ask ok cancil',message='are you sure'):
#         print('ok')
#     else:
#         print('cancil')

#     if messagebox.askretrycancel(title='ask ok cancil',message='are you sure'):
#         print('retry')
#     else:
#         print('cancil')

#     if messagebox.askyesno(title='ask ok cancil',message='do u code?',icon='warning'):
#         print('yes')
#     else:
#         print('no')

#     ans=messagebox.askyesno(title='ask ok cancil',message='do u code?',icon='info')
#     if(ans=='yes'):
#         print('do stng here')
#     else:
#         print('do stng here')

#     print(messagebox.askyesnocancel(title='ask ok cancil',message='do u code?',icon='error'))


# button=Button(window,command=click,text='click me')
# button.pack()




# # colorchooser 🎨
# def click():
#   color=colorchooser.askcolor()
#   print(color)
#   hex=color[1]
#   window.config(bg=hex)

# from tkinter import colorchooser
# button4=Button(text='clickme',command=click)
# button4.pack()



## text area 📒
# def submit():
#     input=text.get("1.0",END)
#     print(input)

# text= Text(window)
# text.pack()

# button5=Button(window,text='submit',command=submit)
# button5.pack()



# # filedialog open 📁
# from tkinter import filedialog

# def openfile():   
#     filepath=filedialog.askopenfilename(initialdir="/home/tomas/Documents/GitHub/Python-GUI/requirments.txt",title="open file",filetypes=((("text files","*.txt"),("all files","*.*"))))    
#     file=open(filepath,'r')
#     print(file.read())
#     file.close

# button6=Button(text='open',command=openfile)
# button6.pack()



# # filedialog save 💾
# from tkinter import filedialog
# def savefile():
#   file=filedialog.asksaveasfile(defaultextension='.txt',initialdir='/home/amin/Documents/GitHub/Python-GUI'
#                         ,filetypes=[("Text file",".txtx"),("HTML file",".html"),("All file",".*")])
#   if file is None:
#     return
#   filetxt=txt.get(1.0,END)
# #   filetxt=input("enter some text ") #to get txt from console
#   file.write(filetxt)
#   file.close()
  
# button7=Button(text='save',command=savefile)
# button7.pack()
# txt=Text(window)
# txt.pack()



# # menubar 🧾

# def openfile():
#     pass

# def savefile():
#     pass

# def cut():
#     pass

# def copy():
#     pass

# def pest():
#     pass


# menubar=Menu(window,)
# window.config(menu=menubar)

# filrmenu=Menu(menubar,tearoff=0)
# menubar.add_cascade(label='file',menu=filrmenu)
# filrmenu.add_command(label='open',command=openfile)
# filrmenu.add_separator()
# filrmenu.add_command(label='save',command=savefile)
# filrmenu.add_command(label='exit',command=quit,image=PhotoImage(file='./pic/quit.png'))


# editmenu=Menu(menubar,tearoff=0)
# menubar.add_cascade(label='edit',menu=editmenu)
# editmenu.add_command(label='cut',command=cut)
# editmenu.add_separator()
# editmenu.add_command(label='copy',command=copy)
# editmenu.add_command(label='pest',command=pest)



# #frames 🗃️
# frame=Frame(window,bg='pink')
# frame.pack()

# buton1=Button(frame,text='N',font=('console',25),width=3)
# buton1.pack(side=TOP)
# buton2=Button(frame,text='w',font=('console',25),width=3)
# buton2.pack(side=LEFT)
# buton3=Button(frame,text='e',font=('console',25),width=3)
# buton3.pack(side=RIGHT)
# buton1=Button(frame,text='s',font=('console',25),width=3)
# buton1.pack(side=BOTTOM)



# # open new window 
# def createnewwindow():
#     # newwindow=Tk() #independant window
#     newwindow=Toplevel() #dependant window
#     window.destroy() #delete the main window

# butt=Button(window,text='create new window',command=createnewwindow)
# butt.pack()




# # window tabs 📑

# notebook=Notebook(window)
# tab1=Frame(notebook)
# tab2=Frame(notebook)

# notebook.add(tab1,text='Tab 1')
# notebook.add(tab2,text='Tab 2')
# notebook.pack(expand=True,fill='both')

# Label(tab1,text='hi',width=25,height=25).pack()
# Label(tab2,text='bye',width=25,height=25).pack()



# #grid geometry manager 🏢--think it as raw & column
# Label(window,text='title',font=("arial",25)).grid(row=0,column=0,columnspan=2)

# lable=Label(window,text='name',width=50,bg='pink')
# lable.grid(row=1,column=0)
# namentr=Entry(window,)
# namentr.grid(row=1,column=1)

# lable=Label(window,text='email',width=25,bg='pink')
# lable.grid(row=2,column=0)
# namentr=Entry(window)
# namentr.grid(row=2,column=1)

# butt=Button(window,text='submit')
# butt.grid(row=3,column=0,columnspan=2)#span makes it like in between columns




# # progressbar 📊
# import time
# def start():
#     GB=100
#     download=0
#     speed=1
#     while(download<GB):
#         time.sleep(0.05)
#         bar['value']+=(speed/GB)*100
#         download+=speed
#         percent.set(f"{int(((download/GB)*100))} %")
#         text.set(f"{str(download)}/{str(GB)} GB completed")
#         window.update_idletasks()

# percent=StringVar()
# text=StringVar()
# bar=Progressbar(window,orient=HORIZONTAL,length=300)
# bar.pack(pady=10)
# percentlable=Label(window,textvariable=percent)
# percentlable.pack()
# textlable=Label(window,textvariable=text)
# textlable.pack()
# butt=Button(window,text='download',command=start)
# butt.pack()




# # canvas 🎨  to draw graphes,plots,images

# canvas=Canvas(window,height=500,width=500)
# canvas.create_line(0,0,500,500,fill='blue',width='5') #top left corner is 0,0
# canvas.create_line(0,500,500,0,fill='red',width='5')
# canvas.create_rectangle(200,50,300,300)

# points=[250,200,400,400,100,400]
# canvas.create_polygon(points,fill='yellow', outline='black',width=5)
# canvas.create_arc(0,0,200,200,fill='pink', style=PIESLICE,start=90,extent=180)
# canvas.pack()



# key events ⌨️

# # window.bind(event,function)
# def dosmtg(event):
#     print("you did a thing!")
# window.bind("<Key>",dosmtg)


#key event that display what key is pressed
# def dosmtg(event):
#     label.config(text=event.keysym)
# window.bind("<Key>",dosmtg)

# label=Label(window,font=("Helvertica",100))
# label.pack()



# #mouse events 🖱️
# def dosmtg(event):
#     print(f" mouse coordinates {str(event.x)},{str(event.x)}")
# window.bind("<Button-1>",dosmtg)#left mouse clock
# window.bind("<Button-2>",dosmtg)#scroll wheel
# window.bind("<Button-3>",dosmtg)#right mouse click
# window.bind("<ButtonRelease>",dosmtg)#display when we release button
# window.bind("<Enter>",dosmtg)#when we pressv enter key 
# window.bind("<Leave>",dosmtg)# display coordinate as soon as we leave the window
# window.bind("<Motion>",dosmtg)#where the mouse moving



# # drag & drop 👈
# def drag_start(event):
#     widget=event.widget
#     widget.startX=event.x
#     widget.startY=event.x
# def drag_motion(event):
#     widget=event.widget
#     x=widget.winfo_x()-widget.startX+event.x
#     y=widget.winfo_y()-widget.startY+event.y
#     widget.place(x=x,y=y)

# label=Label(window,background="green",width=10)
# label.place(x=0,y=0)
# label.bind("<Button-1>",drag_start)
# label.bind("<B1-Motion>",drag_motion)

# label2=Label(window,background="yellow",width=10)
# label2.place(x=0,y=20)
# label2.bind("<Button-1>",drag_start)
# label2.bind("<B1-Motion>",drag_motion)


# move images 🏎️
def move_up():
    label.place(x=label.winfo_x(),y=label.winfo_y()-1)
    
# def move_down():
#     label.place(x=label.winfo_x(),y=label.winfo_y()-1)

# def move_left():
#     label.place(x=label.winfo_x(),y=label.winfo_y()-1)

# def move_right():
#     label.place(x=label.winfo_x(),y=label.winfo_y()-1)

window.geometry("500x500")
window.bind("<u>",move_up)
# window.bind("<u>",move_down)
# window.bind("<u>",move_left)
# window.bind("<u>",move_right)

# myimage=PhotoImage(file='pic/q.png')
label=Label(window,text="lol")
label.place(x=0,y=0)


# animations 🛸
# multiple animations 🎞️
# clock program 🕒














window.mainloop()
