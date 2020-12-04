from guizero import App,Text,ButtonGroup,PushButton,TextBox		#https://pypi.org/project/guizero/
from datetime import date, datetime
#Fetch data from internet using openweather API
import json
import urllib.request

def fetchWeather(city_name):
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&units=imperial&appid=bb0723c44c591a78fd4d5f47215ffb51"
    request = urllib.request.urlopen(url)
    data = json.load(request)
    temp = int(data['main']['temp'])
    temp_min = int(data['main']['temp_min'])
    temp_high = int(data['main']['temp_max'])
    description = data['weather'][0]['description']
    humidity = int(data['main']['humidity'])
    wind_speed = int(data['wind']['speed'])
    str_temp = str(temp) + "°F"
    str_temp_min = str(temp_min) + "°F"
    str_temp_high = str(temp_high) + "°F"
    str_humidity = str(humidity) +  "%"
    str_wind_speed = str(wind_speed) + "m/s"

    # Clearbutton = PushButton(app, text="Clear", grid=[0,6], align="left")
    # Clearbutton.text_color="Black"
    # Clearbutton.bg="light gray"
    # Clearbutton.font="Century Gothic Bold"
    # Clearbutton.text_size="12"
    print(description)
    return str_temp,str_temp_min,str_temp_high,description, str_humidity, str_wind_speed

if __name__ == '__main__':
    fetchWeather()
