# https://algo.monster/liteproblems/253

from heapq import heappop, heappush

def minMeetingRooms(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0
    
    free_rooms = [] # heap, the len of heap is the number of room needed

    intervals.sort(key= lambda x: x[0])

    heappush(free_rooms, intervals[0][1])

    for i in intervals[1:]:
        if free_rooms[0] < i[0]:
            heappop(free_rooms)
        heappush(free_rooms, i[1])
    
    return len(free_rooms)