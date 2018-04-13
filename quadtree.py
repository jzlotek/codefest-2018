from p5 import *


class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


def intersects(r1, r2):
    return not (r1[0] + r1[2] < r2[0] or r1[0] > r2[0] + r2[2] or r1[1] + r1[3] < r2[1] or r1[1] > r2[1] + r2[3])


class QuadTree:
    def __init__(self, boundary, max_points=4):
        self.boundary = boundary  # (x1,y1,width,height)
        self.children = [None, None, None, None]  # UL, UR, LL, LR
        self.points = []
        self.max_points = max_points

    def subdivide(self):
        half_width = self.boundary[2] / 2
        half_height = self.boundary[3] / 2
        self.children[0] = QuadTree([self.boundary[0], self.boundary[1], half_width, half_height])
        self.children[1] = QuadTree([self.boundary[0] + half_width, self.boundary[1], half_width, half_height])
        self.children[2] = QuadTree([self.boundary[0], self.boundary[1] + half_height, half_width, half_height])
        self.children[3] = QuadTree(
            [self.boundary[0] + half_width, self.boundary[1] + half_height, half_width, half_height])

    def draw_box(self):
        no_fill()
        stroke(255, 0, 0)
        rect((self.boundary[0], self.boundary[1] + self.boundary[3]), self.boundary[2], self.boundary[3])

        fill(0, 255, 0)
        stroke(0, 255, 0)
        if len(self.points) > 0:
            for pt in self.points:
                ellipse([pt.x, pt.y], 1, 1)

        if self.children[0] is not None:
            for child in self.children:
                child.draw_box()

    def query(self, region):
        points = []
        if not intersects(region, self.boundary):
            return points
        elif self.children[0] is None:
            for pt in self.points:
                if pt.x <= region[0] + region[2] and \
                        pt.y <= region[1] + region[3]:
                    points.extend(pt)
        else:
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

    def insert(self, point: Point):
        if len(self.points) < self.max_points and point.x < self.boundary[0] + self.boundary[2] and point.x >= \
                self.boundary[0] and point.y < self.boundary[1] + self.boundary[3] and point.y >= self.boundary[1]:

            if self.children[0] is None:
                self.points.append(point)
            else:
                for child in self.children:
                    if child.insert(point):
                        break

            return True
        elif len(self.points) >= self.max_points and point.x < self.boundary[0] + self.boundary[2] and point.x >= \
                self.boundary[0] and point.y < self.boundary[1] + self.boundary[3] and point.y >= self.boundary[1]:
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


height, width = 800, 800
qt = QuadTree([0, 0, width, height])

import random

for x in range(0, 1000):
    # p = Point(random.random() * 500, random.random() * 500)
    p = Point(random.gauss(width / 2, 40), random.gauss(height / 2, 40))
    qt.insert(p)

q = qt.query([0, 0, 250, 250])

print([str(pt) + "\n" for pt in q])
print(len(q))


def setup():
    size(width, height)
    background(0)


def draw():
    qt.draw_box()


try:
    run()
except:
    pass
