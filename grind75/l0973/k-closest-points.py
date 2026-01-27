from typing import List
from math import hypot


def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    points.sort(key=lambda point: hypot(point[0], point[1]))