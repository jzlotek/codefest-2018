from p5 import size, background, no_fill, run, stroke, rect, fill, ellipse
from web.python.quadtree import QuadTree, Point
import random
from web.python import csv_parser


def draw_box(qt):
    no_fill()
    stroke(255, 0, 0)
    rect((qt.boundary[0], qt.boundary[1]), qt.boundary[2], qt.boundary[3])

    fill(0, 255, 0)
    stroke(0, 255, 0)
    if len(qt.points) > 0:
        for pt in qt.points:
            ellipse([pt.x, pt.y], 1, 1)

    if qt.children[0] is not None:
        for child in qt.children:
            draw_box(child)


if __name__ == '__main__':
    height, width = 800, 800
    qt = QuadTree([0, 0, width, height])

    for x in range(0, 1000):
        # p = Point(random.random() * 500, random.random() * 500
        p = Point(random.gauss(width / 2, 80), random.gauss(height / 2, 80), False, False, None)
        qt.insert(p)

    search = [random.random() * width, random.random() * height, 100, 100]
    q = qt.query(search)

    print([str(pt) for pt in q])
    print(len(q))


    def setup():
        size(800, 800)
        background(0)


    def draw():
        draw_box(qt)
        no_fill()
        stroke(0, 0, 255)
        rect([search[0], search[1]], search[2], search[3])


    x = csv_parser.get_info()

    for pt in x[1:]:
        qt.insert(Point(pt['LONG'], pt['LAT'], False, False, None))

    try:
        run()
    except:
        pass
