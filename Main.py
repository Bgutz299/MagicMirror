#!/usr/bin/enb python
# -*- coding:utf-8 -*-

from guizero import App,Text,ButtonGroup,PushButton,TextBox,Drawing,Box,Window		#https://pypi.org/project/guizero/
from datetime import date, datetime
from time import sleep
import tkinter as tk
import keyboard

# import spotipy
# import requests
# import os
# import sys
# import json
# import webbrowser
# import spotipy.util as util
# from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

# os.environ["SPOTIPY_CLIENT_ID"] = "ae84dd0be57a443ebf92476bc190490a"
# os.environ["SPOTIPY_CLIENT_SECRET"] = "9c6431a32a9c4bf79dd590b912709e8c"
# os.environ["SPOTIPY_REDIRECT_URI"] = "https://Smartmirror.com/auth"



#Weather 
import Weather

#date and time
import date_time

#initializing App
import App_init

#Spotify
# import spotify_module

# #Spotify variables
# global cid
# cid = 'ae84dd0be57a443ebf92476bc190490a'
# global secret
# secret = '9c6431a32a9c4bf79dd590b912709e8c'
# global uri
# uri = 'https://Smartmirror.com/auth'
# global username
# username = ''
# global scope
# scope = 'user-read-private user-read-playback-state user-modify-playback-state'

#global spot_args

global app
app = App_init.app_init()

global Keyboard_box
global keys_exist
keys_exist = 0
global uppercase

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
global To_do_list_Title
global Todolist
global Selectedlist
Todolist=[]
Selectedlist=[]
To_do_list_Title = Text(app, "To-do List:", size=20, color="light gray", grid=[0,2,1,1],align="left")

f = open("Todolist.txt", "r")
with open("Todolist.txt") as f:
	Todolist = [line.strip() for line in f]
#print(read_data)
f.close()


global Display_list
#Create List Function (Uses Button Group)
def create_list():
    global Display_list
    Display_list = ButtonGroup(app, options=Todolist, selected=Selectedlist, grid=[0,3,2,1], align="left")
    Display_list.text_color="light gray"
    Display_list.text_size=20
    Display_list.font="Century Gothic Bold"
#Create New list
create_list()

#Text box for typing
#########################################################################################################
global Add_textbox
Add_textbox=TextBox(app,grid=[0,4,1,1],width=50, align="left")
Add_textbox.text_size=12
Add_textbox.text_color="Black"
Add_textbox.font="Century Gothic Bold"
Add_textbox.bg="white"

#Add button and add function
#########################################################################################################
def addto_todolist():
	global Display_list
	global Todolist
	global Add_textbox
	if(Add_textbox.value):
		f = open("Todolist.txt", "a")
		f.write(Add_textbox.value + "\n")
		f.close()
		Todolist.append(Add_textbox.value)
		Display_list.append(Add_textbox.value)
		print(Todolist)
		Add_textbox.clear()

global Addbutton
Addbutton = PushButton(app, command=addto_todolist, image="Images/add_button.png", grid=[0,4,1,1],align="right")

#Delete from list Button and delete from list function
#########################################################################################################
def delfrom_todolist():
	global Display_list
	global Todolist
	if(Display_list.value_text != ""):
		Todolist.remove(Display_list.value_text)
		f = open("Todolist.txt", "w")
		for i in Todolist:
			f.write(i + "\n")
		f.close()
		Display_list.remove(Display_list.value_text)
	app.focus()
	print(Todolist)
global delbutton
delbutton = PushButton(app, command=delfrom_todolist, image="Images/sub_button.png", grid=[1,4,4,1],align="right")

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
	    f = open("Todolist.txt", "w")
	    f.write("")
	    f.close()
	    create_list()
	    print(Todolist)
#Clear List button
#########################################################################################################
global Clearbutton
Clearbutton = PushButton(app, command=clear_todolist, image="Images/clear_button.png", grid=[0,5], width=100, height=50, align="left")
Clearbutton.bg = "light gray"

#Temperature and Weather
############################################################################################################################################

