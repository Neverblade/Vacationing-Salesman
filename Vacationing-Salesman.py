API_KEY = "AIzaSyD3AlCKqOHaQPkrKYUXgYpOqkm7khPYGWw"
CORE_URL = "https://maps.googleapis.com/maps/api/geocode/json?address="
radius = 6378137 # Radius of the earth, in meters.

import sys
import requests
import math

# Converts the given value from meters to the specified unit. Returns meters by default.
def convert(value, convertTarget):
    if convertTarget == "kilometers":
        return value / 1000
    elif convertTarget == "miles":
        return value * 0.000621371
    else:
        return value

# Helper method for findStraightDistance.
def radians(x):
    return x * math.pi / 180

# Finds the straight global distance between two coordinate points. Uses the haversine formula.
def findStraightDistance(p1, p2):
    dLat = radians(p2["lat"] - p1["lat"])
    dLong = radians(p2["lng"] - p1["lng"])
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(radians(p1["lat"])) * math.cos(radians(p2["lat"])) * math.sin(dLong / 2) * math.sin(dLong / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c
    return d

# Reads in input from stdin, then performs the GET request to retrieve coordinate points.
def readInput():
    cities = sys.stdin.read().splitlines()
    coordinates = []
    for city in cities:
        url = CORE_URL + city + "&key=" + API_KEY
        r = requests.get(url)
        coordinates.append(r.json()["results"][0]["geometry"]["location"])
    return cities, coordinates
    
# Finds and outputs distance between cities in a given itinerary.
def processStraightDistances():
    unit = "miles"
    cities, coordinates = readInput()
    if len(cities) == 0:
        print("You're not traveling anywhere! Try added more cities.")
        return
    sum = 0
    print("Success! Your vacation itinerary is:")
    for i in range(1, len(coordinates)):
        distance = findStraightDistance(coordinates[i - 1], coordinates[i])
        sum += distance
        print("\t" + cities[i - 1] + " -> " + cities[i] + ": " + str(round(convert(distance, unit), 2)) + " " + unit)
    print("\nTotal distance covered in your trip: " + str(round(convert(sum, unit), 2)) + " " + unit)
    

processStraightDistances()
    