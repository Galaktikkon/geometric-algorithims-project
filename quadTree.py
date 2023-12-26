from Rectangle import Rectangle
from Point import Point
import matplotlib as plt
import numpy as np


class quadTreeNode:

    def __init__(self, capacity: int, boundary: Rectangle):
        self.boundary = boundary
        self.capacity = capacity
        self.points: list[Point] = []
        self.northWest: quadTreeNode = None
        self.northEast: quadTreeNode = None
        self.southWest: quadTreeNode = None
        self.southEast: quadTreeNode = None
        self.isLeaf = True

    def insert(self, point: Point):

        if not self.boundary.containsPoint(point):
            return False

        self.points.append(point)
        if self.capacity < len(self.points):
            if self.isLeaf:
                self.__divide()
                for p in self.points:
                    self.northWest.insert(p) \
                        or self.northEast.insert(p) \
                        or self.southWest.insert(p) \
                        or self.southEast.insert(p)
            else:
                self.northWest.insert(point) \
                    or self.northEast.insert(point) \
                    or self.southWest.insert(point) \
                    or self.southEast.insert(point)
        return True

    def __divide(self, ):
        lowerLeft = self.boundary.lowerLeft
        upperRight = self.boundary.upperRight

        xLine = (lowerLeft.x()+upperRight.x())/2
        yLine = (lowerLeft.y()+upperRight.y())/2

        lowerRectangle, upperRectangle = self.boundary.divideRectIntoTwo(
            1, yLine
        )
        northWestRectangle, northEastRectangle = upperRectangle.divideRectIntoTwo(
            0, xLine
        )
        southWestRectangle, southEastRectangle = lowerRectangle.divideRectIntoTwo(
            0, xLine
        )

        self.northWest = quadTreeNode(self.capacity, northWestRectangle)
        self.northEast = quadTreeNode(self.capacity, northEastRectangle)
        self.southWest = quadTreeNode(self.capacity, southWestRectangle)
        self.southEast = quadTreeNode(self.capacity, southEastRectangle)

        self.isLeaf = False

    def draw(self, ax):
        self.boundary.draw(ax)
        if not self.isLeaf:
            self.northWest.draw(ax)
            self.northEast.draw(ax)
            self.southWest.draw(ax)
            self.southEast.draw(ax)


class quadTree:

    def __init__(self, points: list[Point], maxPoints: int):

        assert len(points) > 0, "Quad tree cannot be empty"

        self.maxPoints = maxPoints
        self.root: quadTreeNode = None

        self.buildTree(points)

    def draw(self, ax):
        self.root.draw(ax)

    def __findBorders(self, points):
        lowerLeft: Point = points[0]
        upperRight: Point = points[0]

        for point in points:
            lowerLeft = lowerLeft.lowerLeft(point)
            upperRight = upperRight.upperRight(point)

        return lowerLeft, upperRight

    def buildTree(self, points):
        lowerLeft, upperRight = self.__findBorders(points)

        rootRectangle = Rectangle(lowerLeft, upperRight)

        self.root = quadTreeNode(self.maxPoints, rootRectangle)

        for point in points:
            self.root.insert(point)