def init_widgets():
	global app, Weather_drawing, Add_textbox, To_do_list_Title, Addbutton, delbutton, Clearbutton, Citybutton, Spotifybutton
	To_do_list_Title = Text(app, "To-do List:", size=20, color="light gray", grid=[0,2,1,1],align="left")
	create_list()
	Add_textbox=TextBox(app,grid=[0,4,1,1],width=50, align="left")
	Add_textbox.text_size=12
	Add_textbox.text_color="Black"
	Add_textbox.font="Century Gothic Bold"
	Add_textbox.bg="white"
	Addbutton = PushButton(app, command=addto_todolist, image="Images/add_button.png", grid=[0,4,1,1],align="right")
	delbutton = PushButton(app, command=delfrom_todolist, image="Images/sub_button.png", grid=[1,4,4,1],align="right")
	Clearbutton = PushButton(app, command=clear_todolist, image="Images/clear_button.png", grid=[0,5], width=100, height=50, align="left")
	Clearbutton.bg = "light gray"
	Citybutton = PushButton(app, command=change_city, image="Images/Change_city_button.png", grid=[0,5], width=160, height=50)
	Citybutton.bg = "light gray"
	Spotifybutton = PushButton(app, command=Spotify_gui, image="Images/spotify_button.png", grid=[0,5,1,1],align="right", width=50, height=50)
	Spotifybutton.bg = "black"
	Weather_drawing = Drawing(app,grid=[0,6,2,1],align="left",width=600,height=300)
	weather_font_color = which_color(description)
	Image_picture = which_image(description)
	update_weather()
	Weather_drawing.image(0,0,image="Images/" + Image_picture, width=600,height=400)
	city_num_x = 200 - (len(city_name)*10)
	city_num_y = 0

	Weather_drawing.text(city_num_x,city_num_y, text= city_name, color=weather_font_color,font="Arial",size=40)
	Weather_drawing.text(135 - len(temp),45, text= temp, color=weather_font_color,font="Arial",size=50)
	Weather_drawing.text(110 - len(temp),110, text= "Low:" + temp_min, color=weather_font_color,font="Arial",size=15)
	Weather_drawing.text(225 - len(temp) + len(temp_high)*2,110, text= "High:" + temp_high, color=weather_font_color,font="Arial",size=15)
	Weather_drawing.text(150 - len(humidity),135, text= "Humidity: " + humidity, color=weather_font_color,font="Arial",size=15)
	Weather_drawing.text(125 - len(wind_speed),155, text= "Wind Speed: " + wind_speed, color=weather_font_color,font="Arial",size=15)
	Add_textbox.when_clicked = Make_keys
############################################################################################################################################
############################################################################################################################################


#Change City function and Button
#########################################################################################################################################################################################   
def change_city():
	global app
	global window
	global Display_list, Weather_drawing, Add_textbox, To_do_list_Title, Addbutton, delbutton, Clearbutton, Citybutton, Spotifybutton
	def Confirm_city():
		global city_name
		if(City_name_entry_textbox.value):
			city_name = City_name_entry_textbox.value
			f = open("Weather_loc.txt", "w")
			f.write(city_name)
			f.close()
			Confirmbutton.destroy()
			City_name_entry_textbox.destroy()
			City_name_ask_title.destroy()
			Destroy_keys()
			init_widgets()
	if(keys_exist == 1):
		Destroy_keys()
	To_do_list_Title.destroy()
	Add_textbox.destroy()
	Addbutton.destroy()
	delbutton.destroy()
	Citybutton.destroy()
	Spotifybutton.destroy()
	Display_list.destroy()
	Clearbutton.destroy()
	Weather_drawing.destroy()
	City_name_ask_title = Text(app, "Type the name of a city:", size=35, font="Century Gothic Bold", color="light gray", grid=[0,2,2,1],align="left")
	City_name_entry_textbox=TextBox(app,grid=[0,3],width=50)
	City_name_entry_textbox.text_size=12
	City_name_entry_textbox.text_color="Black"
	City_name_entry_textbox.font="Century Gothic Bold"
	City_name_entry_textbox.bg="white"
	City_name_entry_textbox.when_clicked = Make_keys
	Confirmbutton = PushButton(app, command=Confirm_city, image="Images/Confirm.png", grid=[0,4], width=120, height=50)
	Confirmbutton.bg = "light gray"
	app.focus()

