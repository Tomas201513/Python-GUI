from tkinter import *
window = Tk()
window.geometry("620x820")
window.title("new post flag")
window.config(background="#D4D4D4")
from tkinter import filedialog

def savefile():
  file=filedialog.asksaveasfile(defaultextension='.txt',initialdir='/home/amin/Documents/GitHub/Python-GUI'
                        ,filetypes=[("Text file",".txtx"),("HTML file",".html"),("All file",".*")])
  if file is None:
    return
  filetxt=txt.get(1.0,END)
  file.write(filetxt)
  file.close()

def openfile():
    filepath=filedialog.askopenfilename(title="open file",filetypes=((("text files","*.txt"),("all files","*.*"))))    
    file=open(filepath,'r')
    print(file.read())
    txt.insert('1.0', file.read())

    file.close
    
txt=Text(window)
txt.pack()

button7=Button(text='open',command=openfile)
button7.pack()
button7=Button(text='save',command=savefile)
button7.pack()


window.mainloop()