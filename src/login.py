# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 16:34:43 2021

@author: andrea.zammarchi3
"""

from tkinter import *
from PIL import Image, ImageTk
import json

screen_width = 350
screen_height = 500

blue = '#259bca'
red = '#bf404c'
light_red = '#f2b5bb'

w = Tk()
w.geometry('350x500')
w.title('Clinica Zammarchi Login')
w.iconbitmap('web/images/logo.ico')

w.resizable(0,0)

Frame(w, width = screen_width, height = screen_height, bg = blue).place(x = 0, y = 0)
Frame(w, width = 250, height = 400, bg = 'white').place(x = 50, y = 50)

#label and textbox for username
l1 = Label(w, text = 'Username', bg = 'white')
l = ('consolas', 13)
l1.config(font = 1)
l1.place(x = 80, y = 200)
e1 = Entry(w, width = 20, border = 1)
e1.config(font = l)
e1.place(x = 80, y = 230)

#label and textbox for username
l2 = Label(w, text = 'Password', bg = 'white')
l = ('consolas', 13)
l2.config(font = 1)
l2.place(x = 80, y = 280)
e2 = Entry(w, width = 20, border = 1, show = '*')
e2.config(font = l)
e2.place(x = 80, y = 310)

imagea=Image.open("web/images/log.png")
imageb= ImageTk.PhotoImage(imagea)

label1 = Label(image=imageb,
               border=0,
               
               justify=CENTER)


label1.place(x=115, y=50)

###############################
def login(usr):
    uN = e1.get()
    pW = e2.get()

    if uN in usr.keys():
        if pW == usr[uN]:
            print("Welcome back.")
        else:
            print("Incorrect password.")
            return
    else:
        print("Hello, new person.")
        usr[uN] = pW

    writeUsers(usr)
    return

def readUsers():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def writeUsers(usr):
    with open("users.json", "w") as f:
            json.dump(usr, f)
def cmd():
    users = readUsers()
    login(users)
        
###############################

def btn(x, y, text, ecolor, lcolor):
    def on_entera(e):
        myButton1['background'] = ecolor
        myButton1['foreground']= lcolor
        
    def on_leavea(e):
        myButton1['background'] = lcolor
        myButton1['foreground']= ecolor
        
    myButton1 = Button(w,text=text,
                   width=20,
                   height=2,
                   fg=ecolor,
                   border=0,
                   bg=lcolor,
                   activeforeground=lcolor,
                   activebackground=ecolor,
                       command=cmd)
    
    myButton1.bind("<Enter>", on_entera)
    myButton1.bind("<Leave>", on_leavea)

    myButton1.place(x=x,y=y)
    
btn(100,375,'LOGIN',light_red,red)

w.mainloop()