#Change City button
#########################################################################################################################################################################################    
global Citybutton
Citybutton = PushButton(app, command=change_city, image="Images/Change_city_button.png", grid=[0,5], width=160, height=50)
Citybutton.bg = "light gray"
############################################################################################################################################
############################################################################################################################################
#Spotify Button and function

# global Volume_text
# global playbackstate
# def raise_volume_spotify():
# 	global Volume_text, app
# 	volume_level = str(spotify_module.volume_up())
# 	Volume_text.value = "Volume: " + volume_level

# def decrease_volume_spotify():
# 	global Volume_text, app
# 	volume_level = str(spotify_module.volume_down())
# 	Volume_text.value = "Volume: " + volume_level

# def Spotify_gui():
# 	global app
# 	global window
# 	global Display_list, Weather_drawing, Add_textbox, To_do_list_Title, Addbutton, delbutton, Clearbutton, Citybutton, Spotifybutton, Volume_text

# 	def spotify_exit():
# 		Spotify_title.destroy()
# 		Volume_text.destroy()
# 		Playbutton.destroy()
# 		Pausebutton.destroy()
# 		Exit_button.destroy()
# 		Volume_upbutton.destroy()
# 		Volume_downbutton.destroy()
# 		init_widgets()

# 	To_do_list_Title.destroy()
# 	Add_textbox.destroy()
# 	Addbutton.destroy()
# 	delbutton.destroy()
# 	Citybutton.destroy()
# 	Spotifybutton.destroy()
# 	Display_list.destroy()
# 	Clearbutton.destroy()
# 	Weather_drawing.destroy()
# 	Spotify_title = Text(app, "Spotify Player", size=35, font="Century Gothic Bold", color="light gray", grid=[0,2,2,1],align="left")

# 	Volume_level = "Volume: " + str(spotify_module.fetch_volume())
# 	Volume_text = Text(app, Volume_level, size=35, font="Century Gothic Bold", color="light gray", grid=[0,6,2,1],align="left")
# 	Playbutton = PushButton(app, command=spotify_module.play, image="Images/play_button.png", grid=[0,5], width=50, height=50)
# 	Pausebutton = PushButton(app, command=spotify_module.pause, image="Images/pause_button.png", grid=[1,5], align="left", width=50, height=50)
	

# 	Volume_upbutton=PushButton(app, command=raise_volume_spotify, image="Images/volume_up.png", grid=[2,5], width=50, height=50)
# 	Volume_downbutton=PushButton(app, command=decrease_volume_spotify, image="Images/volume_down.png", grid=[2,6], width=50, height=50)	

# 	Playbutton.bg = "light gray"
# 	Pausebutton.bg = "light gray"


# 	Exit_button = PushButton(app, command=spotify_exit, image="Images/Exit_button.png", grid=[0,8], width=100, height=60)
	


# 	app.focus()
# global Spotifybutton
# Spotifybutton = PushButton(app, command=Spotify_gui, image="Images/spotify_button.png", grid=[0,5,1,1], align = "right", width=50, height=50)
# Spotifybutton.bg = "black"


#Weather Drawing
######################################################################################################################################################################################### 
global temp, temp_min, temp_high, description, humidity, wind_speed, city_name
city_name = ""
def update_weather():
	global temp, temp_min, temp_high, description, humidity, wind_speed, city_name
	f = open("Weather_loc.txt", "r")
	city_name = f.read()
	f.close()
	temp, temp_min, temp_high, description, humidity, wind_speed = Weather.fetchWeather(city_name)
	#temp, temp_min, temp_high, description, humidity, wind_speed = "87°F", "80°F", "94°F", "few clouds", "10%", "50 m/s"

