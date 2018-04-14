from quadtree import QuadTree, Point, calculate_boundaries
import json
from math import sin, cos, sqrt, atan2, radians
import requests

url = 'https://maps.googleapis.com/maps/api/geocode/json'
location = "3300 Lancaster Avenue Philadelphia, Pennsylvania"
params = {'sensor': 'false', 'address': location}
r = requests.get(url, params=params)
results = r.json()['results']
location = results[0]['geometry']['location']
lon1 = (location['lat'])
lat1 = (location['lng'])

# approximate radius of earth in km
R = 6373.0
length_list = []

string = ""
with open('hydrants.json', 'r') as file:
    for line in file:
        string += line
print(string.points)

lat2 = radians(52.406374)
lon2 = radians(16.9251681)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print("Result:", distance)
print("Should be:", 278.546, "km")
