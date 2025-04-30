# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/
from typing import List

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

print(merge(0, [[1,3],[2,6],[8,10],[15,18]]))
print(merge(0, [[1,4],[4,5]]))
