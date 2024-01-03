from geometry.Rectangle import Rectangle
from geometry.Point import Point
from visualiser.visualiser import Visualiser
from time import sleep


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

    def insertVis(self, point: Point, vis: Visualiser, lw) -> bool:

        if not self.boundary.containsPoint(point):
            bad = vis.drawRectangle(self.boundary, c='red')
            sleep(0.5)
            bad.remove()
            return False

        self.points.append(point)
        if self.capacity < len(self.points):
            if self.isLeaf:
                divide = vis.drawRectangle(self.boundary, c='green')
                sleep(0.5)
                divide.remove()
                self.__divideVis(vis, lw*4/5)
                for p in self.points:
                    self.northWest.insertVis(p, vis, lw*4/5) \
                        or self.northEast.insertVis(p, vis, lw*4/5) \
                        or self.southWest.insertVis(p, vis, lw*4/5) \
                        or self.southEast.insertVis(p, vis, lw*4/5)
            else:
                divide = vis.drawRectangle(self.boundary, c='yellow')
                sleep(0.5)
                divide.remove()
                self.northWest.insertVis(point, vis, lw*4/5) \
                    or self.northEast.insertVis(point, vis, lw*4/5) \
                    or self.southWest.insertVis(point, vis, lw*4/5) \
                    or self.southEast.insertVis(point, vis, lw*4/5)
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

    def __divideVis(self, vis: Visualiser, lw):
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

        vis.drawRectangle(northWestRectangle, lw=lw)
        vis.drawRectangle(northEastRectangle, lw=lw)
        vis.drawRectangle(southWestRectangle, lw=lw)
        vis.drawRectangle(southEastRectangle, lw=lw)
        sleep(0.5)

        self.northWest = quadTreeNode(self.capacity, northWestRectangle)
        self.northEast = quadTreeNode(self.capacity, northEastRectangle)
        self.southWest = quadTreeNode(self.capacity, southWestRectangle)
        self.southEast = quadTreeNode(self.capacity, southEastRectangle)

        self.isLeaf = False

    def search(self, rect: Rectangle) -> list[Point]:

        if not rect.intersects(self.boundary):
            return []

        if rect.containsRect(self.boundary):
            return self.points

        output = []
        if rect.intersects(self.boundary):
            if self.isLeaf:
                return list(filter(lambda point: rect.containsPoint(point),  self.points))
            else:
                output += self.northWest.search(rect)
                output += self.northEast.search(rect)
                output += self.southWest.search(rect)
                output += self.southEast.search(rect)

        return output

    def searchVis(self, rect: Rectangle, vis, lw) -> list[Point]:

        if not rect.intersects(self.boundary):
            bad = vis.drawRectangle(self.boundary, c='red', lw=lw)
            sleep(0.5)
            bad.remove()
            sleep(0.5)
            return []

        if rect.containsRect(self.boundary):
            good = vis.drawRectangle(self.boundary, c='cyan', lw=lw)
            sleep(0.5)
            good.remove()
            sleep(0.5)
            vis.drawPoints(self.points, color='cyan', markersize=9)
            sleep(0.5)
            return self.points

        output = []
        if rect.intersects(self.boundary):
            ok = vis.drawRectangle(self.boundary, c='green', lw=lw)
            sleep(0.5)
            ok.remove()

            if self.isLeaf:
                goodPoints = list(
                    filter(lambda point: rect.containsPoint(point),  self.points))
                vis.drawPoints(goodPoints, color='green', markersize=9)
                sleep(0.5)
                return goodPoints
            else:
                output += self.northWest.searchVis(rect, vis, lw*4/5)
                output += self.northEast.searchVis(rect, vis, lw*4/5)
                output += self.southWest.searchVis(rect, vis, lw*4/5)
                output += self.southEast.searchVis(rect, vis, lw*4/5)

        return output

    def draw(self, vis: Visualiser, lw=2):
        vis.drawRectangle(self.boundary, lw=lw)
        if not self.isLeaf:
            self.northWest.draw(vis, lw=lw*4/5)
            self.northEast.draw(vis, lw=lw*4/5)
            self.southWest.draw(vis, lw=lw*4/5)
            self.southEast.draw(vis, lw=lw*4/5)
