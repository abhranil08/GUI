# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:48:43 2019

@author: Abhranil
"""
HEIGHT=700
WIDTH=700
import tkinter as tk
import PIL
import requests


#api key = 4e518e9db0089f2e66c82f4b8fb931d6
#api call = api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

def test1(s):
    print("Your entry : "+s)
    
def getFinalWeather (weather):
    try:
        cityName = ("Name of city: "+ str(weather['name']))
        tempVal = ("Temperature : "+ str(weather['main']['temp']))
        maxTemp = ("Maximum Temperature : "+ str(weather['main']['temp_max']))
        minTemp = ("Minimum Temperature : "+ str(weather['main']['temp_min']))
        humidTemp = ("Humidity : "+ str(weather['main']['humidity']))
        weatherCond = ("Weather condition :" + (weather['weather'][0]['description']))
        outputString = cityName + '\n' + tempVal + '\n' + maxTemp + '\n' + minTemp + '\n' + humidTemp + '\n' + weatherCond
    except:
        outputString = "No data recieved"
    return outputString

def getWeather(city):
    api_key = "4e518e9db0089f2e66c82f4b8fb931d6"
    api_url = "https://api.openweathermap.org/data/2.5/weather"
    params = { 'APPID' :api_key , 'q' : city, "units":"imperial"}
    response = requests.get(api_url,params=params)
    weather = (response.json())
    label['text'] = getFinalWeather(weather)
    
    
    

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

from PIL import ImageTk, Image

image = Image.open("photo.png")
backgroundImage = ImageTk.PhotoImage(image)
backgroundImageLabel = tk.Label(root, image = backgroundImage)
backgroundImageLabel.image=image
backgroundImageLabel.place(relheight=1, relwidth=1)

frame = tk.Frame(root,bg='#80c1ff',bd=10)
frame.place(relx=0.5,rely=0.1,relheight=0.1,relwidth=0.75,anchor='n')

entry = tk.Entry(frame,font = ('Modern',20))
entry.place(relwidth=0.65,relheight=1)

button = tk.Button(frame,text="Get Weather",font = ('Modern',20),command= lambda: getWeather(entry.get()))
button.place(relx=0.7,relwidth=0.3,relheight=1)


frame1 = tk.Frame(root,bg='#80c1ff',bd=15)
frame1.place(relx=0.5,rely=0.5,relheight=0.4,relwidth=0.75,anchor='n')

label = tk.Label(frame1,font = ('Modern',20))
label.place(relheight=1,relwidth=1)

#entry = tk.Entry(frame,text="Enter text",bg="green")
#entry.pack(side='left',expand=True,fill='both')

root.mainloop()




