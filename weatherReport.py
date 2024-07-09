import requests
import json
import tkinter as tk
from datetime import datetime


apikey = "da62f95f9d22fc98094f931afd43d221"

baseUrl = "http://api.openweathermap.org/data/2.5/weather?"


def kelvin_to_F_or_C(kelvin, parameter = None):
    if parameter is not None:
        if parameter == "F":
            return str(round(((9/5)*(kelvin - 273.15) + 32), 2))
        if parameter == "C":
            return str(round((kelvin - 273.15),2))
    return

def locationLookup():
    try:
        response = requests.get('http://ipinfo.io/json')
        return response.json()
    except requests.RequestException:
        return False
  
locationDictionary = locationLookup()
city = locationDictionary.get('city')

ip = locationDictionary.get('ip')

personalizedWeather = baseUrl + "appid=" + apikey + "&q=" + city

response = requests.get(personalizedWeather)

weather = response.json()

humidity = weather['main']['humidity']

sunriseTime = datetime.fromtimestamp(weather['sys']['sunrise'])

sunriseTimeFormat = str(sunriseTime.strftime("%I:%M:%S%p"))

sunsetTime = datetime.fromtimestamp(weather['sys']['sunset'])

sunsetTimeFormat = str(sunsetTime.strftime("%I:%M:%S%p"))

windSpeed = str(weather['wind']['speed'])

currentF = kelvin_to_F_or_C(weather['main']['temp'], parameter="F")

currentC = kelvin_to_F_or_C(weather['main']['temp'], parameter="C")

lowFarenheit = kelvin_to_F_or_C(weather['main']['temp_min'], parameter="F")

lowCelsius = kelvin_to_F_or_C(weather['main']['temp_min'], parameter="C")

maxFarenheit = kelvin_to_F_or_C(weather['main']['temp_max'], parameter="F")

maxCelsius = kelvin_to_F_or_C(weather['main']['temp_max'], parameter="C")

#with open('weather.txt', 'w') as f:
 #   f.write(f"The current temperature in {city} is: " + currentF + " Farenheit" + " (" + currentC + " Celsius)\n")
  #  f.write(f"Today, the low in {city}: " + lowFarenheit + " Farenheit" + " (" + lowCelsius + " Celsius)\n")
   # f.write(f"While, the max in {city}: " + maxFarenheit + " Farenheit" + " (" + maxCelsius + " Celsius)\n")
    #f.write(f"Winds in the city of {city} can reach up to " + windSpeed + "m/s" + " with gust speeds reaching " + windGust + "m/s\n")
#    f.write(f"For those who care, sunrise in {city} will  be at " + sunriseTimeFormat + " and sunset will be at " + sunsetTimeFormat + "\n")
 #   f.close()

def __init__():
    root = tk.Tk()
    tempLabel = None
    root.title("Today's weather!   " + f"Your ip is: {ip} !!!!, YAY!")
    root.geometry("800x400")
    setWeatherUp()


    root.mainloop()

        
def setWeatherUp():
    writeHighLowF()
    writeHighLowC()
    windSpeeds()
    sunriseSunset()
    humidityLabel()

def writeHighLowF(row = 0, col = 0):
    tempLabel = tk.Label(text = f"Temperature for the day in {city}: ", font=("Arial",18))
    tempLabel.grid(row = row, column = col, sticky='w')
    
    highTemp = tk.Label(text = f"High: {maxFarenheit}" + "F" , font=("Arial",14))
    highTemp.grid(row = row+1, column = col, sticky = 'w')
    
    currentTemp = tk.Label(text = f"Current: {currentF}" + "F" , font=("Arial",14))
    currentTemp.grid(row = row+2, column = col, sticky = 'w')
    
    lowTemp = tk.Label(text = f"Low: {lowFarenheit}" + "F" , font=("Arial",14))
    lowTemp.grid(row = row+3, column = col, sticky = 'w')

def writeHighLowC(row = 0, col = 0):
    highTemp = tk.Label(text = f"High: {maxCelsius}" + "C" , font=("Arial",14))
    highTemp.grid(row = row+1, column = col, sticky = 'e')
    
    currentTemp = tk.Label(text = f"Current: {currentC}" + "C" , font=("Arial",14))
    currentTemp.grid(row = row+2, column = col, sticky = 'e')
    
    lowTemp = tk.Label(text = f"Low: {lowCelsius}" + "C" , font=("Arial",14))
    lowTemp.grid(row = row+3, column = col, sticky = 'e')
    
def windSpeeds(row = 4, col = 0):
    windSpeedLabel = tk.Label(text = f"Wind Data in {city}: ", font=("Arial",12))
    windSpeedLabel.grid(row = row, column = col, sticky = 'w')
    
    windSpeedMPERS = tk.Label(text = f"Wind Speed: {windSpeed}m/s", font=("Arial", 14))
    windSpeedMPERS.grid(row = row+1, column = col, sticky = 'w')
    
def sunriseSunset(row = 6, col = 0):
    sunriseLabel = tk.Label(text = f"Sunrise and Sunset times in {city} will be at:" , font=("Arial", 12))
    sunriseLabel.grid(row = row, column = col, sticky = 'w')
    
    sunriseActual = tk.Label(text = f"Sunrise: "+ sunriseTimeFormat, font=("Arial",14))
    sunriseActual.grid(row = row+1, column = col, sticky='w')
    
    sunsetActual = tk.Label(text = f"Sunset: "+ sunsetTimeFormat, font=("Arial",14))
    sunsetActual.grid(row = row+1, column = col, sticky='e')
    
def humidityLabel(row = 7, col = 0):
    humidityActual = tk.Label(text = f"Humidity today in {city} is {humidity}%", font=("Arial",12))
    humidityActual.grid(row = row+1, column = col, sticky='w')
    



__init__()
    
