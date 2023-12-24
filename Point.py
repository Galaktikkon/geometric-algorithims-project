import numpy as np


class Point:
    def __init__(self, data) -> None:
        self.point = np.array(data)
        self.dim = len(self.point)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return np.array_equal(self.point, other.point)

    def __str__(self):
        return str(self.point)

    def x(self):
        return self.point[0]

    def y(self):
        assert self.dim > 1, 'Point is 1-D'
        return self.point[1]

    def get_dim(self, i: int):
        assert self.dim > i-1, 'Point has too few dimensions'
        return self.point[i]

    def precedes(self, other) -> bool:
        assert isinstance(
            other, Point), 'Object has to be an instance of Point class'
        assert self.dim == other.dim, 'Points have different number of dimensions'
        for i in range(self.dim):
            if self.point[i] > other.point[i]:
                return False
        return True

    def follows(self, other) -> bool:
        assert self.dim == other.dim, 'Points have different number of dimensions'
        for i in range(self.dim):
            if self.point[i] < other.point[i]:
                return False
        return True

    def lowerLeft(self, other):
        assert isinstance(
            other, Point), 'Object has to be an instance of Point class'
        assert self.dim == other.dim, 'Points have different number of dimensions'
        arr = [0 for _ in range(self.dim)]
        for i in range(self.dim):
            arr[i] = min(self.get_dim[i], other.get_dim[i])
        return Point(arr)

    def upperRight(self, other):
        assert isinstance(
            other, Point), 'Object has to be an instance of Point class'
        assert self.dim == other.dim, 'Points have different number of dimensions'
        arr = [0 for _ in range(self.dim)]
        for i in range(self.dim):
            arr[i] = max(self.get_dim[i], other.get_dim[i])
        return Point(arr)
