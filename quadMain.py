import random
from kd_Tree import kdTree
from Point import Point
from Point import createPointList
from Rectangle import Rectangle
from quadTree import quadTree
import numpy as np
import matplotlib.pyplot as plt
A = [(random.randint(-100, 100), random.randint(-100, 100))
     for _ in range(20)]
points = createPointList(A)

ax = plt.subplot()
tree = quadTree(points, 2)
ax.scatter([p.x() for p in points], [p.y() for p in points], s=5)
tree.draw(ax)
plt.show()
