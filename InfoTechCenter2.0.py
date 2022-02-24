# Weather Branch

import random
from colorama import Fore

def weather():
    weatherForecast = ["Ice", "Snow", "Heavy Rain", "Rain", "High Wind", "Fog", "Sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

# Calling weather function to determine weather
weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "Ice":
        print (Fore.RED + "\nVRS has changed your alarm 30 minutes early due to " + Fore.LIGHTBLUE_EX + "ICY ROADS!")
        print (Fore.RED + "VRS will only allow your car to go 30 MPH" + Fore.RESET)

vehicleResponseSystem()
