# import tkinter, time
# from subprocess import Popen

# Freq = 2500
# Dur = 150

# top = tkinter.Tk()
# top.title('MapAwareness')
# top.geometry('200x100') # Size 200, 200

# def start():
#     import os
# #    os.system("python test.py")
#     Popen(["python", "t.py"])


# def stop():
#     print ("Stop")
#     top.destroy()

# startButton = tkinter.Button(top, height=2, width=20, text ="Start", 
# command = start)
# stopButton = tkinter.Button(top, height=2, width=20, text ="Stop", 
# command = stop)

# startButton.pack()
# stopButton.pack()
# top.mainloop()

from tkinter import *
from threading import Thread
import time

def scanning():
    while True:
        print ("hello")
        if stop == 1:   
            break   #Break while loop when stop = 1

def start_thread():
    # Assign global variable and initialize value
    global stop
    stop = 0

    # Create and launch a thread 
    t = Thread (target = scanning)
    t.start()
    time.sleep()


def stop():
    # Assign global variable and set value to stop
    global stop
    stop = 1

root = Tk()
root.title("Title")
root.geometry("500x500")

app = Frame(root)
app.grid()

start = Button(app, text="Start Scan",command=start_thread)
stop = Button(app, text="Stop",command=stop)

start.grid()
stop.grid()

root.mainloop()