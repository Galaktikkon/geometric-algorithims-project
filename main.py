import random
from kd_Tree import kdTree
from Point import Point
from Point import createPointList
from Rectangle import Rectangle
A = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(18)]
points = createPointList(A)

tree = kdTree(points)
rect = Rectangle(Point((30, 80)), Point((50, 100)))
res = tree.searchKD(rect)
print(str(tree))
print("\n\n")
print(res)
print(len(res))
