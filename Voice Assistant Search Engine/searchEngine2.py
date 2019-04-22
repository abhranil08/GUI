# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 12:46:34 2019

@author: Abhranil
"""

import requests
import webbrowser
import tkinter as tk
from tkinter import ttk
from tkinter import *

def callback():
    if btn.get() == 'google':
        webbrowser.open("https://www.google.com/search?q="+entry.get())
    elif btn.get() == 'duck':
        webbrowser.open("https://www.duckduckgo.com/?q="+entry.get())
    
def EnterGet(event):
    if btn.get() == 'google':
        webbrowser.open("https://www.google.com/search?q="+entry.get())
    elif btn.get() == 'duck':
        webbrowser.open('http://duckduckgo.com/?q='+entry.get())
    
root = tk.Tk()
root.title("Search Bar")

btn = StringVar()


canvas = tk.Canvas(root,height=100,width=1000)
canvas.pack()

frame = tk.Frame(root,bg='#FA8072')
frame.place(relx=0.1,rely=0.1,relheight=0.8,relwidth=0.8)

label = tk.Label(frame,text="Query",font=('Courier',15))
label.place(relwidth=0.1,relheight=1)

entry = tk.Entry(frame,font=('Courier',15))
entry.place(relx=0.1,relheight=0.6,relwidth=0.6)

button = tk.Button(frame,text='Search',font=('Courier',15),command=callback)
button.place(relx=0.7,relheight=0.6,relwidth=0.3)

button2 = tk.Radiobutton(frame,text='Google',padx=20,value='google',font=('Courier',15),variable=btn,anchor='w')
button2.place(relx=0.1,rely=0.70,relheight=0.25)

button3 = tk.Radiobutton(frame,text='Duck',padx=20,value='duck',font=('Courier',15),variable=btn,anchor='e')
button3.place(relx=0.7,rely=0.70,relheight=0.25)

entry.bind('<Return>',EnterGet)
entry.focus()

root.wm_attributes('-topmost',1)

root.mainloop()