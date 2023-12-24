from Point import Point
from QuickSelect import quickSelect


class kdNode:
    def __init__(self, point: Point, dimDiv, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right
        self.dimDiv = dimDiv

    def __str__(self):
        return str(self.point)

    def __repr__(self):
        return str(self.point)


class kdTree:
    def __init__(self, points: list[Point]):
        assert len(points) > 0, 'KD-Tree cannot be initialized as empty'
        points = list(set(points))
        self.dim = points[0].dim
        assert all(
            point.dim == self.dim for point in points), 'Points must have same number of dimensions'
        self.root = self.buildTree(points, 0, len(points)-1)

    def addPoint(self, point: Point, dim):  # O(logn)
        p = self.root
        if p == None:
            self.root = kdNode(point, dim)
        q = None
        while p != None:
            q = p
            if point.isGreater(p.point, dim):
                p = p.right
            else:
                p = p.left
        if point.isGreater(q.point, dim):
            q.right = kdNode(point, dim)
        else:
            q.left = kdNode(point, dim)

    def buildTree(self, points, l, r, dim=0):
        if l > r:
            return None
        if l == r:
            return kdNode(points[l], dim)
        mid = (l+r)//2
        midPoint = quickSelect(points, l, r, mid, dim)
        newNode = kdNode(midPoint, dim)
        newNode.left = self.buildTree(points, l, mid-1, (dim+1) % self.dim)
        newNode.right = self.buildTree(points, mid+1, r, (dim+1) % self.dim)
        return newNode

    def printTree(self):
        def printSubTree(p: kdNode):
            if p != None:
                printSubTree(p.left)
                print(p, end=' ')
                printSubTree(p.right)
        printSubTree(self.root)
        print()
