# 973. K Closest Points to Origin
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

import heapq

def kClosest(points, k):
    # sol1
    # points.sort(key=lambda x: x[0]**2 + x[1]**2)
    # return points[:k]

    #sol 2 
    # hp = []
    # for x, y in points:
    #     dist = x**2 + y**2
    #     hp.append([dist, x, y])
    # heapq.heapify(hp)
    # res = []
    # for _ in range(k):
    #     dist, x, y = heapq.heappop(hp)
    #     res.append([x, y])
    # return res

    #sol3
    hp = []
    for point in points:
        dist = point[0]**2 + point[1]**2
        heapq.heappush(hp, (-dist, point))
        if len(hp) > k:
            heapq.heappop(hp)
    res = []
    while hp:
        dist, point = heapq.heappop(hp)
        res.append(point)
    res.reverse()
    return res

print(kClosest([[1,3],[-2,2]], 1))
print(kClosest([[3,3],[5,-1],[-2,4]], 2))