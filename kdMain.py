import random
from kdTree.kdTree import kdTree
from geometry.Point import Point
from geometry.Point import createPointList
from geometry.Rectangle import Rectangle
from quadTree.quadTree import quadTree
import numpy as np
import matplotlib.pyplot as plt


A = [(random.randint(0, 20000), random.randint(0, 20000))
     for _ in range(200)]

points = createPointList(A)


tree = kdTree(points)
rect = Rectangle(Point((100, 1000)), Point((4000, 8000)))
rect = Rectangle(Point((random.randint(0, 20000), random.randint(0, 20000))), Point(
    (random.randint(0, 20000), random.randint(0, 20000))))

print("\n\n")
res = tree.searchKD(rect)
# print(res)aw
print(tree.countKD(rect))
# print(tree.counter)
ax = plt.subplot()
tree.draw(ax)
rect.draw(ax, c='red', lw=3)
ax.scatter([p.x() for p in points], [p.y() for p in points], s=10)
ax.scatter([p.x() for p in res], [p.y() for p in res], c='blue', s=15)

# rect.drawLineInRect2D(ax, 10000, 0)
plt.show()
