from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    rst = []
    intervals.sort()

    i = 0
    while i < len(intervals) and newInterval[0] > intervals[i][1]:
        rst.append(intervals[i])
        i += 1


    while i < len(intervals) and newInterval[1] >= intervals[i][0]:
        newInterval[0] = min(intervals[i][0], newInterval[0])
        newInterval[1] = max(intervals[i][1], newInterval[1])
        i += 1
    rst.append(newInterval)

    while i < len(intervals):
        rst.append(intervals[i])
        i += 1
    
    return rst
    
    