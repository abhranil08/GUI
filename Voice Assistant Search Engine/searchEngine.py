# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 12:46:34 2019

@author: Abhranil
"""

import requests
import webbrowser
import tkinter as tk
from tkinter import ttk

def callback():
    webbrowser.open("https://www.google.com/search?q="+entry.get())
    
def EnterGet(event):
    webbrowser.open("https://www.google.com/search?q="+entry.get())
    
root = tk.Tk()
root.title("Search Bar")

canvas = tk.Canvas(root,height=50,width=1000)
canvas.pack()

frame = tk.Frame(root,bg='#FA8072')
frame.place(relx=0.1,rely=0.1,relheight=0.8,relwidth=0.8)

label = tk.Label(frame,text="Query",font=('Courier',15))
label.place(relwidth=0.2,relheight=1)

entry = tk.Entry(frame,font=('Courier',15))
entry.place(relx=0.2,relheight=1,relwidth=0.6)

button = tk.Button(frame,text='Search',font=('Courier',15),command=callback)
button.place(relx=0.7,relheight=1,relwidth=0.3)

entry.bind('<Return>',EnterGet)


root.mainloop()