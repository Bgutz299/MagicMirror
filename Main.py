#!/usr/bin/enb python
# -*- coding:utf-8 -*-

from guizero import App,Text,ButtonGroup,PushButton,TextBox,Drawing,Box		#https://pypi.org/project/guizero/
from datetime import date, datetime
from time import sleep
import tkinter as tk

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
Date_display = Text(app, today_date, size=40, font="Century Gothic Bold", color="light gray", grid=[0,0,2,1],align="left")
Time_display = Text(app, curr_time, size=50, font="Century Gothic Bold", color="light gray", grid=[0,1,2,1],align="left")
def time_update():
    Time_display.value = date_time.time_get()
##########################################################################################################################

#Todo List
##########################################################################################################################
To_do_list_Title = Text(app, "To-do List:", size=20, color="light gray", grid=[0,2,1,1],align="left")

global Todolist
global Selectedlist
Todolist=[]
Selectedlist=[]

global Display_list
#Create List Function (Uses Button Group)
def create_list():
    global Display_list
    Display_list = ButtonGroup(app, options=Todolist, selected=Selectedlist, align="left", grid=[0,3,2,1])
    Display_list.text_color="light gray"
    Display_list.text_size=20
    Display_list.font="Century Gothic Bold"
#Create New list
create_list()

#Text box for typing
#########################################################################################################
Add_textbox=TextBox(app,grid=[0,4,2,1],width=40,align="left")
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
    app.focus()

Addbutton = PushButton(app, command=addto_todolist, image="Images/add_button.png", grid=[0,4,1,1], align="right")
#Addbutton.text_color="Black"
#Addbutton.bg="black"
#Addbutton.font="Century Gothic Bold"
#Addbutton.text_size="12"

#Delete from list Button
#########################################################################################################
def delfrom_todolist():
    global Display_list
    global Todolist
    if(Display_list.value_text != ""):
        Todolist.remove(Display_list.value_text)
        Display_list.remove(Display_list.value_text)
    app.focus()
    print(Todolist)

Addbutton = PushButton(app, command=delfrom_todolist, image="Images/sub_button.png", grid=[1,4,1,1], align="left")
# Addbutton.text_color="Black"
# Addbutton.bg="light gray"
# Addbutton.font="Century Gothic Bold"
# Addbutton.text_size="12"

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

#Temperature and Weather
#########################################################################################################

#Weather Drawing
city_name = "Indio"
global temp, temp_min, temp_high, description, humidity, wind_speed
# def update_weather():
#     global temp, temp_min, temp_high, description, humidity, wind_speed
#     temp, temp_min, temp_high, description, humidity, wind_speed = Weather.fetchWeather(city_name)
temp, temp_min, temp_high, description, humidity, wind_speed = "87°F", "80°F", "94°F", "broken clouds", "10%", "50 m/s"
Weather_drawing = Drawing(app,grid=[0,6,2,1],align="left",width=600,height=300)
#update_weather()
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
Weather_drawing.image(0,0,image="Images/" + Image_picture, width=600,height=400)
city_num_x = 200 - (len(city_name)*10)
city_num_y = 0

Weather_drawing.text(city_num_x,city_num_y, text= city_name, color=weather_font_color,font="Arial",size=40)
Weather_drawing.text(135 - len(temp),45, text= temp, color=weather_font_color,font="Arial",size=50)
Weather_drawing.text(110 - len(temp),110, text= "Low:" + temp_min, color=weather_font_color,font="Arial",size=15)
Weather_drawing.text(225 - len(temp) + len(temp_high)*2,110, text= "High:" + temp_high, color=weather_font_color,font="Arial",size=15)
Weather_drawing.text(150 - len(humidity),135, text= "Humidity: " + humidity, color=weather_font_color,font="Arial",size=15)
Weather_drawing.text(125 - len(wind_speed),155, text= "Wind Speed: " + wind_speed, color=weather_font_color,font="Arial",size=15)

def mouseClick( event ):    
	global app
	if(".!entry" in str(app.tk.focus_get())):
		app.focus()
		Destroy_keys()