global Weather_drawing
Weather_drawing = Drawing(app,grid=[0,6,2,1],align="left",width=600,height=300)
update_weather()
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
        "broken clouds": "black",
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

############################################################################################################################################
############################################################################################################################################

#Keyboard Module
############################################################################################################################################
uppercase = 0
keys_exist = 0
global lower_letters, upper_letters
lower_letters = ["q","w","e","r","t","y","u","i","o","p",
					"a","s","d","f","g","h","j","k","l",
					"z","x","c","v","b","n","m", " ", "\b"]
upper_letters = ["Q","W","E","R","T","Y","U","I","O","P",
					"A","S","D","F","G","H","J","K","L",
					"Z","X","C","V","B","N","M", " ", "\b"]


#Keyboard Box
###########################################################################################################################################
def type_function(letter):
	global uppercase
	global Keyboard_box
	keyboard.write(letter)
	if(uppercase == 1):
		Make_keys()

#Make Upper case keyboard
def Make_upperkeys():
	global Keyboard_box
	global keys_exist
	global uppercase
	if(keys_exist == 1 and uppercase == 0):
		Weather_drawing.grid = [0,7,2,1]
		Keyboard_box.destroy()
		Keyboard_box = Box(app,width=500,height=300, layout="grid", grid=[0,6,4,1])
		uppercase = 1
	elif(keys_exist == 1 and uppercase == 1):
		Keyboard_box.destroy()
		Make_keys()
#Keyboard
#1st Row
	Q_button = PushButton(Keyboard_box, grid=[0,0], width=2, height=2, text=upper_letters[0], command=type_function, args=upper_letters[0])
	Q_button.bg = "light gray"
	Q_button.text_size=10

	W_button = PushButton(Keyboard_box, grid=[1,0], width=2, height=2, text=upper_letters[1], command=type_function, args=upper_letters[1])
	W_button.bg = "light gray"
	W_button.text_size=10

	E_button = PushButton(Keyboard_box, grid=[2,0], width=2, height=2, text=upper_letters[2], command=type_function, args=upper_letters[2])
	E_button.bg = "light gray"
	E_button.text_size=10

	R_button = PushButton(Keyboard_box, grid=[3,0], width=2, height=2, text=upper_letters[3], command=type_function, args=upper_letters[3])
	R_button.bg = "light gray"
	R_button.text_size=10

	T_button = PushButton(Keyboard_box, grid=[4,0], width=2, height=2, text=upper_letters[4], command=type_function, args=upper_letters[4])
	T_button.bg = "light gray"
	T_button.text_size=10

	Y_button = PushButton(Keyboard_box, grid=[5,0], width=2, height=2, text=upper_letters[5], command=type_function, args=upper_letters[5])
	Y_button.bg = "light gray"
	Y_button.text_size=10

	U_button = PushButton(Keyboard_box, grid=[6,0], width=2, height=2, text=upper_letters[6], command=type_function, args=upper_letters[6])
	U_button.bg = "light gray"
	U_button.text_size=10

	I_button = PushButton(Keyboard_box, grid=[7,0], width=2, height=2, text=upper_letters[7], command=type_function, args=upper_letters[7])
	I_button.bg = "light gray"
	I_button.text_size=10

	O_button = PushButton(Keyboard_box, grid=[8,0], width=2, height=2, text=upper_letters[8], command=type_function, args=upper_letters[8])
	O_button.bg = "light gray"
	O_button.text_size=10

	P_button = PushButton(Keyboard_box, grid=[9,0], width=2, height=2, text=upper_letters[9], command=type_function, args=upper_letters[9])
	P_button.bg = "light gray"
	P_button.text_size=10

