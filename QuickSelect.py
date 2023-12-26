import random


def rand_partition(points, p, r, dim=0):
    def partition(points, p, r):
        x = points[r].get_dim(dim)
        i = p-1
        for j in range(p, r):
            if points[j].get_dim(dim) <= x:
                i += 1
                points[j], points[i] = points[i], points[j]
        i += 1
        points[i], points[r] = points[r], points[i]
        return i
    num = random.randint(p, r)
    points[num], points[r] = points[r], points[num]
    return partition(points, p, r)


def quickSelect(points, l, r, k, dim=0):
    q = rand_partition(points, l, r, dim)
    if q == k:
        return points[q]
    if q > k:
        return quickSelect(points, l, q-1, k, dim)
    return quickSelect(points, q+1, r, k, dim)
