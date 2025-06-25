# 815 Bus Route
# You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

# For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
# You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

# Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

# Example 1:

# Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# Output: 2
# Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
# Example 2:

# Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
# Output: -1

from typing import List
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        distance = 1
        stop_to_bus = defaultdict(list)
        for bus in range(len(routes)):
            for busstop in routes[bus]:
                stop_to_bus[busstop].append(bus)
        
        print("---stop to bus---")
        print(stop_to_bus)

        visitedBus = set()
        curStops = set()
        visitedStop = set()
        for bus in stop_to_bus[source]:
            visitedBus.add(bus)
            for stop in routes[bus]:
                if stop == target:
                    return distance
                
                curStops.add(stop)
                visitedStop.add(stop)
        
        
        
        while curStops:
            newStops = set()
            distance += 1 
            for stop in curStops:
                for bus in stop_to_bus[stop]:
                    if bus not in visitedBus:
                        visitedBus.add(bus)
                        for next_stop in routes[bus]:
                            if next_stop == target:
                                return distance
                            if next_stop not in visitedStop:
                                visitedStop.add(next_stop)
                                newStops.add(next_stop)

               
            curStops = newStops        
        return -1


sol = Solution()

print(sol.numBusesToDestination([[1,2,7],[3,6,7]], 1, 6)) # 2
print(sol.numBusesToDestination([[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 22)) # -1