#Build Weather App
from tkinter import *
import requests
import json
import matplotlib.pyplot as plt
import math 

root=Tk()
root.title("Weather Forecast")

def LookUp():
    global dlbl,tlbl,rlbl,clbl,minlbl,maxlbl,sunriselbl,sunsetlbl,date,time,region,country,mini,maxi,sunrise,sunset
    '''global tlbl
    global rlbl
    global clbl
    global minlbl
    global maxlbl
    global avglbl
    global sunriselbl
    global sunsetlbl
    global date
    global time
    global region
    global country
    global mini
    global maxi

    global sunrise 
    global sunset'''
    
    
    
    #Requesting API
    
    api_request=requests.get("https://api.weatherapi.com/v1/forecast.json?key=095c610ce26c429e87870327210601&q="+Area.get()+"&days=1")
    api=json.loads(api_request.content)
    
    #
    
    
    #Filtering out the required fields from the json file

    date=(api["forecast"]["forecastday"][0]["date"])
    time=((api["location"]["localtime"]).split())[1]
    region=(api["location"]["region"])
    country=(api["location"]["country"])
    mini=(api["forecast"]["forecastday"][0]["day"]["mintemp_c"])
    maxi=(api["forecast"]["forecastday"][0]["day"]["maxtemp_c"])
    avg=(api["forecast"]["forecastday"][0]["day"]["avgtemp_c"])
    sunrise=(api["forecast"]["forecastday"][0]["astro"]["sunrise"])
    sunset=(api["forecast"]["forecastday"][0]["astro"]["sunset"])
    currtemp=(api["current"]["temp_c"])
    #Creating name Labels
    d_lbl=Label(root,text="Date:").grid(row=1,column=0)
    t_lbl=Label(root,text="Time:").grid(row=2,column=0)
    r_lbl=Label(root,text="Region:").grid(row=3,column=0)
    c_lbl=Label(root,text="Country:").grid(row=4,column=0)
    min_lbl=Label(root,text="min temp(in C):").grid(row=5,column=0)
    max_lbl=Label(root,text="max temp (in C):").grid(row=6,column=0)
    avg_lbl=Label(root,text="avg temp:").grid(row=7,column=0)
    curr_lbl=Label(root,text="current temp(in C):").grid(row=8,column=0)
    sunrise_lbl=Label(root,text="Sunrise:").grid(row=9,column=0)
    sunset_lbl=Label(root,text="Sunset:").grid(row=10,column=0)
    search=Label(root,text="Search Region:").grid(row=0,column=0)

    #Putting Vallue in the corresponding name Labels
    dlbl=Label(root,text=date).grid(row=1,column=1)
    tlbl=Label(root,text=time).grid(row=2,column=1)
    rlbl=Label(root,text=region).grid(row=3,column=1)
    clbl=Label(root,text=country).grid(row=4,column=1)
    minlbl=Label(root,text=mini).grid(row=5,column=1)
    maxlbl=Label(root,text=maxi).grid(row=6,column=1)
    avglbl=Label(root,text=avg).grid(row=7,column=1)
    sunriselbl=Label(root,text=sunrise).grid(row=9,column=1)
    sunsetlbl=Label(root,text=sunset).grid(row=10,column=1)
    currlbl=Label(root,text=currtemp).grid(row=8,column=1)

def ChangeText():
        dlbl=Label(root,text="                                                            ").grid(row=1,column=1)
        tlbl=Label(root,text="                                                            ").grid(row=2,column=1)
        rlbl=Label(root,text="                                                            ").grid(row=3,column=1)
        clbl=Label(root,text="                                                            ").grid(row=4,column=1)
        minlbl=Label(root,text="                                                            ").grid(row=5,column=1)
        maxlbl=Label(root,text="                                                            ").grid(row=6,column=1)
        avglbl=Label(root,text="                                                            ").grid(row=7,column=1)
        sunriselbl=Label(root,text="                                                            ").grid(row=9,column=1)
        sunsetlbl=Label(root,text="                                                            ").grid(row=10,column=1)
        currlbl=Label(root,text="                                                            ").grid(row=8,column=1)

        Area.delete(0,END)

def graph():
    maxdata=[]
    mindata=[]
    avgdata=[]
    api_request=requests.get("https://api.weatherapi.com/v1/forecast.json?key=095c610ce26c429e87870327210601&q="+Area.get()+"&days=3")
    api=json.loads(api_request.content)
    for ii in range(3):
        maxdata=maxdata+[api["forecast"]["forecastday"][ii]["day"]["maxtemp_c"]]
        mindata=mindata+[api["forecast"]["forecastday"][ii]["day"]["mintemp_c"]]
        avgdata=avgdata+[api["forecast"]["forecastday"][ii]["day"]["avgtemp_c"]]
        
    xaxis=[api["forecast"]["forecastday"][0]["date"],api["forecast"]["forecastday"][1]["date"],api["forecast"]["forecastday"][2]["date"]]
    plt.plot(xaxis,maxdata,'r-',label="maximum temperature")
    plt.plot(xaxis,mindata,'b-',label="minimum temperature")
    plt.plot(xaxis,avgdata,'g-',label="average temperature")
    plt.xlabel("day")
    plt.ylabel("temperature")
    plt.legend()
    plt.show()
        
def newt():
    global days
    global dayslbl
    global new
    new=Tk()
    new.title("weather forecast data")
    trend_btn=Button(new,text="Show Trend for the next 3 days",command=graph).grid(row=1,column=0,columnspan=2,ipadx=30)
    new.mainloop()
    


    
    
    




    





    
Area =Entry(root,width=40,borderwidth=5)
Area.grid(row=0,column=1)
btn=Button(root,text="Search",command=LookUp).grid(row=11,column=0,columnspan=2,ipadx=100)
reset_btn=Button(root,text="Reset",command=ChangeText).grid(row=12,column=0,columnspan=2,ipadx=104)
graph_btn=Button(root,text="Click to Graph the forecast",command=newt).grid(row=13,column=0,columnspan=2,ipadx=48)


root.mainloop()