#2nd Row
	A_button = PushButton(Keyboard_box, grid=[0,1,2,1], width=2, height=2, text=upper_letters[10], command=type_function, args=upper_letters[10])
	A_button.bg = "light gray"
	A_button.text_size=10

	S_button = PushButton(Keyboard_box, grid=[1,1,2,1], width=2, height=2, text=upper_letters[11], command=type_function, args=upper_letters[11])
	S_button.bg = "light gray"
	S_button.text_size=10

	D_button = PushButton(Keyboard_box, grid=[2,1,2,1], width=2, height=2, text=upper_letters[12], command=type_function, args=upper_letters[12])
	D_button.bg = "light gray"
	D_button.text_size=10

	F_button = PushButton(Keyboard_box, grid=[3,1,2,1], width=2, height=2, text=upper_letters[13], command=type_function, args=upper_letters[13])
	F_button.bg = "light gray"
	F_button.text_size=10

	G_button = PushButton(Keyboard_box, grid=[4,1,2,1], width=2, height=2, text=upper_letters[14], command=type_function, args=upper_letters[14])
	G_button.bg = "light gray"
	G_button.text_size=10

	H_button = PushButton(Keyboard_box, grid=[5,1,2,1], width=2, height=2, text=upper_letters[15], command=type_function, args=upper_letters[15])
	H_button.bg = "light gray"
	H_button.text_size=10

	J_button = PushButton(Keyboard_box, grid=[6,1,2,1], width=2, height=2, text=upper_letters[16], command=type_function, args=upper_letters[16])
	J_button.bg = "light gray"
	J_button.text_size=10

	K_button = PushButton(Keyboard_box, grid=[7,1,2,1], width=2, height=2, text=upper_letters[17], command=type_function, args=upper_letters[17])
	K_button.bg = "light gray"
	K_button.text_size=10

	L_button = PushButton(Keyboard_box, grid=[8,1,2,1], width=2, height=2, text=upper_letters[18], command=type_function, args=upper_letters[18])
	L_button.bg = "light gray"
	L_button.text_size=10

#3rd Row
	shift_button = PushButton(Keyboard_box, grid=[0,2,2,1], align="left", width=2, height=2, padx=15,pady=10, text="Shift", command = Make_keys)
	shift_button.bg = "light gray"
	shift_button.text_size=10

	Z_button = PushButton(Keyboard_box, grid=[1,2,2,1], width=2, height=2, text=upper_letters[19], command=type_function, args=upper_letters[19])
	Z_button.bg = "light gray"
	Z_button.text_size=10

	X_button = PushButton(Keyboard_box, grid=[2,2,2,1], width=2, height=2, text=upper_letters[20], command=type_function, args=upper_letters[20])
	X_button.bg = "light gray"
	X_button.text_size=10

	C_button = PushButton(Keyboard_box, grid=[3,2,2,1], width=2, height=2, text=upper_letters[21], command=type_function, args=upper_letters[21])
	C_button.bg = "light gray"
	C_button.text_size=10

	V_button = PushButton(Keyboard_box, grid=[4,2,2,1], width=2, height=2, text=upper_letters[22], command=type_function, args=upper_letters[22])
	V_button.bg = "light gray"
	V_button.text_size=10

	B_button = PushButton(Keyboard_box, grid=[5,2,2,1], width=2, height=2, text=upper_letters[23], command=type_function, args=upper_letters[23])
	B_button.bg = "light gray"
	B_button.text_size=10

	N_button = PushButton(Keyboard_box, grid=[6,2,2,1], width=2, height=2, text=upper_letters[24], command=type_function, args=upper_letters[24])
	N_button.bg = "light gray"
	N_button.text_size=10

	M_button = PushButton(Keyboard_box, grid=[7,2,2,1], width=2, height=2, text=upper_letters[25], command=type_function, args=upper_letters[25])
	M_button.bg = "light gray"
	M_button.text_size=10

	backspace_button = PushButton(Keyboard_box, grid=[8,2,2,1], align="right", width=2, height=2, padx=15,pady=10, text="<-", command=type_function, args=upper_letters[27])
	backspace_button.bg = "light gray"
	backspace_button.text_size=10

#4th Row
	Space_button = PushButton(Keyboard_box, grid=[2,3,6,1], width=28, height=2, padx=5,pady=1, text="Space", command=type_function, args=upper_letters[26])
	Space_button.bg = "light gray"
	Space_button.text_size=10

	Hide_button = PushButton(Keyboard_box, grid=[8,3,6,1], width=5, height=2, padx=5,pady=1, text="Hide", command =	Destroy_keys)
	Hide_button.text_size=10
	Hide_button.bg = "light gray"

