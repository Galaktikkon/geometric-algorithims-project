from Rectangle import Rectangle
from Point import Point
import matplotlib as plt
import numpy as np


class quadTreeNode:
    def __init__(self, capacity: int, boundary: Rectangle):
        self.boundary = boundary
        self.capacity = capacity
        self.northWest = None
        self.northEast = None
        self.southWest = None
        self.southEast = None
        self.isLeaf = True


class quadTree:

    def __init__(self, maxPoints: int):
        self.maxPoints = maxPoints
        self.boundary

    def insert(self, points: list[Point]):
        pass

    def __divide(self, ):
        pass
