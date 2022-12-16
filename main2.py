import time
import random
import requests
import datetime
import pyfiglet
from rich import print
from rich.console import Console
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
import psycopg2

def Run():
   pass

def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['id'])
    e2.insert(0,select['username'])
    e3.insert(0,select['userpagelink'])
    e4.insert(0,select['timexpath'])
 
def Add():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()
 
    conn=psycopg2.connect(database="employee_crud", user='root', password='root', host='127.0.0.1', port= '5432')
    cursor = conn.cursor()
 
    try:
       sql = "INSERT INTO  users (id,username,userpagelink,timexpath) VALUES (%s, %s, %s, %s)"
       val = (studid,studname,coursename,feee)
       cursor.execute(sql, val)
       conn.commit()
       lastid = cursor.lastrowid
       messagebox.showinfo("information", "inserted successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()
    except Exception as e:
       print(e)
       conn.rollback()
       conn.close()
 
def update():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()
    conn=psycopg2.connect(database="employee_crud", user='root', password='root', host='127.0.0.1', port= '5432')
    cursor=conn.cursor()
 
    try:
       sql = "Update  users set username= %s,userpagelink= %s,timexpath= %s where id= %s"
       val = (studname,coursename,feee,studid)
       cursor.execute(sql, val)
       conn.commit()
       lastid = cursor.lastrowid
       messagebox.showinfo("information", "Record Updateddddd successfully...")
 
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()
 
    except Exception as e:
 
       print(e)
       conn.rollback()
       conn.close()
 
def delete():
    studid = e1.get()
 
    conn=psycopg2.connect(database="employee_crud", user='root', password='root', host='127.0.0.1', port= '5432')
    cursor=conn.cursor()
 
    try:
       sql = "delete from users where id = %s"
       val = (studid,)
       cursor.execute(sql, val)
       conn.commit()
       lastid = cursor.lastrowid
       messagebox.showinfo("information", "Record Deleteeeee successfully...")
 
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()
    except Exception as e:
 
       print(e)
       conn.rollback()
       conn.close()

def show():
      conn = psycopg2.connect(database="employee_crud", user='root', password='root', host='127.0.0.1', port= '5432')
      cursor = conn.cursor()
      cursor.execute("SELECT id,username,userpagelink,timexpath FROM users")
      data = cursor.fetchall()
      print("Connection established to: ",data)

      for i, (w,x, y,z) in enumerate(data, start=1):
         listBox.insert("", "end", values=(w,x, y,z))
         conn.close()


root = Tk()
root.geometry("1200x700")
root.title("new post flag")
global e1
global e2
global e3
global e4
delay = random.randint(3, 6)
 
tk.Label(root, text="NEW POST FLAG", fg="#326791", font=('None', 30)).place(x=500, y=0)
 
tk.Label(root, text="ID").place(x=10, y=10)
Label(root, text="UserName").place(x=10, y=40)
Label(root, text="UserPageLink").place(x=10, y=70)
Label(root, text="TimeXPath").place(x=10, y=100)
 
e1 = Entry(root)
e1.place(x=140, y=10)
 
e2 = Entry(root)
e2.place(x=140, y=40)
 
e3 = Entry(root)
e3.place(x=140, y=70,width=650)
 
e4 = Entry(root)
e4.place(x=140, y=100,width=650)
 
Button(root, text="Add",command = Add,height=2, width= 13).place(x=250, y=140)
Button(root, text="update",command = update,height=2, width= 13).place(x=360, y=140)
Button(root, text="Delete",command = delete,height=2, width= 13).place(x=470, y=140)
 
cols = ('id', 'username', 'userpagelink','timexpath')
listBox = ttk.Treeview(root, columns=cols, show='headings' )
 
for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)
 
show()
listBox.bind('<Double-Button-1>',GetValue)


Button(root, text="Run",command = Run,bg='#cc823f',height=2, width= 13).place(x=360, y=600)
label=Label(root,font=('Arial',40,'bold'),bg='white',compound='bottom',).place(x=900, y=70)














root.mainloop()

