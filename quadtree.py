import json

const_range = 0


def calculate_boundaries(points: list):
    lng, lat, w, h = points[0].lng, points[0].lat, points[0].lng, points[0].lat

    for pt in points[1:]:
        # print(pt)
        if pt.lng < lng:
            lng = pt.lng - const_range
        elif w < pt.lng:
            w = pt.lng + const_range

        if pt.lat < lat:
            lat = pt.lat - const_range
        elif h < pt.lat:
            h = pt.lat + const_range

    return [lng, h, abs(w - lng), abs(h - lat)]


class Point:
    def __init__(self, lat, lng, OutOfService, Critical, CriticalNotes):
        self.lat = float(lat)
        self.lng = float(lng)
        self.OutOfService = bool(OutOfService)
        self.Critical = bool(Critical)
        self.CriticalNotes = str(CriticalNotes)

    def __str__(self):
        return "({}, {})".format(self.lng, self.lat)

    def __eq__(self, other):
        return self.lat == other.lat and self.lng == other.lng and self.OutOfService == other.OutOfService and self.Critical == other.Critical and self.CriticalNotes == other.CriticalNotes


def intersects(r1, r2):
    return not (r1[0] + r1[2] < r2[0] or r1[0] > r2[0] + r2[2] or r1[1] + r1[3] < r2[1] or r1[1] > r2[1] + r2[3])


class QuadTree:
    def __init__(self, boundary, max_points=4):
        self.boundary = boundary  # (lng,lat,lng_lim,lat_lim)
        self.children = [None, None, None, None]  # UL, UR, LL, LR
        self.points = []
        self.max_points = max_points
        # print(boundary)

    def subdivide(self):  # recursively splits the qt into 4 children
        half_width = self.boundary[2] / 2
        half_height = self.boundary[3] / 2
        self.children[0] = QuadTree([self.boundary[0], self.boundary[1], half_width, half_height])
        self.children[1] = QuadTree([self.boundary[0] + half_width, self.boundary[1], half_width, half_height])
        self.children[2] = QuadTree([self.boundary[0], self.boundary[1] + half_height, half_width, half_height])
        self.children[3] = QuadTree(
            [self.boundary[0] + half_width, self.boundary[1] + half_height, half_width, half_height])

    def query(self, region):  # search region of [x,y,width,height] for points and returns array
        points = []
        if not intersects(region, self.boundary):
            return points
        elif self.children[0] is None and len(self.points) is not 0:
            for pt in self.points:
                if pt.lng <= region[0] + region[2] and \
                        pt.lat <= region[1] + region[3] and \
                        pt.lng >= region[0] and pt.lat >= region[1]:
                    points.append(pt)
        else:
            if self.children[0] is not None:
                for child in self.children:
                    points.extend(child.query(region))
        return points

    def get_all_pts(self):
        if self.children[0] is None:
            return self.points
        else:
            points = []
            for child in self.children:
                points.extend(child.get_all_pts())
            return points

    def contains(self, point):
        p1, p2, p3, p4 = self.boundary
        # print(point.lng >= p1)
        # print(point.lng <= p1 + p3)
        # print(point.lat <= p2)
        # print(point.lng >= p2 - p4)
        return point.lng >= p1 and point.lng <= p1 + p3 and point.lat <= p2 and point.lat >= p2 - p4

    def insert(self, point: Point):
        # tries to insert into qt, if there are too manu points in the quad, splits and tries inserting recursively
        print(len(self.points) < self.max_points and self.contains(point))
        print(len(self.points) >= self.max_points and self.contains(point))
        print()

        if len(self.points) < self.max_points and self.contains(point):
            if self.children[0] is None:
                self.points.append(point)
            else:
                for child in self.children:
                    if child.insert(point):
                        break
            return True
        elif len(self.points) >= self.max_points and self.contains(point):
            self.subdivide()

            for pt in self.points:
                for child in self.children:
                    if child.insert(pt):
                        break

            for child in self.children:
                if child.insert(point):
                    break
            self.points = []
        else:
            return False
