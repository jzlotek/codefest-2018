import csv


def get_info():
    with open('hydrants.csv', newline='\n') as file:
        csvreader = csv.DictReader(file)
        return [row for row in csvreader]

if __name__ == "__main__":

    c = get_info()

    points = []

    from quadtree import Point

    for row in c:
        points.append(Point(row['LAT'], row['LONG'], False, False, None))

    for pt in points:
        print(str(pt))

    def jsonify(li):
        j = "["
        for i, e in enumerate(li):
            if i < len(li) - 1:
                j += (str(e.toJSON()) + ',')
            else:
                j += str(e.toJSON())
        return j + "]"

    with open('drexel_json.json', 'w') as file:
        file.write(jsonify(points))
