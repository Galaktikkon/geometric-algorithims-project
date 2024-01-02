from geometry.Point import Point
from kdTree.QuickSelect import quickSelect
from geometry.Rectangle import Rectangle
from math import inf
from kdTree.kdTreeNode import kdTreeNode


class kdTree:
    def __init__(self, points: list[Point]):
        assert len(points) > 0, 'KD-Tree cannot be initialized as empty'
        self.dim = points[0].dim
        assert all(
            point.dim == self.dim for point in points), 'Points must have same number of dimensions'
        self.root = self.buildTree(points)
        self.counter = 0

    def buildTree(self, points):
        def buildTreeRec(points: list[Point], l: int, r: int, rect: Rectangle, dim: int):
            if l > r:
                return None
            if l == r:
                return points[l]
            mid = (l+r)//2
            midPoint = quickSelect(points, l, r, mid, dim)
            newNode = kdTreeNode(midPoint.get_dim(
                dim), dim, rect, points[l:r+1])
            rectLeft, rectRight = rect.divideRectIntoTwo(
                dim, midPoint.get_dim(dim))
            newNode.left = buildTreeRec(
                points, l, mid, rectLeft, (dim+1) % self.dim)
            newNode.right = buildTreeRec(
                points, mid+1, r, rectRight, (dim+1) % self.dim)
            return newNode
        lowerLeft, upperRight = Point((inf, inf)), Point((-inf, -inf))
        for point in points:
            lowerLeft = lowerLeft.lowerLeft(point)
            upperRight = upperRight.upperRight(point)
        rectStart = Rectangle(lowerLeft, upperRight)
        return buildTreeRec(points, 0, len(points)-1, rectStart, 0)

    def search(self, rectangle: Rectangle):

        def searchKD(p, rect: Rectangle):
            self.counter += 1
            if isinstance(p, Point):
                if rect.containsPoint(p):
                    return [p]
            elif rect.containsRect(p.rect):
                return p.allLeaves()
            elif rectangle.intersects(p.rect):
                res = []
                res += searchKD(p.left, rect)
                res += searchKD(p.right, rect)
                return res
            return []
        return searchKD(self.root, rectangle)

    def countKD(self, rectangle: Rectangle):
        def count(p, rect: Rectangle):
            if isinstance(p, Point):
                if rect.containsPoint(p):
                    return 1
            elif rect.containsRect(p.rect):
                return p.countLeaves()
            elif rectangle.intersects(p.rect):
                res = 0
                res += count(p.left, rect)
                res += count(p.right, rect)
                return res
            return 0
        return count(self.root, rectangle)

    def draw(self, ax):
        self.root.draw(ax, lw=2)