#Make lower case keyboard
def Make_keys():
	global Keyboard_box
	global keys_exist
	global uppercase
	global lower_letters
	if(keys_exist == 0):
		Weather_drawing.grid = [0,7,2,1]
		Keyboard_box = Box(app,width=500,height=300, layout="grid", grid=[0,6,4,1])
		keys_exist = 1
		uppercase = 0
	elif(keys_exist == 1 and uppercase == 1):
		Keyboard_box.destroy()
		Keyboard_box = Box(app,width=500,height=300, layout="grid", grid=[0,6,2,1])
		uppercase = 0
#Keyboard
#1st Row
	Q_button = PushButton(Keyboard_box, grid=[0,0], width=2, height=2, text=lower_letters[0], command = type_function, args = lower_letters[0])
	Q_button.bg = "light gray"
	Q_button.text_size=10

	W_button = PushButton(Keyboard_box, grid=[1,0], width=2, height=2, text=lower_letters[1], command = type_function, args = lower_letters[1])
	W_button.bg = "light gray"
	W_button.text_size=10

	E_button = PushButton(Keyboard_box, grid=[2,0], width=2, height=2, text=lower_letters[2], command = type_function, args = lower_letters[2])
	E_button.bg = "light gray"
	E_button.text_size=10

	R_button = PushButton(Keyboard_box, grid=[3,0], width=2, height=2, text=lower_letters[3], command = type_function, args = lower_letters[3])
	R_button.bg = "light gray"
	R_button.text_size=10

	T_button = PushButton(Keyboard_box, grid=[4,0], width=2, height=2, text=lower_letters[4], command = type_function, args = lower_letters[4])
	T_button.bg = "light gray"
	T_button.text_size=10

	Y_button = PushButton(Keyboard_box, grid=[5,0], width=2, height=2, text=lower_letters[5], command = type_function, args = lower_letters[5])
	Y_button.bg = "light gray"
	Y_button.text_size=10

	U_button = PushButton(Keyboard_box, grid=[6,0], width=2, height=2, text=lower_letters[6], command = type_function, args = lower_letters[6])
	U_button.bg = "light gray"
	U_button.text_size=10

	I_button = PushButton(Keyboard_box, grid=[7,0], width=2, height=2, text=lower_letters[7], command = type_function, args = lower_letters[7])
	I_button.bg = "light gray"
	I_button.text_size=10

	O_button = PushButton(Keyboard_box, grid=[8,0], width=2, height=2, text=lower_letters[8], command = type_function, args = lower_letters[8])
	O_button.bg = "light gray"
	O_button.text_size=10

	P_button = PushButton(Keyboard_box, grid=[9,0], width=2, height=2, text=lower_letters[9], command = type_function, args = lower_letters[9])
	P_button.bg = "light gray"
	P_button.text_size=10

