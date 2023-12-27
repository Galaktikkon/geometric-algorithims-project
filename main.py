import random
from kd_Tree import kdTree
from Point import Point
from Point import createPointList
from Rectangle import Rectangle
from quadTree import quadTree
import numpy as np
import matplotlib.pyplot as plt


A = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(18)]

A = [(82, 23), (36, 53), (34, 64), (67, 67), (71, 88), (59, 94),
     (20, 28), (25, 79), (23, 82), (26, 18), (74, 55), (22, 95)]
points = createPointList(A)

ax = plt.subplot()
tree = quadTree(points, 2, ax)
ax.scatter([p.x() for p in points], [p.y() for p in points], s=5)
# tree.draw(ax)
plt.show()

tree = kdTree(points)
rect = Rectangle(Point((30, 80)), Point((50, 100)))
res = tree.searchKD(rect)
print(str(tree))
print("\n\n")
print(res)
print(len(res))
