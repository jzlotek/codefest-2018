from quadtree import QuadTree, Point, calculate_boundaries
import json


def build_tree(inputs, boundary=None):
    points = build_list(inputs)

    if boundary is None:
        # calculate boundary conditions
        boundary = calculate_boundaries(points)
        qt = QuadTree(boundary)
    else:
        qt = QuadTree(boundary)

    print(len(points))
    for pt in points:
        qt.insert(pt)

    return qt


def build_list(inputs):
    points = []

    if isinstance(inputs, str):
        j = json.loads(inputs.replace('\'', '"'))
        for pt in j:
            points.append(
                Point(pt['lat'], pt['lng'], pt['OutOfService'], pt['Critical'], pt['CriticalNotes']))
    else:
        for pt in inputs:
            points.append(Point(pt.lat, pt.lng, pt.OutOfService, pt.Critical, pt.CriticalNotes))

    return points


string = ""
with open('hydrants.json', 'r') as file:
    for line in file:
        string += line
l = build_list(string)


def remove_from_tree(qt: QuadTree, pt: Point):
    all_pts = qt.get_all_pts()
    print(len(all_pts))
    try:
        all_pts.remove(pt)
        return build_tree(all_pts)
    except ValueError:
        return qt


def get_closest_to_point(hydrant_locations, point: Point, max=5):
    sorted_list = sorted(hydrant_locations, key=lambda pt: (point.lat - pt.lat) ** 2 + (point.lng - pt.lng) ** 2,
                         reverse=True)
    #for p in sorted_list:
    #     print(str(p))

    if len(sorted_list) < max:
        return sorted_list
    else:
        return [pt for pt in sorted_list[:max]]

    closest = []
    itr = 0
    while len(closest < 5):
        pt = sorted_list[itr]
        if(pt.OutOfService):
            itr+=1
        else:
            closest.append(pt)
            itr+=1

    print(closest)

if __name__ == "__main__":
    p = get_closest_to_point(l, l[5])
    for pt in p:
        print(str(pt))
    # tree = build_tree(string)
    #
    # print(len(tree.get_all_pts()))
    #
    # tree = remove_from_tree(tree, Point(39.883289, -75.052684, False, False, None))
    #
    # print(len(tree.get_all_pts()))

    # for pt in tree.get_all_pts():
    #     print(str(pt))
