# 253 Meeting Room II
import heapq
from typing import List

def minMeetingRooms(intervals: List[List[int]]) -> int:
    hp = []

    intervals = sorted(intervals)
    for begin, end in intervals:
        if not hp:
            hp.append((end, begin))
            continue

        if hp[0][0] < begin:
            heapq.heappop(hp)
        
        heapq.heappush(hp, (end, begin))
    return len(hp)

print(minMeetingRooms([[0, 30], [5, 10], [15, 20]])) # 2
print(minMeetingRooms([[1,2],[4,5],[8,10]])) # 1
print(minMeetingRooms([[1,2]])) # 1