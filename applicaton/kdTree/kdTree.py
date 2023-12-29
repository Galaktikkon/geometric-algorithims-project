from geometry.Point import Point
from applicaton.QuickSelect import quickSelect
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

    def __str__(self):
        return self.display()

    def __repr__(self):
        return self.display()

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

    def searchKD(self, rectangle: Rectangle):

        def search(p, rect: Rectangle):
            self.counter += 1
            if isinstance(p, Point):
                if rect.containsPoint(p):
                    return [p]
            elif rect.containsRect(p.rect):
                return p.allLeaves()
            elif rectangle.intersects(p.rect):
                res = []
                res += search(p.left, rect)
                res += search(p.right, rect)
                return res
            return []
        return search(self.root, rectangle)

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

    def display(self):
        def _display_aux(root: kdTreeNode):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if isinstance(root, Point):
                line = str(root)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if root.right is None:
                lines, n, p, x = _display_aux(root.left)
                s = str(root)
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if root.left is None:
                lines, n, p, x = _display_aux(root.right)
                s = str(root)
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
            # Two children.
            left, n, p, x = _display_aux(root.left)
            right, m, q, y = _display_aux(root.right)
            s = str(root)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * \
                '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + \
                (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + \
                [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2
        lines, *_ = _display_aux(self.root)
        s = ""
        for line in lines:
            s += line
            s += '\n'
        return s

    def drawTree(self, ax):
        def draw(root, ax, lw):
            if not isinstance(root, Point):
                # print(root.axis, self.dim)
                root.rect.drawLineInRect2D(ax, root.axis, root.dim, lw)
                draw(root.left, ax, lw*4/5)
                draw(root.right, ax, lw*4/5)
        draw(self.root, ax, 2)
