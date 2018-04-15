if __name__ == "__main__":
    import requests
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    location = "3300 Lancaster Avenue Philadelphia, Pennsylvania"
    params = {'sensor': 'false', 'address': location}
    r = requests.get(url, params=params)
    results = r.json()['results']
    location = results[0]['geometry']['location']
    print(location['lat'])
    print(location['lng'])

    import geocoder
    g = geocoder.ipinfo('me')
    print(g.latlng)
