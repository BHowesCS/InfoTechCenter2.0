# Code Name - Hornet

# Import libraries here
from time import sleep
import colorama
from colorama import Fore
colorama.init(strip=False, autoreset=True)
import random

# Welcome Branch

print(Fore.MAGENTA+"Welcome to Hornet's InfoTechCenter\n")

sleep(1)

print("Hornet's Operating System Booting Up\n")

sleep(1)

# Gas Branch

# Gas Level Function
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

# Variable calls the value of gasLevelGauge Function
gasLevelIndicator = gasLevelGauge()

# Create IF-ELIF-ELSE statements using Comparative Operators == Equal To in order to display gas level messages
def gasLevelAlert():
    gasStations = ["Shell", "BP", "Citgo", "Circle K", "Mobil", "Speedway", "Marathon", "Love's", "Meijer", "Costco"]
    miles = round(random.uniform(1, 25), 1)
    if gasLevelIndicator == "Empty":
        print(Fore.RED+"***WARNING***\n**GAS EMPTY**\nCalling Emergency Contact"+Fore.RESET)
    elif gasLevelIndicator == "Low":
        print(Fore.LIGHTYELLOW_EX+"***WARNING***\n**LOW ON GAS**")
        print("The closest gas station is "+random.choice(gasStations)+" which is "+str(miles)+" miles away"+Fore.RESET)
    elif gasLevelIndicator == "Quarter Tank":
        print(Fore.YELLOW+"QUARTER TANK Of Gas\nPlan On Visiting The Gas Station"+Fore.RESET)
    elif gasLevelIndicator == "Half Tank":
        print(Fore.LIGHTGREEN_EX+"HALF TANK Of Gas\n125 Miles Till Empty"+Fore.RESET)
    elif gasLevelIndicator == "Three Quarter Tank":
        print(Fore.GREEN+"THREE QUARTER TANK Of Gas\n205 Miles Till Empty"+Fore.RESET)
    else:
        print(Fore.GREEN+"FULL TANK Of Gas\n310 Miles Till Empty"+Fore.RESET)

# Weather Branch

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

# Call Functions Here
gasLevelAlert()
sleep(1)
vehicleResponseSystem()

