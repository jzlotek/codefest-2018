from p5 import *


class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


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
            print("SUBDIVIDE")
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
    pass


def setup():
    size(width, height)
    background(0)


def draw():
    p = Point(random.gauss(width / 2, 40), random.gauss(height / 2, 40))
    print(p)
    qt.insert(p)
    qt.draw_box()

    # pass


try:
    run()
except:
    pass
