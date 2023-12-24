import Point
import numpy as np


class Rectangle:
    def __init__(self, point1: Point, point2: Point) -> None:
        self.lowerLeft = point1.lowerLeft(point2)
        self.upperRight = point1.upperRight(point2)
        self.dim = point1.dim

    def __str__(self):
        return self.lowerLeft + ' - ' + self.upperRight

    def contains(self, point: Point):
        return point.follows(self.lowerLeft) and point.precedes(self.upperRight)
