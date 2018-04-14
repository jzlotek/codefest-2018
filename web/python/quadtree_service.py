from web.python.quadtree import QuadTree, Point, calculate_boundaries
import json


def build_tree(inputs, boundary=None):
    points = []
    if isinstance(inputs, str):
        j = json.loads(inputs.replace('\'', '"'))
        for pt in j:
            points.append(
                Point(pt['lat'], pt['lng'], pt['OutOfService'], pt['Critical'], pt['CriticalNotes']))
    else:
        for pt in inputs:
            points.append(Point(pt.lat, pt.lng, pt.OutOfService, pt.Critical, pt.CriticalNotes))

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


def remove_from_tree(qt: QuadTree, pt: Point):
    all_pts = qt.get_all_pts()
    print(len(all_pts))
    try:
        all_pts.remove(pt)
        return build_tree(all_pts)
    except ValueError:
        return qt


string = ""
with open('hydrants.json', 'r') as file:
    for line in file:
        string += line

tree = build_tree(string)

print(len(tree.get_all_pts()))

tree = remove_from_tree(tree, Point(39.883289, -75.052684, False, False, None))

print(len(tree.get_all_pts()))

# for pt in tree.get_all_pts():
#     print(str(pt))
