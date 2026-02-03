from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    rst = []
    if not intervals:
        return rst

    if len(intervals) <= 1:
        return intervals

    intervals.sort(key = lambda x: x[0])
    
    # index = 1
    # while index < len(intervals) and intervals[index][0] > intervals[index-1][1]:
    #     rst.append(intervals[index-1])
    #     index += 1
        
    # start, end = intervals[index][0], intervals[index][1]

    # while index < len(intervals) and intervals[index][0] <= intervals[index-1][1]:
    #    start = min(intervals[index-1][0], intervals[index][0])
    #    end = max(intervals[index-1][1], intervals[index][1])
    #    index += 1 
    # rst.append([start, end])

    # while index < len(intervals):
    #     rst.append(intervals[index])
    #     index += 1

    # return rst    

    for interval in intervals:
        if not rst or rst[-1][1] < interval[0]:
            rst.append(interval)
        else:
            rst[-1][1] = max(rst[-1][1], interval[1])
    return rst


print(merge(intervals=[[1,3],[2,6],[15,18], [8,10]]))
print(merge(intervals=[[1,10]]))
print(merge(intervals=[[1,4], [5,6]]))