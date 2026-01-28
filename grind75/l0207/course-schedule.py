# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
from typing import List
from collections import deque

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = {i: [] for i in range(numCourses)}
    degree = [0] * numCourses

    for pre in prerequisites:
        child, parent = pre[0], pre[1]
        graph[parent].append(child)
        degree[child] += 1
    
    sources = deque([])
    for i in range(numCourses):
        if degree[i] == 0:
            sources.append(i)

    scheduled = 0
    while sources:
        node = sources.popleft()
        scheduled += 1
        for child in graph[node]:
            degree[child] -= 1
            if degree[child] == 0:
                sources.append(child)
    
    return scheduled == numCourses