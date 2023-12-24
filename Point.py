import numpy as np


class Point:
    def __init__(self, data: tuple) -> None:
        self.data = data  # krotka wspolrzednych
        self.dim = len(self.data)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return np.array_equal(self.data, other.data)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

    def __hash__(self):
        return hash(self.data)

    def x(self):
        return self.data[0]

    def y(self):
        assert self.dim > 1, 'Point is 1-D'
        return self.data[1]

    def get_dim(self, i: int):
        assert self.dim > i-1, 'Point has too few dimensions'
        return self.data[i]

    def isGreater(self, other, dim):
        assert isinstance(
            other, Point), 'Object has to be an instance of Point class'
        assert self.dim == other.dim, 'Points have different number of dimensions'
        assert self.dim > dim, 'Points have too few dimensions'
        return self.data[dim] >= other.data[dim]

    def precedes(self, other) -> bool:
        assert isinstance(
            other, Point), 'Object has to be an instance of Point class'
        assert self.dim == other.dim, 'Points have different number of dimensions'
        for i in range(self.dim):
            if self.data[i] > other.data[i]:
                return False
        return True

    def follows(self, other) -> bool:
        assert isinstance(
            other, Point), 'Object has to be an instance of Point class'
        assert self.dim == other.dim, 'Points have different number of dimensions'
        for i in range(self.dim):
            if self.data[i] < other.data[i]:
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