app.tk.bind("<Double-Button-1>", mouseClick)

global Keyboard_box
#Keyboard Box
#########################################################################################################
def Make_keys():
	global Keyboard_box
	Keyboard_box = Box(app,width=600,height=200, layout="grid", grid=[0,7,2,1])
	#Keyboard
	Q_button = PushButton(Keyboard_box, grid=[0,0], width=2, height=2, text="Q")
	Q_button.bg = "light gray"

	W_button = PushButton(Keyboard_box, grid=[1,0], width=2, height=2, text="W")
	W_button.bg = "light gray"

	E_button = PushButton(Keyboard_box, grid=[2,0], width=2, height=2, text="E")
	E_button.bg = "light gray"

	R_button = PushButton(Keyboard_box, grid=[3,0], width=2, height=2, text="R")
	R_button.bg = "light gray"

	T_button = PushButton(Keyboard_box, grid=[4,0], width=2, height=2, text="T")
	T_button.bg = "light gray"

	Y_button = PushButton(Keyboard_box, grid=[5,0], width=2, height=2, text="Y")
	Y_button.bg = "light gray"

	U_button = PushButton(Keyboard_box, grid=[6,0], width=2, height=2, text="U")
	U_button.bg = "light gray"

	I_button = PushButton(Keyboard_box, grid=[7,0], width=2, height=2, text="I")
	I_button.bg = "light gray"

	O_button = PushButton(Keyboard_box, grid=[8,0], width=2, height=2, text="O")
	O_button.bg = "light gray"

	P_button = PushButton(Keyboard_box, grid=[9,0], width=2, height=2, text="P")
	P_button.bg = "light gray"

	A_button = PushButton(Keyboard_box, grid=[0,1], width=2, height=2, text="A")
	A_button.bg = "light gray"

	S_button = PushButton(Keyboard_box, grid=[1,1], width=2, height=2, text="S")
	S_button.bg = "light gray"

	D_button = PushButton(Keyboard_box, grid=[2,1], width=2, height=2, text="D")
	D_button.bg = "light gray"

	F_button = PushButton(Keyboard_box, grid=[3,1], width=2, height=2, text="F")
	F_button.bg = "light gray"

	G_button = PushButton(Keyboard_box, grid=[4,1], width=2, height=2, text="G")
	G_button.bg = "light gray"

	H_button = PushButton(Keyboard_box, grid=[5,1], width=2, height=2, text="H")
	H_button.bg = "light gray"

	J_button = PushButton(Keyboard_box, grid=[6,1], width=2, height=2, text="J")
	J_button.bg = "light gray"

	K_button = PushButton(Keyboard_box, grid=[7,1], width=2, height=2, text="K")
	K_button.bg = "light gray"

	L_button = PushButton(Keyboard_box, grid=[8,1], width=2, height=2, text="L")
	L_button.bg = "light gray"

	Z_button = PushButton(Keyboard_box, grid=[1,2], width=2, height=2, text="Z")
	Z_button.bg = "light gray"

	X_button = PushButton(Keyboard_box, grid=[2,2], width=2, height=2, text="X")
	X_button.bg = "light gray"

	C_button = PushButton(Keyboard_box, grid=[3,2], width=2, height=2, text="C")
	C_button.bg = "light gray"

	V_button = PushButton(Keyboard_box, grid=[4,2], width=2, height=2, text="V")
	V_button.bg = "light gray"

	B_button = PushButton(Keyboard_box, grid=[5,2], width=2, height=2, text="B")
	B_button.bg = "light gray"

	N_button = PushButton(Keyboard_box, grid=[6,2], width=2, height=2, text="N")
	N_button.bg = "light gray"

	M_button = PushButton(Keyboard_box, grid=[7,2], width=2, height=2, text="M")
	M_button.bg = "light gray"
def Destroy_keys():
	global Keyboard_box
	Keyboard_box.destroy()

Add_textbox.when_clicked = Make_keys


Time_display.repeat(1000, time_update)
#Weather_drawing.repeat(600000, update_weather)
app.display()
