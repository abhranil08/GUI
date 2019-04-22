# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:48:43 2019

@author: Abhranil
"""
HEIGHT=700
WIDTH=900
import tkinter as tk
import PIL
import requests
from pytube import YouTube
import datetime


    
def downloadVideo(youtube,path):
    #path=r"C:\Users\Abhranil\Desktop" 
    stream = youtube.streams.filter(progressive=True).first()
    #path = r
    stream.download(path)
    print("Downloading done..")
    
def designPage(youtube):
    try:
        title = "Title : " + str(youtube.title)
        length = "Length of the video : " + str(datetime.timedelta(seconds=int(youtube.length)))
        outputString = title + '\n' + length + '\n' + "Downloaded Video.."
    except:
        outputString = "No data received."
    return outputString

def getVideoDetails(url,path):
    try:
        youtube = YouTube(url)
        downloadVideo(youtube,path)
        label['text'] = "Fetching Video details and Downloading.. \n\n"+designPage(youtube)
    except:
        print("Wrong URL! ")
    
    

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

from PIL import ImageTk, Image

image = Image.open("photo1.png")
backgroundImage = ImageTk.PhotoImage(image)
backgroundImageLabel = tk.Label(root, image = backgroundImage)
backgroundImageLabel.image=image
backgroundImageLabel.place(relheight=1, relwidth=1)

frame = tk.Frame(root,bg='#FA8072',bd=10)
frame.place(relx=0.5,rely=0.1,relheight=0.1,relwidth=0.75,anchor='n')

button = tk.Button(frame,text="Copy, Paste URL & Click Here",font = ('Courier',12),wraplength=200,anchor='w', justify='left', padx=2,command= lambda: getVideoDetails(entry.get(),entry1.get()))
button.place(relwidth=0.3,relheight=1)

entry = tk.Entry(frame,font = ('Courier',20))
entry.place(relx=0.32,relwidth=0.68,relheight=1)




middleframe = tk.Frame(root,bg='#FA8072',bd=10)
middleframe.place(relx=0.5,rely=0.3,relheight=0.1,relwidth=0.75,anchor='n')

button1 = tk.Button(middleframe,text="Download Path",font = ('Courier',12),wraplength=200,anchor='w', justify='left', padx=2,command= lambda: getVideoDetails(entry.get()))
button1.place(relwidth=0.3,relheight=1)

entry1 = tk.Entry(middleframe,font = ('Courier',20))
entry1.place(relx=0.32,relwidth=0.68,relheight=1)




lowerframe1 = tk.Frame(root,bg='#FA8072',bd=15)
lowerframe1.place(relx=0.5,rely=0.5,relheight=0.3,relwidth=0.75,anchor='n')

label = tk.Label(lowerframe1,font = ('Courier',18),wraplength=650,anchor='w', justify='left')
label.place(relheight=1,relwidth=1)

#entry = tk.Entry(frame,text="Enter text",bg="green")
#entry.pack(side='left',expand=True,fill='both')

root.mainloop()




