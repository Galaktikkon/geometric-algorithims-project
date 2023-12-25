from Point import Point


class Rectangle:  # jeszcze nieprzydatne ale moze mi sie przyda do jakiejs wizualizacji czy cos
    def __init__(self, point1: Point, point2: Point) -> None:
        self.lowerLeft = point1.lowerLeft(point2)
        self.upperRight = point1.upperRight(point2)
        self.dim = point1.dim

    def __str__(self):
        return str(self.lowerLeft) + ' - ' + str(self.upperRight)

    def intersects(self, other):
        return self.lowerLeft.precedes(other.upperRight) and self.upperRight.follows(other.lowerLeft)

    def containsPoint(self, point: Point):
        return point.follows(self.lowerLeft) and point.precedes(self.upperRight)

    def containsRect(self, other):
        return other.lowerLeft.follows(self.lowerLeft) and other.upperRight.precedes(self.upperRight)

    def divideRect(self, dim, divLine):
        Lower = self.lowerLeft.data
        Upper = self.upperRight.data
        assert divLine <= Upper[dim] or divLine >= Lower[dim], 'Line does not belong to rectangle'
        lowerIntersection, upperIntersection = list(
            Lower), list(Upper)
        lowerIntersection[dim] = upperIntersection[dim] = divLine
        lowerIntersection, upperIntersection = tuple(
            lowerIntersection), tuple(upperIntersection)
        return (Rectangle(Point(Lower), Point(upperIntersection)), Rectangle(Point(lowerIntersection), Point(Upper)))
