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
        print (Fore.RED + "\nVRS has changed your alarm 30 minutes early due to " + Fore.BLUE + "ICY ROADS!")
        print (Fore.RED + "VRS will only allow your car to go 30 MPH" + Fore.RESET)
    elif weatherAlert == "Snow":
        print(Fore.RED + "\nVRS has changed your alarm 15 minutes early due to " + Fore.BLUE + "SNOW!")
        print(Fore.RED + "VRS will only allow your car to go 50 MPH" + Fore.RESET)
    elif weatherAlert == "Heavy Rain":
        print(Fore.RED + "\nVRS has changed your alarm 10 minutes early due to " + Fore.BLUE + " HEAVY RAIN!")
        print(Fore.RED + "VRS will only allow your car to go 50 MPH" + Fore.RESET)
    elif weatherAlert == "Rain":
        print(Fore.RED + "\nVRS has changed your alarm 5 minutes early due to " + Fore.BLUE + "RAIN!")
        print(Fore.RED + "VRS will only allow your car to go 60 MPH" + Fore.RESET)
    elif weatherAlert == "High Wind":
        print(Fore.RED + "\nVRS has changed your alarm 5 minutes early due to " + Fore.BLUE + "HIGH WIND!")
        print(Fore.RED + "VRS will only allow your car to go 70 MPH" + Fore.RESET)
    elif weatherAlert == "Fog":
        print(Fore.RED + "\nVRS has changed your alarm 5 minutes early due to " + Fore.BLUE + "FOG!")
        print(Fore.RED + "VRS will only allow your car to go 60 MPH" + Fore.RESET)
    else:
        print(Fore.YELLOW + "\nWeather is Sunny!" + Fore.RESET)

vehicleResponseSystem()
