from geometry.Point import Point
from visualiser.visualiser import Visualiser


class kdTreeNode:
    def __init__(self, axis, dim, rect, children, left=None, right=None):
        self.left = left
        self.right = right
        self.axis = axis
        self.rect = rect
        self.dim = dim
        self.children = children

    def __str__(self):
        s = str(self.axis)
        if self.dim == 0:
            s += " | "
        if self.dim == 1:
            s += " -- "
        return s

    def __repr__(self):
        return str(self.axis)

    def allLeaves(self):
        return self.children

    def countLeaves(self):
        return len(self.children)

    def draw(self, vis: Visualiser, lw=2):
        if not isinstance(self, Point):
            vis.drawLineInRect2D(self.rect, self.axis, self.dim, lw)
        if not isinstance(self.left, Point):
            self.left.draw(vis, lw=lw*4/5)
        if not isinstance(self.right, Point):
            self.right.draw(vis, lw=lw*4/5)
