import random
from kd_Tree import kdTree
from Point import Point
from quadTree import quadTree
import numpy as np
import matplotlib.pyplot as plt
from Rectangle import Rectangle


# A = [(random.randint(10, 99), random.randint(10, 99)) for _ in range(12)]
A = [(82, 23), (36, 53), (34, 64), (67, 67), (71, 88), (59, 94),
     (20, 28), (25, 79), (23, 82), (26, 18), (74, 55), (22, 95)]
points = [Point(cord) for cord in A]

ax = plt.subplot()
tree = quadTree(points, 2, ax)
ax.scatter([p.x() for p in points], [p.y() for p in points], s=5)
# tree.draw(ax)
plt.show()
