from tkinter import *

window = Tk()
window.geometry("620x820")
window.title("tomiii")
# icon=PhotoImage(file='./pic/botdog.png')
# window.iconphoto(True,icon)
window.config(background="#D4D4D4")


# #Label
# photo=PhotoImage(file='./pic/Selenium_log.png')
# label=Label(window,# text='Selenium',font=('Arial',40,'bold'),# bg='green',# bd='20',
#              padx='40',pady='40',relief=RAISED,image=photo,compound='bottom',)
# # label.config(text='selenium')...we can also give the atributes like this
# label.pack()




# #Buttons
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


# #entry widget (Submiting text)
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




# #check button with integer variable...we can also use string...
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




# # Radiobuttons
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




# #scale
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







# listbox--is selectable list

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




# # messagebox
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




# #color chooser
# def click():
#   color=colorchooser.askcolor()
#   print(color)
#   hex=color[1]
#   window.config(bg=hex)

# from tkinter import colorchooser
# button4=Button(text='clickme',command=click)
# button4.pack()



#textarea
# def submit():
#     input=text.get("1.0",END)
#     print(input)

# text= Text(window)
# text.pack()

# button5=Button(window,text='submit',command=submit)
# button5.pack()



#filedialogue
from tkinter import filedialog

def openfile():   
    filepath=filedialog.askopenfilename(initialdir="/home/tomas/Documents/GitHub/Python-GUI/requirments.txt",title="open file",filetypes=((("text files","*.txt"),("all files","*.*"))))    
    file=open(filepath,'r')
    print(file.read())
    file.close

button6=Button(text='open',command=openfile)
button6.pack()











window.mainloop()
