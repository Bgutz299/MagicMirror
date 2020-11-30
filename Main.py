#!/usr/bin/enb python
# -*- coding:utf-8 -*-

from guizero import App,Text,ButtonGroup,PushButton,TextBox,Drawing		#https://pypi.org/project/guizero/
from datetime import date, datetime
from time import sleep

#Weather 
import Weather
import date_time
import App_init

global app
app = App_init.app_init()

#Date and Time
##########################################################################################################################
today_date = date_time.date_get()
curr_time = date_time.time_get()
Date_display = Text(app, today_date, size=30, font="Century Gothic Bold", color="light gray", grid=[0,0],align="left")
Time_display = Text(app, curr_time, size=40, font="Century Gothic Bold", color="light gray", grid=[0,1],align="left")
def time_update():
    Time_display.value = date_time.time_get()
##########################################################################################################################

#Todo List
##########################################################################################################################
To_do_list_Title = Text(app, "To-do List:", size=20, color="light gray", grid=[0,2],align="left")

global Todolist
global Selectedlist
Todolist=[]
Selectedlist=[]

global Display_list
#Create List Function (Uses Button Group)
def create_list():
    global Display_list
    Display_list = ButtonGroup(app, options=Todolist, selected=Selectedlist, align="left", grid=[0,3])
    Display_list.text_color="light gray"
    Display_list.text_size=20
    Display_list.font="Century Gothic Bold"
#Create New list
create_list()

#Text box for typing
#########################################################################################################
Add_textbox=TextBox(app,grid=[0,4],width=30,align="left")
Add_textbox.text_size=12
Add_textbox.text_color="Black"
Add_textbox.font="Century Gothic Bold"
Add_textbox.bg="white"

#Add button and add function
#########################################################################################################
def addto_todolist():
    global Display_list
    global Todolist
    if(Add_textbox.value):
        Todolist.append(Add_textbox.value)
        Display_list.append(Add_textbox.value)
        print(Todolist)
        Add_textbox.clear()

Addbutton = PushButton(app, command=addto_todolist, text="Add", grid=[0,4], align="right")
Addbutton.text_color="Black"
Addbutton.bg="light gray"
Addbutton.font="Century Gothic Bold"
Addbutton.text_size="12"

#Delete from list Button
#########################################################################################################
def delfrom_todolist():
    global Display_list
    global Todolist
    if(Display_list.value_text != ""):
        Todolist.remove(Display_list.value_text)
        Display_list.remove(Display_list.value_text)
    print(Todolist)

Addbutton = PushButton(app, command=delfrom_todolist, text="Delete", grid=[1,4], align="left")
Addbutton.text_color="Black"
Addbutton.bg="light gray"
Addbutton.font="Century Gothic Bold"
Addbutton.text_size="12"

#Clear List function and button
#########################################################################################################
def clear_todolist():
    global Display_list
    global Todolist
    if(Todolist):
	    for i in Todolist:
	        Display_list.remove(i)
	    Display_list.destroy()
	    Todolist.clear()
	    create_list()
	    print(Todolist)
Clearbutton = PushButton(app, command=clear_todolist, text="Clear", grid=[0,5], align="left")
Clearbutton.text_color="Black"
Clearbutton.bg="light gray"
Clearbutton.font="Century Gothic Bold"
Clearbutton.text_size="12"

#########################################################################################################

#Weather Drawing
city_name = "Indio"
temp, temp_min, temp_high, description = Weather.fetchWeather(city_name)
#description = "mist"
Weather_drawing = Drawing(app,grid=[0,6],align="left",width=400,height=300)
#Weather_drawing.rectangle(0,0,1000,1000,"white")
def which_image(description):
    switcher ={
        "clear sky": "Clear_sky.png",
        "few clouds": "Cloudy_sky.png",
        "scattered clouds": "Scattered_clouds.png",
        "broken clouds": "Broken_clouds.png",
        "shower rain": "rain.png",
        "rain":"rain.png",
        "thunderstorm":"thunderstorm.png",
        "snow":"snow.png",
        "mist":"mist.png"
    }
    return switcher.get(description, "Clear_sky.png")
def which_color(description):
    switcher = {
        "clear sky": "black",
        "few clouds": "white",
        "scattered clouds": "black",
        "broken clouds": "white",
        "rain":"white",
        "shower rain": "white",
        "thunderstorm":"white",
        "snow":"white",
        "mist":"black"
    }
    return switcher.get(description, "black")
weather_font_color = which_color(description)
Image_picture = which_image(description)
#Image_picture = "Cloudy_sky.png"
#print(Image_picture)
Weather_drawing.image(0,0,image="Images/" + Image_picture, width=400,height=300)
city_num_x = 200 - (len(city_name)*10)
city_num_y = 0

Weather_drawing.text(city_num_x,city_num_y, text= city_name, color=weather_font_color,font="Arial",size=40)
Weather_drawing.text(135 - len(temp),45, text= temp, color=weather_font_color,font="Arial",size=50)
Weather_drawing.text(110 - len(temp),110, text= "Low:" + temp_min, color=weather_font_color,font="Arial",size=15)
Weather_drawing.text(225 - len(temp) + len(temp_high)*2,110, text= "High:" + temp_high, color=weather_font_color,font="Arial",size=15)

    
Time_display.repeat(1000, time_update)
app.display()
