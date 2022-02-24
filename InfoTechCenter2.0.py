# Weather Branch

import random

def weather():
    weatherForecast = ["Ice", "Snow", "Heavy Rain", "Rain", "High Wind", "Fog", "Sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

# Calling weather function to determine weather
weatherAlert = weather()

print(weatherAlert)
