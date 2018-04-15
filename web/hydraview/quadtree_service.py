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


def remove_from_tree(qt: QuadTree, pt: Point):
    all_pts = qt.get_all_pts()
    print(len(all_pts))
    try:
        all_pts.remove(pt)
        return build_tree(all_pts)
    except ValueError:
        return qt


from math import sin, cos, sqrt, atan2, radians

def cal_dist(p, point):
    R = 6373.0

    lat1 = point.lat
    lon1 = point.lng

    lat2 = p.lat
    lng2 = p.lng

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c


def get_closest_to_point(hydrant_locations, point: Point, max_num=5):
    sorted_list = sorted(hydrant_locations, key=lambda p: 2 * atan2(
        sqrt(sin(radians(point.lat) - p.lat / 2) ** 2 + cos(p.lat) * cos(radians(point.lat)) * sin(
            radians(point.lng) - p.lng / 2) ** 2),
        sqrt(1 - sin(radians(point.lat) - p.lat / 2) ** 2 + cos(p.lat) * cos(radians(point.lat)) * sin(
            radians(point.lng) - p.lng / 2) ** 2)) * 6373.0,
                         reverse=False)

    # sorted_list = sorted(hydrant_locations, key=lambda p: (point.lat - p.lat) ** 2 + (point.lng - p.lng) ** 2,
    #                      reverse=False)

    # print((point.lat - sorted_list[0].lat) ** 2 + (point.lng - sorted_list[0].lng) ** 2)
    # print((point.lat - sorted_list[1].lat) ** 2 + (point.lng - sorted_list[1].lng) ** 2)
    # print((point.lat - sorted_list[-2].lat) ** 2 + (point.lng - sorted_list[-2].lng) ** 2)
    # print((point.lat - sorted_list[-1].lat) ** 2 + (point.lng - sorted_list[-1].lng) ** 2)

    if len(sorted_list) < max_num:
        return sorted_list
    else:
        closest = []
        itr = 0
        while len(closest) < max_num and itr < len(sorted_list):
            pt = sorted_list[itr]
            if pt.OutOfService:
                itr += 1
            else:
                closest.append(pt)
                itr += 1

        # print(closest)
        return closest


if __name__ == "__main__":
    pass
    # p = get_closest_to_point(l, l[5])
    # for pt in p:
    #     print(str(pt))
    # tree = build_tree(string)
    #
    # print(len(tree.get_all_pts()))
    #
    # tree = remove_from_tree(tree, Point(39.883289, -75.052684, False, False, None))
    #
    # print(len(tree.get_all_pts()))

    # for pt in tree.get_all_pts():
    #     print(str(pt))
