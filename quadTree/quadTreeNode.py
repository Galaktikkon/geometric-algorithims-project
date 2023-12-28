from geometry.Rectangle import Rectangle
from geometry.Point import Point


class quadTreeNode:

    def __init__(self, capacity: int, boundary: Rectangle):
        self.boundary = boundary
        self.capacity = capacity
        self.points: list[Point] = []
        self.northWest: quadTreeNode = None
        self.northEast: quadTreeNode = None
        self.southWest: quadTreeNode = None
        self.southEast: quadTreeNode = None
        self.isLeaf: bool = True

    def insert(self, point: Point) -> bool:

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

    def __divide(self):
        lowerLeft = self.boundary.lowerLeft
        upperRight = self.boundary.upperRight

        xLine = (lowerLeft.x()+upperRight.x())/2
        yLine = (lowerLeft.y()+upperRight.y())/2

        lowerRectangle, upperRectangle = self.boundary.divideRectIntoTwo(
            1,
            yLine
        )
        northWestRectangle, northEastRectangle = upperRectangle.divideRectIntoTwo(
            0,
            xLine
        )
        southWestRectangle, southEastRectangle = lowerRectangle.divideRectIntoTwo(
            0,
            xLine
        )

        self.northWest = quadTreeNode(self.capacity, northWestRectangle)
        self.northEast = quadTreeNode(self.capacity, northEastRectangle)
        self.southWest = quadTreeNode(self.capacity, southWestRectangle)
        self.southEast = quadTreeNode(self.capacity, southEastRectangle)

        self.isLeaf = False

    def search(self, rect: Rectangle) -> set[Point]:

        if not rect.intersects(self.boundary):
            return set()

        if rect.containsRect(self.boundary):
            return set(self.points)

        if rect.intersects(self.boundary):
            if self.isLeaf:
                return set(filter(lambda point: rect.containsPoint(point),  self.points))
            else:
                return self.northWest.search(rect) | \
                    self.northEast.search(rect) | \
                    self.southWest.search(rect) | \
                    self.southEast.search(rect)

    def draw(self, ax, lw=2):
        self.boundary.draw(ax, lw=lw)
        if not self.isLeaf:
            self.northWest.draw(ax, lw=lw*4/5)
            self.northEast.draw(ax, lw=lw*4/5)
            self.southWest.draw(ax, lw=lw*4/5)
            self.southEast.draw(ax, lw=lw*4/5)
