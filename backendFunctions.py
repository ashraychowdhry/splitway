import requests
import json
import urllib.request
import datetime
def findCoordinates(address):
    address = address.replace(" ", "+")
    addressURL = "https://maps.googleapis.com/maps/api/geocode/json?address=" + address + "&key=AIzaSyCdaPXmz8jQexyn-kWR9rmiumUuLn3GgMs"
    with urllib.request.urlopen(addressURL) as url:
        data = json.loads(url.read().decode())
    lat = (data["results"][0]["geometry"]["location"]["lat"])
    lng = (data["results"][0]["geometry"]["location"]["lng"])
    coordinates = (lng, lat)
    return coordinates
def getDistance(address1, address2):
    address1 = address1.replace(" ", "+")
    address2 = address2.replace(" ", "+")
    distanceURL = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=" + address1 + "&destinations=" + address2 + "&units=imperial&mode=walking&language=en-EN&key=AIzaSyANMkW7bIUZCJI1jNM2l5hl1CpmXzVCpJg"
    with urllib.request.urlopen(distanceURL) as url:
        data = json.loads(url.read().decode())
    distance = data["rows"][0]["elements"][0]["distance"]["value"]
    distance = distance / 1609.344
    return distance
def timeFormatter(strTime1, strTime2):

def test():
    return(print(getDistance("1250 cobblemill way", "1259 cobblemill way")))
def newEvent(currentAddress, destinationAddress, eventTime, email, phone):
    #Will store a new event in the database
    numEvents += 1
def searchEvents(currentAddress, destinationAddress, eventTime): #incomplete requires DB info
    for i = 0 to numEvents:
        if getDistance(currentAddress, EVENTCURRENTADDRESS) < 0.25 and getDistance(destinationAddress, EVENTDESTINATIONADDRESS) < .25 **
        
test()