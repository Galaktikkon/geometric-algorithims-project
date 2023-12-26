import Point
import numpy as np


class Rectangle:  # jeszcze nieprzydatne ale moze mi sie przyda do jakiejs wizualizacji czy cos
    def __init__(self, point1: Point, point2: Point) -> None:
        self.lowerLeft = point1.lowerLeft(point2)
        self.upperRight = point1.upperRight(point2)
        self.dim = point1.dim

    def __str__(self):
        return self.lowerLeft + ' - ' + self.upperRight

    def contains(self, point: Point):
        return point.follows(self.lowerLeft) and point.precedes(self.upperRight)

    def draw(self, ax, c='k', lw=1, **kwargs):
        x1, y1 = self.lowerLeft.x(), self.lowerLeft.y()
        x2, y2 = self.upperRight.x(), self.upperRight.y()
        ax.plot([x1, x2, x2, x1, x1],
                [y1, y1, y2, y2, y1], c=c, lw=lw, **kwargs)
