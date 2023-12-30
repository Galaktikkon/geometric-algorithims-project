import random
from geometry.Point import Point
from geometry.Point import createPointList
from geometry.Rectangle import Rectangle
from quadTree.quadTree import quadTree
import numpy as np
import matplotlib.pyplot as plt
A = [(random.randint(-1000, 1000), random.randint(-1000, 1000))
     for _ in range(200)]
points = createPointList(A)

rect = Rectangle(Point((random.randint(-1000, 1000), random.randint(-1000, 1000))), Point(
    (random.randint(-1000, 1000), random.randint(-1000, 1000))))


ax = plt.subplot()
tree = quadTree(points, 1)
ax.scatter([p.x() for p in points], [p.y() for p in points], s=5)
rect.draw(ax, c='red')
tree.draw(ax)

points = tree.search(rect)
print(points)
ax.scatter([p.x() for p in points], [p.y() for p in points], s=8, c='red')

plt.show()
