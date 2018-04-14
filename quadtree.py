import json


class Point:
    def __init__(self, lat, lng, OutOfService, Critical, CriticalNotes):
        self.lat = float(lat)
        self.lng = float(lng)
        self.OutOfService = bool(OutOfService)
        self.Critical = bool(Critical)
        self.CriticalNotes = str(CriticalNotes)

    def __str__(self):
        return "({}, {})".format(self.lat, self.lng)

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

    def remove(self, pt):
        all_pts = self.get_all_pts()

        try:
            all_pts.remove(pt)
            return self.build_tree(all_pts)
        except ValueError:
            return self

    def build_tree(self, inputs, boundary=None):
        points = []
        if isinstance(inputs, str):
            j = json.loads(inputs.replace('\'', '"'))
            for pt in j:
                points.append(
                    Point(pt['lat'], pt['lng'], pt['OutOfService'], pt['Critical'], pt['CriticalNotes']))
        else:
            for pt in inputs:
                points.append(Point(pt.lat, pt.lng, pt.OutOfService, pt.Critical, pt.CriticalNotes))
        qt = QuadTree(self.boundary)

        for pt in points:
            qt.insert(pt)

        return qt

    def insert(self,
               point: Point):  # tries to insert into qt, if there are too manu points in the quad, splits and tries inserting recursively
        if len(self.points) < self.max_points and point.lat < self.boundary[0] + self.boundary[2] and point.lat >= \
                self.boundary[0] and point.lng < self.boundary[1] + self.boundary[3] and point.lng >= self.boundary[1]:
            if self.children[0] is None:
                self.points.append(point)
            else:
                for child in self.children:
                    if child.insert(point):
                        break
            return True
        elif len(self.points) >= self.max_points and point.lat < self.boundary[0] + self.boundary[2] and point.lat >= \
                self.boundary[0] and point.lng < self.boundary[1] + self.boundary[3] and point.lng >= self.boundary[1]:
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