#2nd Row
	A_button = PushButton(Keyboard_box, grid=[0,1,2,1], width=2, height=2, text=lower_letters[10], command = type_function, args = lower_letters[10])
	A_button.bg = "light gray"
	A_button.text_size=10

	S_button = PushButton(Keyboard_box, grid=[1,1,2,1], width=2, height=2, text=lower_letters[11], command = type_function, args = lower_letters[11])
	S_button.bg = "light gray"
	S_button.text_size=10

	D_button = PushButton(Keyboard_box, grid=[2,1,2,1], width=2, height=2, text=lower_letters[12], command = type_function, args = lower_letters[12])
	D_button.bg = "light gray"
	D_button.text_size=10

	F_button = PushButton(Keyboard_box, grid=[3,1,2,1], width=2, height=2, text=lower_letters[13], command = type_function, args = lower_letters[13])
	F_button.bg = "light gray"
	F_button.text_size=10

	G_button = PushButton(Keyboard_box, grid=[4,1,2,1], width=2, height=2, text=lower_letters[14], command = type_function, args = lower_letters[14])
	G_button.bg = "light gray"
	G_button.text_size=10

	H_button = PushButton(Keyboard_box, grid=[5,1,2,1], width=2, height=2, text=lower_letters[15], command = type_function, args = lower_letters[15])
	H_button.bg = "light gray"
	H_button.text_size=10

	J_button = PushButton(Keyboard_box, grid=[6,1,2,1], width=2, height=2, text=lower_letters[16], command = type_function, args = lower_letters[16])
	J_button.bg = "light gray"
	J_button.text_size=10

	K_button = PushButton(Keyboard_box, grid=[7,1,2,1], width=2, height=2, text=lower_letters[17], command = type_function, args = lower_letters[17])
	K_button.bg = "light gray"
	K_button.text_size=10

	L_button = PushButton(Keyboard_box, grid=[8,1,2,1], width=2, height=2, text=lower_letters[18], command = type_function, args = lower_letters[18])
	L_button.bg = "light gray"
	L_button.text_size=10

#3rd Row
	shift_button = PushButton(Keyboard_box, grid=[0,2,2,1], align="left", width=2, height=2, padx=15,pady=10, text="Shift", command = Make_upperkeys)
	shift_button.bg = "light gray"
	shift_button.text_size=10

	Z_button = PushButton(Keyboard_box, grid=[1,2,2,1], width=2, height=2, text=lower_letters[19], command = type_function, args = lower_letters[19])
	Z_button.bg = "light gray"
	Z_button.text_size=10

	X_button = PushButton(Keyboard_box, grid=[2,2,2,1], width=2, height=2, text=lower_letters[20], command = type_function, args = lower_letters[20])
	X_button.bg = "light gray"
	X_button.text_size=10

	C_button = PushButton(Keyboard_box, grid=[3,2,2,1], width=2, height=2, text=lower_letters[21], command = type_function, args = lower_letters[21])
	C_button.bg = "light gray"
	C_button.text_size=10

	V_button = PushButton(Keyboard_box, grid=[4,2,2,1], width=2, height=2, text=lower_letters[22], command = type_function, args = lower_letters[22])
	V_button.bg = "light gray"
	V_button.text_size=10

	B_button = PushButton(Keyboard_box, grid=[5,2,2,1], width=2, height=2, text=lower_letters[23], command = type_function, args = lower_letters[23])
	B_button.bg = "light gray"
	B_button.text_size=10

	N_button = PushButton(Keyboard_box, grid=[6,2,2,1], width=2, height=2, text=lower_letters[24], command = type_function, args = lower_letters[24])
	N_button.bg = "light gray"
	N_button.text_size=10

	M_button = PushButton(Keyboard_box, grid=[7,2,2,1], width=2, height=2, text=lower_letters[25], command = type_function, args = lower_letters[25])
	M_button.bg = "light gray"
	M_button.text_size=10

	backspace_button = PushButton(Keyboard_box, grid=[8,2,2,1], align="right", width=2, height=2, padx=15,pady=10, text="<-", command=type_function, args=lower_letters[27])
	backspace_button.bg = "light gray"
	backspace_button.text_size=10

#4th Row
	Space_button = PushButton(Keyboard_box, grid=[2,3,6,1], width=28, height=2, padx=5,pady=1, text="Space", command=type_function, args=lower_letters[26])
	Space_button.bg = "light gray"
	Space_button.text_size=10

	Hide_button = PushButton(Keyboard_box, grid=[8,3,6,1], width=5, height=2, padx=5,pady=1, text="Hide", command =	Destroy_keys)
	Hide_button.text_size=10
	Hide_button.bg = "light gray"

#Destroy Keyboard box
def Destroy_keys():
	global Keyboard_box
	global app
	global keys_exist
	keys_exist = 0
	Keyboard_box.destroy()
	app.focus()


Add_textbox.when_clicked = Make_keys
Time_display.repeat(1000, time_update)
Weather_drawing.repeat(600000, update_weather)
app.display()
