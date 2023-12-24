import random
from kd_Tree import kdTree
from Point import Point
A = [(random.randint(10, 99), random.randint(10, 99)) for _ in range(12)]
points = [Point(cord) for cord in A]
for point in points:
    print(point, end=' ')
print()
tree = kdTree(points)
tree.printTree()
print(tree.root)
