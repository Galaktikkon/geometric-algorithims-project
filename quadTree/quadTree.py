from geometry.Rectangle import Rectangle
from geometry.Point import Point
from quadTree.quadTreeNode import quadTreeNode


class quadTree:

    def __init__(self, points: list[Point], maxPoints: int):

        assert len(points) > 0, "Quad tree cannot be empty"

        self.maxPoints = maxPoints
        self.root: quadTreeNode = None

        self.__buildTree(points)

    def draw(self, ax):
        self.root.draw(ax)

    def __findBorders(self, points) -> tuple[Point]:
        lowerLeft: Point = points[0]
        upperRight: Point = points[0]

        for point in points:
            lowerLeft = lowerLeft.lowerLeft(point)
            upperRight = upperRight.upperRight(point)

        return lowerLeft, upperRight

    def __buildTree(self, points):
        lowerLeft, upperRight = self.__findBorders(points)

        rootRectangle = Rectangle(lowerLeft, upperRight)

        self.root = quadTreeNode(self.maxPoints, rootRectangle)

        for point in points:
            self.root.insert(point)

    def search(self, rect: Rectangle) -> list[Point]:
        return self.root.search(rect)
