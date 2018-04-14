from p5 import *
from quadtree import QuadTree, Point

height, width = 800, 800
qt = QuadTree([0, 0, width, height])

import random
import csv_parser


for x in range(0, 1000):
    # p = Point(random.random() * 500, random.random() * 500
    p = Point(random.gauss(width / 2, 80), random.gauss(height / 2, 80))
    qt.insert(p)

search = [random.random()*width, random.random()*height, 100, 100]
q = qt.query(search)

print([str(pt) for pt in q])
print(len(q))


def setup():
    size(800,800)
    background(0)


def draw():
    qt.draw_box()
    no_fill()
    stroke(0,0,255)
    rect([search[0],search[1]],search[2],search[3])

x = csv_parser.get_info()

for pt in x[1:]:
    qt.insert(Point(pt['LONG'], pt['LAT']))


try:
    run()
except:
    pass
