import requests
import json
from hydraview.quadtree import Point

config = json.load(open("./api.json", 'r'))


def get_gps_location(path):
    r = requests.get(
        'https://maps.googleapis.com/maps/api/geocode/json?address={}&key={}'.format(path,
                                                                                     config.get(
                                                                                         'google_maps_geocoding')))
    s = str(r.json()).replace('\'', '"')
    j = json.loads(s)

    # formatted_json_string = json.dumps(j, sort_keys=True, indent=4)
    # print(formatted_json_string)

    coords = []
    for res in j.get('results'):
        coords.append(res.get('geometry').get('location'))

    points = []
    for c in coords:
        points.append(Point(c.get('lat'), c.get('lng'), False, False, None))

    return points


if __name__ == "__main__":
    pass
    # points = get_gps_location()
    # print([str(pt) for pt in points])
