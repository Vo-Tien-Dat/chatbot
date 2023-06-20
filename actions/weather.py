import requests
from geopy.geocoders import Nominatim
import json 


def get_location(place_name):
    loc = Nominatim(user_agent="GetLoc")
    getLoc = loc.geocode(place_name)
    lat =  getLoc.latitude
    loc = getLoc.longitude
    return [lat, loc]

def get_weather(lat, lon):
# argument in request
    url_weather = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":str(lat)+','+str(lon)}
    headers = {
	    "X-RapidAPI-Key": "6ccb3e8089msh897614c7165244dp18626ejsn71521dc60bc0",
	    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    response = requests.request("GET", url_weather, headers=headers, params=querystring)
    return response


def main():
    location =  get_location('Ho Chi Minh City')
    lat = location[0]
    lon = location[1]
    weather = get_weather(lat=lat, lon = lon)
    data = weather.json()
    return data['current']['temp_f']


def weather_location(place):
    location = get_location(place)
    lat = location[0]
    lon = location[1]
    weather = get_weather(lat = lat, lon = lon)
    data = weather.json()
    temp = data['current']['temp_f']
    return temp
